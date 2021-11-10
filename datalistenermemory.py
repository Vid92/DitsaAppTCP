from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate
import shared
from shared import lock_uart, lock_memory,devStart,devStop,DEV,lock_client
import appsettings
from appsettings import useIp,usePort

from devicemainboard import BCmb
#from report import IndividualReport

logger = logging.getLogger(__name__)


class ACTION(Enum):
	PASS = 0
	FAIL = 1


class DataListenerMemory(Thread):

	mySrc = None
	_stop_event = None

	def __init__(self, args):
		'''Constructor'''
		Thread.__init__(self)
		self._args = args
		self._name = "DataListenerMemory Thread"
		if args != None:
			self.mySrc = Communicate()
			self.mySrc.myGUI_signal.connect(args)

		self._stop_event = Event()
		self._stop_event.clear()

		
	def run(self):
		print(self._name+" started")
		#lock_client.acquire()
		while not self._stop_event.is_set():
			'''
			for j in range(len(useIp)):
				#memoryPolling = BCmb.startPollingClient(useIp[j],usePort[j])
				readData = BCmb.readDataClient('192.168.1.25',9000)
				address = 1 #se tiene que modificar
				#sleep(.3)
				#print("memory:",memoryPolling)
				if readData!= None and len(readData)==12:

					shared.DEV[address][1] = str(readData[0].replace('I',''))
					#we store voltage
					shared.DEV[address][2] = str(readData[1].replace('V',''))
					#we store temperature
					shared.DEV[address][3] = str(readData[2].replace('T',''))
					#we store step number and type
					shared.DEV[address][4] = str(readData[3].replace('AH',''))
					#we store amper accumulate
					shared.DEV[address][5] = str(readData[4].replace('AC',''))
					#we store step number 
					shared.DEV[address][6] = str(readData[5].replace('P',''))
					#we store time of current status
					shared.DEV[address][7] = str(readData[6].replace('S',''))
					#we store current time program
					shared.DEV[address][8] = str(readData[7].replace('t',''))
					#we store the total time program
					shared.DEV[address][9] = str(readData[8].replace('Tt',''))
					#we store the total time program
					shared.DEV[address][10] = str(readData[9].replace('TT',''))
					#we store the name program
					shared.DEV[address][11] = str(readData[10].replace('N',''))
					#we store the total time program
					shared.DEV[address][12] = str(readData[11].replace('',''))
			'''
				#if memoryPolling != None:  
				#	if self.mySrc != None:
						#self.mySrc.myGUI_signal.emit("DL["+str(address)+"]:DataReady")
			self.mySrc.myGUI_signal.emit("DL[PASS]:DataReady")
			sleep(1)
		
		#lock_client.release()

	def stop(self):
		print("stop was done in "+self._name)
		self._stop_event.set()

	def join(self, *args, **kwargs):
		self.stop()
		super(DataListenerMemory,self).join(*args, **kwargs)

if __name__ == '__main__':
	logger.debug("demo")
	main = DataListenerMemory(None)
	# main.daemon = True
	main.start()
	# main.stop()
