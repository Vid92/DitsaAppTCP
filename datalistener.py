from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate
import shared
import appsettings

from devicemainboard import BCmb

logger = logging.getLogger(__name__)

class ACTION(Enum):
    PASS = 0
    FAIL = 1

class DataListener(Thread):


    mySrc = None

    _stop_event = None


    def __init__(self, args):
        '''Constructor'''
        Thread.__init__(self)
        self._args = args
        self._name = "DataListener Thread"
        if args != None:
            self.mySrc = Communicate()
            self.mySrc.myGUI_signal.connect(args)
        
        self._stop_event = Event()
        self._stop_event.clear()
        
        
    def run(self):

        #try:
        print(self._name+" started")
        
        self.pingForDevicesPresent()

        while not self._stop_event.is_set():
            
            # we do ping to the devices 
    
            for i in range(shared.devStart,shared.devStop+1):
                address=i

                if shared.DEV[address][0] == True:
                    print("Doing asking data to device No."+str(address))
                    readData = BCmb.readDataClient('ditsa-Lenovo-C20-00.local', address)
                    print("VALUE:")
                    print(readData)
                    if readData!= None:
                        #we store current
                        shared.DEV[address][1] = str(readData[0]).replace('I','')
                        #we store voltage
                        shared.DEV[address][2] = str(readData[1]).replace('V','')
                        #we store temperature
                        shared.DEV[address][3] = str(readData[2]).replace('T','')
                        #we store step number and type
                        shared.DEV[address][4] = str(readData[3]).replace('P','')
                        #we store time of current step
                        shared.DEV[address][5] = str(readData[4].replace('t',''))
                        #we store total time program
                        shared.DEV[address][6] = str(readData[5].replace('t',''))

                        self.dataStr = str(readData[0])
                
                    #['VALUE', 'I0.27,V-0.98,T27.21']
                    if readData != None:
                        if self.mySrc != None:
                            self.mySrc.myGUI_signal.emit("DL["+str(address)+"]:DataReady")
            '''
            
            sleep(.1)

            print(self._name+" stopped")
        
            '''
        '''
        except:
            print("ERROR SERVER WHEN ASKING DATA")
            self.stop()
        '''

    def stop(self):
        print("stop was done in "+self._name)
        self._stop_event.set()

    def join(self, *args, **kwargs):
        self.stop()
        super(DataListener,self).join(*args, **kwargs)

    def pingForDevicesPresent(self):
        # we do ping to the devices 
 
        for i in range(shared.devStart, shared.devStop+1):
            address=i
            print("Doing ping to device No."+str(address))
            readData = BCmb.pingClient('ditsa-Lenovo-C20-00.local', address)
            print("VALUE:")
            print(str(readData))
            shared.DEV[i][0] = False
            if readData!= None:
                if readData == True:
                    shared.DEV[i][0] = True
                    print("DEV"+str(address)+" is Present!")  
                else:
                    print("DEV"+str(address)+" is not Present!")
            else:
                print("DEV"+str(address)+" is not Present!")

if __name__ == '__main__':
    logger.debug("demo")
    main = DataListener(None)
    #main.daemon = True
    main.start()
    #main.stop()