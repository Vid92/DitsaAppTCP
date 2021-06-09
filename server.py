import socket
import sys
from _thread import start_new_thread
import threading

import USBUtils
import SerialPortUtil
import StringUtils
from serialcommthread import SerialCommThread, serial_cmd_result

from time import sleep, time

import serial
import appsettings 
from appsettings import useHostname,usePort
from datalistenerserver import DataListenerServer
from devinterface import  devInterface
#from testLcd import LCD

import shared
from shared import lock_uart, lock_memory,devStart,devStop,DEV,DA_PI,ON_PI
from devicemainboard import BCmb
from downloadsFileServer import FilesServer

#sleep(10)
HOST = useHostname #'raspberrypi.local' # all availabe interfaces
PORT = usePort # arbitrary non privileged port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
except socket.error as msg:
    print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
    sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except socket.error as msg:
    print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()

s.listen(10)
print("Listening...")

#ds = DataListenerServer(None)

# The code below is what you're looking for ############

#lcd = LCD()
#lcd.clear()
#lcd.write_line1('Listenig...',1)
#lcd.lcd_string('Local IP Address:',2)
#lcd.lcd_string('Listening...',1)

#lock = threading.Lock()
#op_data = False

ds = None

def client_thread(conn):
    global ds
    while True:
        p_data = conn.recv(1024)
        if not p_data:
            break
        
        result = None
        data = None
        
        try:
            #cmd_data = bytes(cmd,'ISO-8859-1')
            #p_data = devInterface.packMessage(address, op, cmd_data)
        
            if appsettings.useDongle == True:
                print("Test Mac Server")
                sp = SerialPortUtil.getFirstPortByVID_PID(0x1a86,0x7523)
                #print(sp)
                #print("p_data")
                #print(p_data)
                op_code = 0x57
                st_polling = 0x36
                cl_polling = 0x37
                op_data = 0x38
                da_ping = 0x65
                t_out = 10
                
                
                if p_data[1] == st_polling:
                    print("START_POLLING")
                    #msg = devInterface.unpackMessage(p_data)
                    msg = devInterface.unpackMessageWithoutAddr(p_data)
                   
                    ds = DataListenerServer(None)
                    ds.start()
                    ds.join()
                    
                    tmp = bytes("ACTION: PASS", 'ISO-8859-1')

                    data = bytes(devInterface.packMessageWithoutAddr(msg[1],tmp))
                    #data = bytes(devInterface.packMessage(msg[1], msg[2], tmp))
                    #print("DATA1:",data)

                elif p_data[1]== cl_polling:
                    print("STOP_POLLING")
                    #msg = devInterface.unpackMessage(p_data)
                    msg = devInterface.unpackMessageWithoutAddr(p_data)
                    #print("msg:",msg)
                    tmp = bytes("ACTION: PASS", 'ISO-8859-1')
                    if ds is not None:
                        #print("Have Value: ")
                        #print(ds)
                        ds.stop()                        
                    #data = bytes(devInterface.packMessage(msg[1], msg[2], tmp))
                    data = bytes(devInterface.packMessageWithoutAddr(msg[1], tmp))
                    #print("DATA2:",data)

                elif p_data[1] == da_ping: 
                    print("DATAPING")
                    msg = devInterface.unpackMessageWithoutAddr(p_data)
                    #print("msg:",msg[2])
                               
                    new = msg[2].decode("utf-8")
                    test = new.split('e')
                    test2 = test[1]
                    test2 = test2.split("'")
                    
                    shared.DA_PI.clear()
                    shared.ON_PI.clear()
                    shared.RE_PI.clear()
                    for i in range(len(test2)):
                        if test2[i].isdigit():    
                            shared.DA_PI.append(int(test2[i]))
                            
                    print("sharedDA:",shared.DA_PI)
                    
                    #preguntaria del 1 al 16 no importa lo que tenga shared OJO!!
                    
                    #hace ping a todos los modulos
                    for i in range(shared.devStart,shared.devStop+1): #len(shared.DA_PI)
                        #address = shared.DA_PI[i]
                        address = i

                        #print("Doing ping to device No."+str(address))
                        readData = BCmb.ping(address)
                        #print("VALUE:",str(readData))
                        
                        shared.DEV[address][0] = False
                        if readData!= None:
                            if readData == True:
                                shared.DEV[address][0] = True
                                shared.ON_PI.append(int(address))
                                shared.RE_PI.append(int(shared.DA_PI[i-1]))
                                print("DEV"+str(address)+" is Present!")  
                            else:
                                print("DEV"+str(address)+" is not Present!")
                                #ireport.end()
                        else:
                            print("DEV"+str(address)+" is not Present!")
                            #ireport.end()
                    
                    #dfile = FilesServer()
                    
                    tmp = bytes("ACTION: PASS", 'ISO-8859-1')                    
                    data = bytes(devInterface.packMessageWithoutAddr(msg[1], tmp))
                    #print("DATA3:",data)
                
                elif p_data[1]==op_data:
                    print("MEMORY_DATA")

                    #ds.stop()
                    #sleep(.2)                    
                    #msg = devInterface.unpackMessage(p_data)
                    lock_memory.acquire()
                    msg = devInterface.unpackMessageWithoutAddr(p_data)
                    #print("msg")
                    #print(msg)
                    #tmp = bytes("ACTION: PASS", 'ISO-8859-1')
                    #address = int(msg[1])
                    #print("started Acquire memory server")
                    tmp = "VALUE: "
                    for i in range (shared.devStart,shared.devStop+1): #len(DA_PI) #en vez de solo los que estan pregunta por todos ON_PI
                                    
                        address = i
                        #address = DA_PI[i]
                        #print("Address: "+str(address))
                        if DEV[address][0] == True: 
                            #DEV[address][0] = "True"
                            tmp += "{"
                            tmp +=  str(shared.DEV[address][0]) + "," +\
                                    "I" + shared.DEV[address][1] + "," +\
                                    "V" + shared.DEV[address][2] + "," +\
                                    "T" + shared.DEV[address][3] + "," +\
                                    "AH" + shared.DEV[address][4] + "," +\
                                    "AC" + shared.DEV[address][5] + "," +\
                                    "P" + shared.DEV[address][6] + "," +\
                                    "S" + shared.DEV[address][7] + "," +\
                                    "t" + shared.DEV[address][8] + "," +\
                                    "Tt" + shared.DEV[address][9] + "," +\
                                    "TT" + shared.DEV[address][10] + "," +\
                                    "" + shared.DEV[address][11] 
                            tmp += "}"
                        else:
                            tmp += "{"
                            tmp += str(shared.DEV[address][0])
                            tmp += "}"
                        tmp += ";"
                        #print(tmp)
                        
                    
                    #print("stop RELEASE memory server")
                    #print("TMP")
                    #print(tmp)
                    #data = bytes(devInterface.packMessage(msg[1], msg[2], bytes(tmp,'ISO-8859-1')))
                    data = bytes(devInterface.packMessageWithoutAddr(msg[1],bytes(tmp,'ISO-8859-1')))
                    lock_memory.release()
                    #print("DATA3:")
                    #print(data)           
                
                else:
                    
                    if p_data[2] == op_code:               #write eeprom json
                        t_out = 10
                        attempts = 1
                    else:
                        t_out = 1
                        attempts = 3
                    
                    try:
                        lock_memory.acquire()
                        sct = SerialCommThread(None, sp, appsettings.FTDI_baudRate, p_data, b'\x04',t_out,attempts)
                        sct.start()
                        sct.join()
                        
                        data = bytes(serial_cmd_result[0])
                        #print("DATA11:",data)
                        lock_memory.release()
                        
                    except:
                        print("Error: Serial Communication")
                    
                
                
            else:
                print("Test Raspbian")
                sp = SerialPortUtil.getPortByName("/dev/ttyS0")
                #print(sp)

            #sp = SerialPortUtil.getPortBySerialNumber(appsettings.FTDI_serialNumber)
            #sp = SerialPortUtil.getFirstPortByVID_PID(0x067b,0x2303)
            #sp = SerialPortUtil.getFirstPortByVID_PID(0x10c4,0xea60)
            if sp == None:
                raise Exception("devInterface", "No serial device found!")
                
            #print("serial thread stopped")
            #if sct.stopped() == False:
            #   e="serial thread not stopped"
            #   print("\033[1;31;40m"+str(e)+"\033[0;37;40m")

            '''
            result = None
            if data != None:
                result = devInterface.decodeMessage(data)
            else:
                result = None
            '''
        except Exception as e:
            print("\033[1;31;40m"+str(e)+"\033[0;37;40m")
        #return result

        #reply = b'OK . . '
        #reply = serial_cmd_result[0]
        #print('Received', repr(data))
        if data != None:
            conn.sendall(data)
            print("Send:",data)
        else:
            conn.sendall(b'None')
    print("[-] Closed connection")
    conn.close()

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
    ip_address = ''
    ip_address = s.getsockname()[0]
    
    #lcd.write_line2(ip_address,1)
    #print(ip_address)

    start_new_thread(client_thread, (conn,))

s.close()
