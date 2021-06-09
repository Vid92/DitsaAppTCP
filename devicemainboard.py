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
from appsettings import useHostname,usePort

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

	#------------------------------------------- Client -------------------------------------------#
	@staticmethod
	def writeProgramClient(hostname,port,addr,program_in_json):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,port,addr, 0x57,program_in_json,10)
		print("resultW:",result)
		if result != None:
			if result[1] == 'PASS':
				result = result[1]
			else:
				result = result[1]
		return result  

	@staticmethod
	def runClient(hostname,port,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,port,addr, 0x33, "", BCmb.timeout)
		print("resultRun:",result)
		if result != None:
			if result[1] == 'PASS,RUN':
				result = result[1]
			else:
				result = result[1]
		return result

	@staticmethod
	def pauseClient(hostname,port,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,port,addr, 0x34, "", BCmb.timeout)
		print("resultP:",result)
		if result != None:
			if result[1] == 'PASS,PAUSE':
				result = result[1]
			else:
				result = result[1]
				
		return result
	
	@staticmethod
	def stopClient(hostname,port,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,port,addr, 0x35, "", BCmb.timeout)
		print("STP:",result)
		if result != None:
			if result[1] == 'PASS,STOP':
				result = result[1]
			else:
				result = result[1]
		return result

	@staticmethod
	def pingDataClient(hostname,port,listaAddr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponseWithoutAddr(hostname,port,0x65,listaAddr,BCmb.timeout)
		#print("pingDataCl:",result)
		if result != None:
			if result[1] == 'PASS':
				result = True
			else:
				result = False
		return result

	@staticmethod
	def pingClient(hostname,port,addr):
		result = ACTION.FAIL
		result = devInterface.sendClientCommandAndGetResponse(hostname,port,addr,0x64, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = True
			else:
				result = False
		return result

	@staticmethod
	def readDataClient(hostname,port,addr):
		result = ACTION.FAIL
		res = devInterface.sendClientCommandAndGetResponse(hostname,port,addr, 0x43, "", BCmb.timeout)
		print(res)
		result=None
		if res != None:
			if res[0] == 'VALUE':
				result = res[1].split(',')
			else:
				result = None
		return result

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

	#---------------------------------------------- Server --------------------------------------------#
	
	@staticmethod
	def ping(addr):
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponse(addr,0x64, "", BCmb.timeout)
		print("pingR:",result)
		if result != None:
			if result[1] == 'PASS':
				result = True
			else:
				result = False
		return result  

	@staticmethod
	def readData(addr):
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponse(addr, 0x43, "", 0.25)
		print("readData:",result)
		if result != None:
			DEV_ADDR[addr].clear()
			if result[0] == 'VALUE':
				result = result[1].split(',')
			else:
				result = None
		else:   #DEV[addr][0] = False
			DEV_ADDR[addr].append(False)
			#print("DEV_ADDR:",DEV_ADDR)
			if DEV_ADDR[addr].count(False) == 8:
				#print("Se perdio pingAddr")
				DEV_ADDR[addr].clear() 
				DEV[addr][0] = False
		return result

	'''
	@staticmethod
	def setAddress(address):
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponse(None, 0xFF, str(chr(address)), BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result

	@staticmethod
	def getAddress():
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponse(None, 0xFF, "", BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result

	'''
	@staticmethod
	def writeProgramFake(addr, program_in_json):
		result = ACTION.FAIL
		result = devInterface.sendCommandAndGetResponseFake(addr, 0x57, program_in_json, BCmb.timeout)
		print(result)
		if result != None:
			if result[1] == 'PASS':
				result = ACTION.PASS
			else:
				result = ACTION.FAIL
		return result

	
if __name__ == "__main__":
	print("tests")
	#BCmb.readData(1)
	#BCmb.pingClient(useHostname,1)
	#BCmb.ping(1)
	#BCmb.writeProgram(0, "[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"10000\"},{\"Type\":\"Charge\",\"Time\":\"120000\",\"Current\":\"8.0\"},{\"Type\":\"Charge\",\"Time\":\"50000\",\"Current\":\"12.0\"},{\"Type\":\"Carga\",\"Time\":\"60000\",\"Current\":\"15.0\"},{\"Type\":\"Charge\",\"Time\":\"40000\",\"Current\":\"20.0\"},{\"Type\":\"Pause\",\"Time\":\"20000\"},{\"Type\":\"Charge\",\"Time\":\"30000\",\"Current\":\"10.5\"},{\"Type\":\"Charge\",\"Time\":\"40000\",\"Current\":\"14.5\"},{\"Type\":\"End\"}]")
	#BCmb.readProgram(0)
	#BCmb.setAddress(1)
	#BCmb.run(1)
	#BCmb.stop(1)
	#BCmb.readStep(0)
	#BCmb.currentTime(0)
	#BCmb.readProgram(0)
	#BCmb.readDataClient(useHostname, 1)
	#BCmb.getAddress()
	
	#BCmb.stop(1)
	
	'''
	BCmb.getAddress()
	BCmb.readProgram(2)
	BCmb.run(2)
	'''
	
	
	
	#sleep(0.1)
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
	#adr = ["['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']"]
	#for j in range(2):
	#BCmb.pingDataClient('ditsaServer2.local',65434,"['17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32']")
	#print(adr[0])
	
	#BCmb.pingClient('ditsaServer2.local',65434,1)
	#BCmb.runClient('ditsaServer2.local',65434,1)
	#BCmb.stopClient('ditsaServer2.local',65434,1)
	#BCmb.pauseClient('ditsaServer2.local',65434,1)
	#BCmb.readDataClient('ditsaServer2.local',65434, 1)

	#BCmb.pingClient('ditsaServer1.local',65433,4)
	#BCmb.pingClient(useHostname,2)
	#BCmb.runClient(useHostname, 3)
	#BCmb.runClient('ditsaServer1.local',65433, 1)
	#BCmb.pauseClient(useHostname, 2)
	#BCmb.stopClient('ditsaServer1.local',65433,1)
	#BCmb.stopClient(useHostname, 3)
	#BCmb.readDataClient('ditsaServer1.local',65433, 1)
	#BCmb.readStepClient(useHostname, 3)
	#BCmb.currentTimeClient(useHostname, 1)
	#BCmb.readProgramClient(useHostname,1)
	#BCmb.writeProgramClient('ditsaServer2.local',65434,1,"[{\"T\":\"Bg\",\"                                           \"},{\"T\":\"Ch\",\"C\":\"22.7\",\"H\":\"000.083\",\"M\":\"00.0\",\"m\":\"00.0\"},{\"T\":\"Ch\",\"C\":\"12.3\",\"A\":\"004.099\",\"M\":\"0075\",\"m\":\"37.7\"},{\"T\":\"Pa\",\"           \H\":\"000.166\",\"                   \"},{\"T\":\"Ch\",\"C\":\"0019\",\"H\":\"0000.25\",\"M\":\"00.0\",\"m\":\"00.0\"},{\"T\":\"Ch\",\"C\":\"0024\",\"A\":\"011.997\",\"M\":\"0068\",\"m\":\"0035\"},{\"T\":\"Pa\",\"           H\":\"00000.1\",\"                   \"},{\"T\":\"Ch\",\"C\":\"0015\",\"A\":\"006.248\",\"M\":\"0057\",\"m\":\"0035\"},{\"T\":\"Ed\",\"                                            \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"}]")
	BCmb.writeProgramClient('ditsaServer2.local',65434,1,"2-SGL[{\"T\":\"Bg\",\"                                           \"},{\"T\":\"Ch\",\"C\":\"0022\",\"H\":\"000.583\",\"M\":\"0067\",\"m\":\"0040\"},{\"T\":\"Ch\",\"C\":\"0017\",\"H\":\"000.666\",\"M\":\"0075\",\"m\":\"0040\"},{\"T\":\"Pa\",\"           H\":\"000.416\",\"                   \"},{\"T\":\"Ch\",\"C\":\"0019\",\"A\":\"0009.49\",\"M\":\"00.0\",\"m\":\"00.0\"},{\"T\":\"Ed\",\"                                            \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"},{\"                                                     \"}]")
	#BCmb.writeProgramClient(useHostname,1,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"25\"},{\"Type\":\"Charge\",\"Time\":\"30\",\"Current\":\"30.0\"},{\"Type\":\"Charge\",\"Time\":\"1800\",\"Current\":\"27.4\"},{\"Type\":\"Carga\",\"Time\":\"1200\",\"Current\":\"18.6\"},{\"Type\":\"Pause\",\"Time\":\"180\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"9.0\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"12.4\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"22.2\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"8.8\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"25.6\"},{\"Type\":\"Pause\",\"Time\":\"180\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"17.2\"},{\"Type\":\"End\"}]")
	#BCmb.writeProgramClient(useHostname,1,"[{\"Type\":\"Begin\"},{\"Type\":\"Pause\",\"Time\":\"15\"},{\"Type\":\"Charge\",\"Time\":\"60\",\"Current\":\"28.3\"},{\"Type\":\"Pause\",\"Time\":\"46\"},{\"Type\":\"Charge\",\"Time\":\"180\",\"Current\":\"20.8\"},{\"Type\":\"Carga\",\"Time\":\"40\",\"Current\":\"30.0\"},{\"Type\":\"Pause\",\"Time\":\"15\"},{\"Type\":\"Charge\",\"Time\":\"60\",\"Current\":\"25.7\"},{\"Type\":\"Pause\",\"Time\":\"20\"},{\"Type\":\"Charge\",\"Time\":\"120\",\"Current\":\"26.4\"},{\"Type\":\"Charge\",\"Time\":\"30\",\"Current\":\"18.9\"},{\"Type\":\"End\"}]")
	#BCmb.writeProgramClient('ditsaServer1.local',65433,1,"[{\"Type\":\"Begin\"},{\"Type\":\"Charge\",\"Time\":\"180\",\"Current\":\"30.0\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"25.6\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Carga\",\"Time\":\"600\",\"Current\":\"10.5\"},{\"Type\":\"Carga\",\"Time\":\"1200\",\"Current\":\"19.2\"},{\"Type\":\"Carga\",\"Time\":\"600\",\"Current\":\"28.4\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"23.5\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"14.7\"},{\"Type\":\"Pause\",\"Time\":\"300\"},{\"Type\":\"Pause\",\"Time\":\"120\"},{\"Type\":\"Charge\",\"Time\":\"1200\",\"Current\":\"17.7\"},{\"Type\":\"Charge\",\"Time\":\"900\",\"Current\":\"9.5\"},{\"Type\":\"Charge\",\"Time\":\"1500\",\"Current\":\"24.8\"},{\"Type\":\"End\"}]")
	#x = BCmb.memoryDataClient(useHostname)
	#print("x:",x)



	'''
	while True:
		#BCmb.readData(1)
		
		#BCmb.readDataClient(useHostname, 1)
		#BCmb.readDataClient(useHostname, 2)
		#BCmb.readStepClient(useHostname, 2)
		sleep(.1)
	#'''
