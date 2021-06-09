import logging
from time import sleep, time

from threading import Thread, Event
from queue import Queue

import USBUtils
import SerialPortUtil
import StringUtils

from communicate import Communicate

from shared import lock_uart,lock_memory

import serial
import appsettings

#if appsettings.useMac == False:
#   import RPi.GPIO as GPIO

serial_cmd_result = [None]

logger = logging.getLogger(__name__)

EN_485 =  4

class SerialCommThread(Thread):

    _begin_char = b'\x02'
    _end_char = b'\x04'
    _callback = None
    _serialport = None
    _serialnumber = None
    _baudrate = 115200
    _messagetosend = None
    _timeout = 1
    _attemps = 1

    _packet_being_received = False
    
    _start = 0
    _end = 0
    _elapsed = 0
    _stopevent = None

    _dataByteArray = []
    _dataBytesLiteral = b''

    _flagcommand = False
    _msgwasreceived = False

    def __init__(self, callbackFunc, serialport, baudrate, messagetosend, endchar, timeout, attempts=2):
        '''Constructor'''
        Thread.__init__(self)
        self._name = "SerialCommThread"
        self._portname = None



        if callbackFunc != None:
            self._callback = Communicate()
            self._callback.myGUI_signal.connect(callbackFunc)

        if baudrate != None:
            self._baudrate = baudrate

        if timeout != None:
            self._timeout = timeout

        if serialport != None and baudrate != None:
            self._serialport = serialport
            self._serialport.baudrate = self._baudrate
            self._serialport.rtscts = False
            self._serialport.dsrdtr = False
            self._serialport.timeout = 10
            self._serialport.writeTimeout = 1
            self._serialport.stopbits = serial.STOPBITS_ONE
            self._serialport.parity = serial.PARITY_NONE
            self._serialport.bytesize = serial.EIGHTBITS
            self._serialport.xonxoff = True

            self._serialport.setDTR(True)
            self._serialport.setRTS(False)
            
            self._portname = self._serialport.name
            
            if timeout>0:
                self._serialport.timeout = 0.25
        
        if not StringUtils.isNoneOrEmpty(messagetosend):
            self._messagetosend = messagetosend

        if not StringUtils.isNoneOrEmpty(endchar):
            self._end_char = endchar
        
        if attempts != None:
            self._attemps = attempts

        self._stopevent = Event()
        self._stopevent.clear()

        self._wasStopped = Event()
        self._wasStopped.clear()

    def run(self):

        print(self._name+" started")
        if appsettings.useMac == False:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(EN_485,GPIO.OUT)
            GPIO.output(EN_485,GPIO.LOW)

        while not self._msgwasreceived and not self._stopevent.is_set():
            if self._serialport != None:
                
                #print("clear result")
                serial_cmd_result[0] = None
                self._msgwasreceived = False
                for n in range(0, self._attemps):
                    #print("attemp " + str(n))
                    
                    # we sent the message data if there is any data
                    if not self._serialport.is_open:
                        self._serialport.open()
                        #print("opening serila port")

                    if self._messagetosend != None:
                       
                        print("doing attempt no."+str(n+1)+" msg:"+ ''.join(str( bytes(self._messagetosend), 'ISO-8859-1')))
                        self._serialport.flushOutput()
                        self._serialport.flushInput()
                        if appsettings.useMac == False:
                            GPIO.output(EN_485,GPIO.HIGH)
                        self._serialport.write(self._messagetosend)
                        sleep(.002)
                        if appsettings.useMac == False:
                            GPIO.output(EN_485,GPIO.LOW)

                    
                    # wait until we get the full message or timeout
                    #print("running loop")
                    self._start = time()
                    self._end = time()
                    self._elapsed = self._end-self._start
                    #print(self._elapsed)

                    if self._timeout == 0:
                        serial_cmd_result[0] = None
                        self.flag_command = False
                        
                        self.inicbuff()
                        self.stop()
                        continue
                    

                    if self._end_char != None:

                        while self._flagcommand == False and not self._stopevent.is_set() and (self._timeout == -1 or self._elapsed < self._timeout):# and appsettings.GLOBAL_TEST_STATUS != appsettings.TEST_CANCEL:
                            #print("rcv loop")
                            self._end = time()
                            self._elapsed = self._end-self._start
                            #print(self._elapsed)

                            if self._end_char:
                                #print("read from port")
                                self.read_from_port(self._serialport)
                            
                            if self._flagcommand == False and self._elapsed > self._timeout and self._timeout!= -1:
                                #print("timeout")
                                if self._callback != None:
                                    self._callback.myGUI_signal.emit("TesterThread[True]:"+"TIMEOUT!")
                                    raise Exception("Serial", "Device timeout!")

                            if self._msgwasreceived == True or self._stopevent.is_set():
                                #print("message was received")
                                break
                    
                    else:
                        sleep(self._timeout)

                    self._flagcommand = False
                    self.inicbuff()
                    #print("done serial loop")

                    if self._msgwasreceived == True or self._stopevent.is_set():
                        #print("message was received")
                        break

                self._flagcommand = False
                self.inicbuff()

                self._serialport.close()

                self.stop()

                print(self._name+" stopped")

            else:
                self.stop()
                raise Exception("Serial", "No device found!")

        #print("serial thread stopped")
        self._wasStopped.set()
        

    def stop(self):
        self._stopevent.set()
        print("stop was done in "+self._name)
    
    def stopped(self):
        return self._wasStopped.is_set()

    def join(self, *args, **kwargs):
        super(SerialCommThread,self).join(*args, **kwargs)

    def addcbuff(self, ser, c):
        lock_uart.acquire()
        if c == self._end_char:
            self._dataByteArray.append(ord(c))
            self._dataBytesLiteral = ''.join(str( bytes(self._dataByteArray), 'ISO-8859-1') )
            self.flag_command = True
            self.process_data(self._serialport)
            #print(c)
            self._packet_being_received = False
            #print("END")
        elif (c == self._begin_char) and (len(self._dataByteArray)<2):
            #print("BEGIN")
            self._packet_being_received = True
            self._flagcommand = False
            self.inicbuff()
            self._dataByteArray.append(ord(c))
            self._dataBytesLiteral = ''.join(str( bytes(self._dataByteArray), 'ISO-8859-1') )
            #print(c)
        else:
            if self._packet_being_received == True:
                self._dataByteArray.append(ord(c))
                self._dataBytesLiteral = ''.join(str( bytes(self._dataByteArray), 'ISO-8859-1') )
                #print(c)
        lock_uart.release()

    def inicbuff(self):
        #self._serialport.flushInput()
        self._dataByteArray.clear()
        self._dataBytesLiteral = b''
    
    def handle_data(self, ser, c):
        self.addcbuff(ser, c)
        

    def read_from_port(self, ser):
        if appsettings.useMac == False:
            GPIO.output(EN_485,GPIO.LOW)
        if not ser.is_open:
            # port is not open, we open the port
            ser.open()
        
        if ser.is_open:
            
            while ser.inWaiting()>0:
                n = ser.inWaiting()
                
                for _ in range(0, n):
                    reading = ser.read(1)
                    if len(reading) > 0:
                        self.handle_data(ser, reading)

    def process_data(self, ser):
        #print("process")
        self._msgwasreceived = True
        serial_cmd_result[0] = self._dataByteArray.copy()
        #print(serial_cmd_result[0])

    def tryToReconnect(self):
        print("try to reconnect")
        # to do

if __name__ == '__main__':
    logger.debug("demo")
    

    