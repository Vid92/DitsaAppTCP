import logging
from time import sleep, time

import StringUtils

import os
import sys
import subprocess
import shared
import math
from enum import Enum

import shared
from shared import DEV,DEV_ADDR
import appsettings
#from appsettings import useHostname,usePort
from appsettings import useIp,usePort

from devinterface import devInterface

from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QScrollBar
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QDesktopServices
from PyQt5.QtCore import QEventLoop, QByteArray, Qt, QUrl, pyqtSignal, pyqtSlot, QObject, QTimer

logger = logging.getLogger(__name__)

class ACTION(Enum):
	PASS = 0
	FAIL = 1

class BCmb(object):
	timeout = 1
	attempts = 1
	x = 0

	#------------------------------------------- Client -------------------------------------------#
	@staticmethod
	def writeProgramClient(ip,port,program_in_json):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(ip,port, 0x57,program_in_json,10)
		print("resultW:",result)
		if result != None:
			if result[1] == 'PASS':
				result = result[1]
				BCmb.x = BCmb.x + 1
				print("count: ",BCmb.x)
				if(BCmb.x == 17):#checar esta parte
					print("ACTION:TRUE")
					BCmb.x = 0
			else:
				result = result[1]
		return result  
	
	@staticmethod			#programa eeprom disk2 cambia ip,gt,mr 
	def disk2Client(ip,port,ip_gaterway_mask):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(ip,port, 0x45,ip_gaterway_mask,10)
		print("resultW:",result)
		if result != None:
			if result[1] == 'PASS':
				result = result[1]
			else:
				result = result[1]
		return result 

	@staticmethod
	def runClient(ip,port):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(ip,port, 0x33, "", BCmb.timeout)
		print("resultRun:",result)
		if result != None:
			if result[1] == 'PASS,RUN':
				result = result[1]
			else:
				result = result[1]
		return result

	@staticmethod
	def pauseClient(ip,port):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(ip,port, 0x34, "", BCmb.timeout)
		print("resultP:",result)
		if result != None:
			if result[1] == 'PASS,PAUSE':
				result = result[1]
			else:
				result = result[1]
				
		return result
	
	@staticmethod
	def stopClient(ip,port):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(ip,port, 0x35, "", BCmb.timeout)
		print("STP:",result)
		if result != None:
			if result[1] == 'PASS,STOP':
				result = result[1]
			else:
				result = result[1]
		return result

	#es probable que ya no sea necesaria
	@staticmethod
	def pingDataClient(ip,port,listaAddr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponseWithoutAddr(ip,port,0x65,listaAddr,BCmb.timeout)
		#print("pingDataCl:",result)
		if result != None:
			if result[1] == 'PASS':
				result = True
			else:
				result = False
		return result
	

	@staticmethod
	def pingClient(ip,port):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(ip,port,0x64, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = True
			else:
				result = False
		return result

	@staticmethod
	def readDataClient(ip,port):
		result = ACTION.FAIL
		res = devInterface.sendClientCommandAndGetResponse(ip,port,0x43, "", BCmb.timeout)
		print(res)
		result=None
		if res != None:
			if res[0] == 'VALUE':
				result = res[1].split(',')
			else:
				result = None
		return result

	'''
	@staticmethod
	def startPollingClient(hostname,port):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponseWithoutAddr(hostname,port,0x36, "", BCmb.timeout)
		#print(result)
		if result != None:
			if result[1] == 'PASS':
				result = result[1]
			else:
				result = None
		return result
	
	@staticmethod
	def stopPollingClient(hostname,port):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponseWithoutAddr(hostname,port,0x37, "", BCmb.timeout)
		#print("stopP:",result)
		if result != None:
			if result[1] == 'PASS':
				result = result[1]
			else:
				result = result[1]
		return result

	@staticmethod
	def memoryDataClient(hostname,port):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponseWithoutAddr(hostname,port,0x38, "", BCmb.timeout)
		#print(result)
		if result != None:
			if result[0] == 'VALUE':
				result = result[1].split(';')
			else:
				result = None
		return result

	
	@staticmethod
	def readProgramClient(hostname,port,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,port,addr, 0x52, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[0] == 'VALUE':
				result = result[1]
			else:
				result = None
		return result
	'''
	
if __name__ == "__main__":
	print("tests")

	'''
	BCmb.startPollingClient(useHostname)
	sleep(.1)
	BCmb.stopPollingClient(useHostname)
	sleep(.3)
	BCmb.memoryDataClient(useHostname)
	'''
	#BCmb.runClient(useHostname, 1)
	
	#for j in range(100):
	#	for i in range(2):
	#		BCmb.startPollingClient(useHostname[i],usePort[i]) 
			#BCmb.memoryDataClient(useHostname[i],usePort[i])

	#BCmb.stopPollingClient(useHostname)

	#   BCmb.pingClient(useHostname,1)
		#BCmb.readDataClient(useHostname, 2)
	#adr = ["1","1","23"]
	#for j in range(2):
	#BCmb.pingDataClient('ditsaServer2.local',65434,"['17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']")
	#print(adr[0])

	##Prueba rapida 

	#BCmb.runClient('192.168.1.73',9000)
	#for i in range(1000):
	#	BCmb.readDataClient('192.168.1.73',9000)
	#	sleep(5)

	#BCmb.pingClient('192.168.0.70',9000)
	#BCmb.runClient('192.168.1.25',9000)
	#BCmb.stopClient('192.168.1.25',9000)
	#BCmb.pauseClient('192.168.1.25',9000)
	#for i in range(5000):
	#	BCmb.readDataClient('192.168.0.25',9000)
	#	sleep(1)

	BCmb.disk2Client('192.168.0.25',9000,"192.168.0.72,255.255.255.0,192.168.0.1")
	#program = ["2-SGL   [1{\"T\":\"Bg\",\"                                           \"},","2{\"T\":\"Ch\",\"C\":\"0015\",\"H\":\"000.583\",\"M\":\"0067\",\"m\":\"0040\"},","3{\"T\":\"Ch\",\"C\":\"0017\",\"H\":\"000.666\",\"M\":\"0075\",\"m\":\"0040\"},","4{\"T\":\"Pa\",\"           H\":\"000.416\",\"                   \"},","5{\"T\":\"Ch\",\"C\":\"0019\",\"A\":\"0009.49\",\"M\":\"00.0\",\"m\":\"00.0\"},","6{\"T\":\"Ed\",\"                                            \"},","7{\"                                                     \"},","8{\"                                                     \"},","9{\"                                                     \"},","10{\"                                                     \"},","11{\"                                                     \"},","12{\"                                                     \"},","13{\"                                                     \"},","14{\"                                                     \"},","15{\"                                                     \"},","16{\"                                                     \"},","17{\"                                                     \"}]"]
	#BCmb.writeProgramClient('192.168.1.73',9000,"[{\"T\":\"Bg\",\"                                           \"},{\"T\":\"Ch\",\"C\":\"22.7\",\"H\":\"000.083\",\"M\":\"00.0\",\"m\":\"00.0\"},{\"T\":\"Ch\",\"C\":\"12.3\",\"A\":\"004.099\",\"M\":\"0075\",\"m\":\"37.7\"},{\"T\":\"Pa\",\"           \H\":\"000.166\",\"                   \"},{\"T\":\"Ch\",\"C\":\"0019\",\"H\":\"0000.25\",\"M\":\"00.0\",\"m\":\"00.0\"},{\"T\":\"Ch\",\"C\":\"0024\",\"A\":\"011.997\",\"M\":\"0068\",\"m\":\"0035\"},{\"T\":\"Pa\",\"           H\":\"00000.1\",\"                   \"},{\"T\":\"Ch\",\"C\":\"0015\",\"A\":\"006.248\",\"M\":\"0057\",\"m\":\"0035\"},{\"T\":\"Ed\",\"                                            \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"}]")
	#BCmb.writeProgramClient('192.168.1.73',9000,"2-SGL[{\"T\":\"Bg\",\"                                           \"},{\"T\":\"Ch\",\"C\":\"0022\",\"H\":\"000.583\",\"M\":\"0067\",\"m\":\"0040\"},{\"T\":\"Ch\",\"C\":\"0017\",\"H\":\"000.666\",\"M\":\"0075\",\"m\":\"0040\"},{\"T\":\"Pa\",\"           H\":\"000.416\",\"                   \"},{\"T\":\"Ch\",\"C\":\"0019\",\"A\":\"0009.49\",\"M\":\"00.0\",\"m\":\"00.0\"},{\"T\":\"Ed\",\"                                            \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"}]")
	#BCmb.writeProgramClient('192.168.1.73',9000,"2-SGL[{\"T\":\"Bg\",\"                                           \"},{\"T\":\"Ch\",\"C\":\"0022\",\"H\":\"000.583\",\"M\":\"0067\",\"m\":\"0040\"},{\"T\":\"Ch\",\"C\":\"0017\",\"H\":\"000.666\",\"M\":\"0075\",\"m\":\"0040\"},{\"T\":\"Pa\",\"           H\":\"000.416\",\"                   \"},{\"T\":\"Ch\",\"C\":\"0019\",\"A\":\"0009.49\",\"M\":\"00.0\",\"m\":\"00.0\"},{\"T\":\"Ed\",\"                                            \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"}]")
	#for i in range(17):
	#	print("program[]:",program[i])
	#	BCmb.writeProgramClient('192.168.1.73',9000, program[i])
	#	sleep(2)
	#BCmb.writeProgramClient('192.168.1.73',9000,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"25\"},{\"Type\":\"Charge\",\"Time\":\"30\",\"Current\":\"30.0\"},{\"Type\":\"Charge\",\"Time\":\"1800\",\"Current\":\"27.4\"},{\"Type\":\"Carga\",\"Time\":\"1200\",\"Current\":\"18.6\"},{\"Type\":\"Pause\",\"Time\":\"180\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"9.0\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"12.4\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"22.2\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"8.8\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"25.6\"},{\"Type\":\"Pause\",\"Time\":\"180\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"17.2\"},{\"Type\":\"End\"}]")
	#BCmb.writeProgramClient('192.168.1.73',9000,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"15\"},{\"Type\":\"Charge\",\"Time\":\"60\",\"Current\":\"28.3\"},{\"Type\":\"Pause\",\"Time\":\"46\"},{\"Type\":\"Charge\",\"Time\":\"180\",\"Current\":\"20.8\"},{\"Type\":\"Carga\",\"Time\":\"40\",\"Current\":\"30.0\"},{\"Type\":\"Pause\",\"Time\":\"15\"},{\"Type\":\"Charge\",\"Time\":\"60\",\"Current\":\"25.7\"},{\"Type\":\"Pause\",\"Time\":\"20\"},{\"Type\":\"Charge\",\"Time\":\"120\",\"Current\":\"26.4\"},{\"Type\":\"Charge\",\"Time\":\"30\",\"Current\":\"18.9\"},{\"Type\":\"End\"}]")
	#BCmb.writeProgramClient('192.168.1.73',9000,"[{\"Type\":\"Begin\"},{\"Type\":\"Charge\",\"Time\":\"180\",\"Current\":\"30.0\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"25.6\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Carga\",\"Time\":\"600\",\"Current\":\"10.5\"},{\"Type\":\"Carga\",\"Time\":\"1200\",\"Current\":\"19.2\"},{\"Type\":\"Carga\",\"Time\":\"600\",\"Current\":\"28.4\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"23.5\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"14.7\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Pause\",\"Time\":\"120\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"17.7\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"9.5\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"24.8\"},{\"Type\":\"End\"}]")

