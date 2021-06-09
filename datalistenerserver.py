from time import sleep, time

from threading import Thread, Event

import logging
from enum import Enum
from communicate import Communicate

from shared import lock_uart, lock_memory,devStart,devStop,DEV,DA_PI,ON_PI,RE_PI
#import shared
import appsettings

from devicemainboard import BCmb
from report import IndividualReport

logger = logging.getLogger(__name__)


ireport = IndividualReport()

class ACTION(Enum):
    PASS = 0
    FAIL = 1

class DataListenerServer(Thread):


    mySrc = None

    _stop_event = None
    _pause_event = None
    

    def __init__(self, args):
        '''Constructor'''
        Thread.__init__(self)
        self._args = args
        self._name = "DataListenerServer Thread"
        if args != None:
            self.mySrc = Communicate()
            self.mySrc.myGUI_signal.connect(args)
        
        self._stop_event = Event()
        self._stop_event.clear()
        
        self._pause_event = Event()
        self._pause_event.clear()
        
        
    def run(self):

        #try:
        print(self._name+" started")
        
        #self.pingForDevicesPresent() #verificar ping hacer pruebas 
        
        while not self._stop_event.is_set():
            
            # we do ping to the devices 
            lock_memory.acquire()
            for i in range(len(ON_PI)): #todos
                address = ON_PI[i]
                #print("DA_PI:",ON_PI[i])
                #print("DEV:",DEV[address][0])

                if DEV[address][0] == True:
                    print("Doing asking data to device No."+str(address))
                   
                    readData = BCmb.readData(address)
                    #print("ValueDLS:",readData)
                    
                    
                    if readData!= None and len(readData)==11:
                        #we store current
                        DEV[address][1] = str(readData[0].replace('I',''))
                        #we store voltage
                        DEV[address][2] = str(readData[1].replace('V',''))
                        #we store temperature
                        DEV[address][3] = str(readData[2].replace('T',''))
                        #we store step number and type
                        DEV[address][4] = str(readData[3].replace('AH',''))
                        #we store step number and type
                        DEV[address][5] = str(readData[4].replace('AC',''))
                        #we store step number and type
                        DEV[address][6] = str(readData[5].replace('P',''))
                        #we store step number and type
                        DEV[address][7] = str(readData[6].replace('S',''))
                        #we store time of current step
                        DEV[address][8] = str(readData[7].replace('t',''))
                        #we store current time program
                        DEV[address][9] = str(readData[8].replace('Tt',''))
                        #we store the total time program
                        DEV[address][10] = str(readData[9].replace('TT',''))
                        #we store the total time program
                        DEV[address][11] = str(readData[10].replace('',''))
                        '''
                        print("Current Value:")
                        print(DEV[address][1])
                        print(DEV[address][2])
                        print(DEV[address][3])
                        print(DEV[address][4])
                        print(DEV[address][5])
                        print(DEV[address][6])
                        print(DEV[address][7])
                        print(DEV[address][8]) 
                        '''
                        if (DEV[address][11] == 'S' or DEV[address][11] == 'E') and DEV[address][12] == True:
                            DEV[address][12] = False
                            ireport.appendWithTimeStampUsingFile(","+ DEV[address][1] + "," + DEV[address][2] + "," +\
                                                    DEV[address][3] + "," + DEV[address][4] + "," +\
                                                    DEV[address][5] + "," + DEV[address][6] + "," +\
                                                    DEV[address][7] + "," + DEV[address][8] + "," +\
                                                    DEV[address][9] + "," + DEV[address][10] + "," + DEV[address][11],str(RE_PI[i]))

                        if DEV[address][11] == 'R' or DEV[address][11] == 'P' or DEV[address][11] == 'T' or DEV[address][11] == 'W':
                            DEV[address][12] = True
                            ireport.appendWithTimeStampUsingFile(","+ DEV[address][1] + "," + DEV[address][2] + "," +\
                                                    DEV[address][3] + "," + DEV[address][4] + "," +\
                                                    DEV[address][5] + "," + DEV[address][6] + "," +\
                                                    DEV[address][7] + "," + DEV[address][8] + "," +\
                                                    DEV[address][9] + "," + DEV[address][10] + "," + DEV[address][11],str(RE_PI[i]))
                        
                    
                        #self.dataStr = str(readData[0])
                
                    #['VALUE', 'I0.27,V-0.98,T27.21']
                else:
                    self.pingForDevicesPresent(address)
                    
            #print("sleep22")
            sleep(.3)
            self.stop()
            #self._pause_event.set()
            lock_memory.release()
            #while not self._stop_event.is_set():
            #   print("stop_event")
            #   sleep(.2)
            #print(self._name+" stopped")
        
        '''
        except:
            print("ERROR SERVER WHEN ASKING DATA")
            self.stop()
 
        '''
        
    def pause(self):
        print("pause was done in "+self._name)
        self._pause_event.set()
    def resume(self):
        print("resume was done in "+self._name)
        self._pause_event.clear()
    def stop(self):
        print("stop was done in "+self._name)
        self._stop_event.set()

    def join(self, *args, **kwargs):
        #self.stop()
        super(DataListenerServer,self).join(*args, **kwargs)

    def pingForDevicesPresent(self,addr):
        # we do ping to the devices, falta agregar 3 timeout si los 3 son falso el quipo esta desconectado
        #print("Doing ping to device No."+str(addr))
        readData = BCmb.ping(addr)
        print("VALUE_PING_PRESENT:",str(readData))
        DEV[addr][0] = False
        if readData!= None:
            if readData == True:
                DEV[addr][0] = True
                print("DEV"+str(addr)+" is Present!")
            else:
                print("DEV"+str(addr)+" is not Present!")
        else:
            print("DEV"+str(addr)+" is not Present!")
        

if __name__ == '__main__':
    logger.debug("demo")
    #main.daemon = True
    main = DataListenerServer(None)
    main.start()
    main.stop()