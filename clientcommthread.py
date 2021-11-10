import logging
from time import sleep, time

from threading import Thread, Event
from queue import Queue

import USBUtils
#import SerialPortUtil
import StringUtils

from communicate import Communicate

#from shared import lock
import socket
#import serial
import appsettings


client_cmd_result = [None]

logger = logging.getLogger(__name__)


class ClientCommThread(Thread):

	_begin_char = b'\x02'
	_end_char = b'\x04'
	_callback = None
	_messagetosend = None
	_timeout = 1
	_attemps = 1
	_hostname = None
	_packet_being_received = False

	_start = 0
	_end = 0
	_elapsed = 0
	_stopevent = None

	_dataByteArray = []
	_dataBytesLiteral = b''

	_flagcommand = False
	_msgwasreceived = False

	def __init__(self, callbackFunc, hostname, port, messagetosend, endchar, timeout, attempts=1):
		'''Constructor'''
		Thread.__init__(self)
		self._name = "ClientCommThread"
		self._portname = None


		if callbackFunc != None:
			self._callback = Communicate()
			self._callback.myGUI_signal.connect(callbackFunc)

		if hostname != None:
			self._hostname = hostname
		
		if port != None:
			self._port = port

		if timeout != None:
			self._timeout = timeout


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
		try:
			while not self._msgwasreceived and not self._stopevent.is_set():
				if self._hostname != None:

					client_cmd_result[0] = None
					self._msgwasreceived = False
					for n in range(0, self._attemps):
						if self._messagetosend != None:

							#print("doing attempt no."+str(n+1)+" msg:"+ ''.join(str( bytes(self._messagetosend), 'ISO-8859-1')))
							print("doing attempt no."+str(n+1))
							HOST = self._hostname  # The server's hostname or IP address
							PORT = self._port		# The port used by the server

							client_cmd_result[0] = None
							self.flag_command = False
							self.inicbuff()
							data = None
							with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
								try: 
									s.connect((HOST, PORT))
									s.settimeout(5)
									s.sendall(bytes(self._messagetosend))
									data = s.recv(1024)

								except:
									print("", end='')

							if data!= None:
								print('Received', repr(data))
								self._msgwasreceived = True
								client_cmd_result[0]=data
							else:
								self._msgwasreceived = False
								client_cmd_result[0]=data

							if self._msgwasreceived == True or self._stopevent.is_set():
								break

						else:
							sleep(self._timeout)	

						self._flagcommand = False
						self.inicbuff()
						#print("done client loop")

						if self._msgwasreceived == True or self._stopevent.is_set():
							#print("message was received")
							break

					self._flagcommand = False
					self.inicbuff()

					self.stop()

					#lock.release()
				else:
					self.stop()
					raise Exception("Hostname", "No hostname found!")

			#print("client thread stopped")
			self._wasStopped.set()
			#lock.release()
		except:
			print("ERROR SERVER")
			self.stop()

	def stop(self):
		print("stop was done in "+self._name)
		self._stopevent.set()

	def stopped(self):
		return self._wasStopped.is_set()

	def join(self, *args, **kwargs):
		super(ClientCommThread,self).join(*args, **kwargs)

	def addcbuff(self, c):
		if c == self._end_char:
			self._dataByteArray.append(ord(c))
			self._dataBytesLiteral = ''.join(str( bytes(self._dataByteArray), 'ISO-8859-1') )
			self.flag_command = True
			self.process_data()
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

	def inicbuff(self):
		self._dataByteArray.clear()
		self._dataBytesLiteral = b''

	def handle_data(self, c):
		self.addcbuff(c)

	def process_data(self):
		self._msgwasreceived = True
		client_cmd_result[0] = self._dataByteArray.copy()

if __name__ == '__main__':
	logger.debug("demo")
	
	   
