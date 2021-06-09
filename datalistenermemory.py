from time import sleep, time

from threading import Thread, Event
from queue import Queue

import logging
from enum import Enum
from communicate import Communicate
import shared
from shared import lock_uart, lock_memory,devStart,devStop,DEV,lock_client
import appsettings
from appsettings import useHostname,usePort

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

		#memoryPolling = BCmb.startPollingClient(useHostname)
		#sleep(.3)
		
	def run(self):
		print(self._name+" started")
		#lock_client.acquire()
		while not self._stop_event.is_set():
			for j in range(len(useHostname)):
				memoryPolling = BCmb.startPollingClient(useHostname[j],usePort[j])
				#sleep(.3)
				#print("memory:",memoryPolling)

				#if memoryPolling != None:  
				#	if self.mySrc != None:
						#self.mySrc.myGUI_signal.emit("DL["+str(address)+"]:DataReady")
				self.mySrc.myGUI_signal.emit("DL[PASS]:DataReady")
		
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
