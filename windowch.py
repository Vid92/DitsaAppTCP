# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from io import open 
from os import scandir

import time 

from devicemainboard import BCmb
#from datalistenermemory import DataListenerMemory

from appsettings import useHostname,usePort
import shared

#from ordened import NameOrdened

class Ui_WindowCh(QtWidgets.QDialog):
	#def setupUi(self, WindowCh):
	def __init__(self,parent=None):
		super(Ui_WindowCh, self).__init__()
		self.parent = parent

		self.setObjectName("WindowCh")
		self.setFixedSize(392, 421) #self.setFixedSize(392, 384) 533-663
		self.BttnCancel = QtWidgets.QPushButton(self)
		self.BttnCancel.setGeometry(QtCore.QRect(110, 190, 80, 25))
		self.BttnCancel.setObjectName("BttnCancel")
		self.BttnDone = QtWidgets.QPushButton(self)
		self.BttnDone.setGeometry(QtCore.QRect(220, 190, 80, 25))
		self.BttnDone.setObjectName("BttnDone")
		self.textPrograms = QtWidgets.QComboBox(self)
		self.textPrograms.setGeometry(QtCore.QRect(50, 60, 301, 25))
		self.textPrograms.setObjectName("textPrograms")
		self.lblPrograms = QtWidgets.QLabel(self)
		self.lblPrograms.setGeometry(QtCore.QRect(160, 16, 81, 31))
		self.lblPrograms.setObjectName("lblPrograms")
		self.lblModules = QtWidgets.QLabel(self)
		self.lblModules.setGeometry(QtCore.QRect(130, 100, 151, 21))
		self.lblModules.setObjectName("lblModules")
		self.layoutWidget = QtWidgets.QWidget(self)
		self.layoutWidget.setGeometry(QtCore.QRect(80, 140, 251, 27))
		self.layoutWidget.setObjectName("layoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.lineEditMin = QtWidgets.QLineEdit(self.layoutWidget)
		self.lineEditMin.setObjectName("lineEditMin")
		self.lineEditMin.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[-A-Za-z\\d]*$"),self))
		self.horizontalLayout.addWidget(self.lineEditMin)
		self.label = QtWidgets.QLabel(self.layoutWidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.lineEditMax = QtWidgets.QLineEdit(self.layoutWidget)
		self.lineEditMax.setObjectName("lineEditMax")
		self.lineEditMax.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[-A-Za-z\\d]*$"),self))
		self.horizontalLayout.addWidget(self.lineEditMax)
		self.listWidget = QtWidgets.QListWidget(self)
		self.listWidget.setGeometry(QtCore.QRect(391, 0, 141, 421))
		self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
		self.listWidget.setObjectName("listWidget")
		self.BtnArrowR = QtWidgets.QPushButton(self)
		self.BtnArrowR.setGeometry(QtCore.QRect(300, 220, 89, 25))
		self.BtnArrowR.setObjectName("BtnArrowR")
		self.textEdit = QtWidgets.QTextEdit(self)
		self.textEdit.setGeometry(QtCore.QRect(0, 250, 391, 171))
		self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
		self.textEdit.setObjectName("textEdit")
		self.BtnArrowL = QtWidgets.QPushButton(self)
		self.BtnArrowL.setGeometry(QtCore.QRect(0, 220, 89, 25))
		self.BtnArrowL.setObjectName("BtnArrowL")
		self.tableWidget = QtWidgets.QTableWidget(self)
		self.tableWidget.setGeometry(QtCore.QRect(0, 420, 391, 241))
		self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
		self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget.setAlternatingRowColors(True)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(5)
		self.tableWidget.setRowCount(0)
		self.tableWidget.setHorizontalHeaderLabels(('Operation','Nominal','Time','Temp Max','Temp Min'))

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

		#self.newlist = list()
		self.loadProg = list()
		self.addrs = list()
		self.check = list()
		self.tempList = list()

		self.data1 = None
		self.data2 = None
		self.flagOutL = False
		self.flagChange = False

		self.flagFail = False	#flag para controlar el cierre de windowch
		self.flagSect = False

	def retranslateUi(self, WindowCh):
		_translate = QtCore.QCoreApplication.translate
		WindowCh.setWindowTitle(_translate("WindowCh", "Programs"))
		self.BttnCancel.setText(_translate("WindowCh", "Cancel"))
		self.BttnDone.setText(_translate("WindowCh", "Done"))
		self.lblPrograms.setText(_translate("WindowCh", "Programs"))
		self.lblModules.setText(_translate("WindowCh", "Selection of Modules"))
		self.label.setText(_translate("WindowCh", "-"))
		self.BtnArrowR.setText(_translate("WindowCh", ">>"))
		self.BtnArrowL.setText(_translate("WindowCh", "<<"))

		self.BtnArrowR.clicked.connect(self.on_bttnArrowR)
		self.BtnArrowL.clicked.connect(self.on_bttnArrowL)
		self.BttnDone.setDefault(True)
		self.lineEditMin.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditMax.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditMin.setMaxLength(8)
		self.lineEditMax.setMaxLength(8)
		self.lineEditMin.textChanged.connect(self.on_editMin)
		self.lineEditMax.textChanged.connect(self.on_editMax)
		self.BttnDone.clicked.connect(self.on_bttnDoneClicked)
		self.BttnCancel.clicked.connect(self.on_bttnCancelClicked)

		self.textPrograms.addItem('')		
		self.textPrograms.activated.connect(self.loadTableW)
		#self.listWidget.itemClicked.connect(self.uncheck_check)
		#self.textEdit.textChanged.connect(self.chtext)

	def showEvent(self,event):
		print("showEventWindowCh")
		self.on_cb_textPrograms()

		self.loadTableW() ##verificar lo que sucede si no hay programas

	def closeEvent(self,event):
		print("closeEventW")

	def on_editMin(self):
		y = self.lineEditMin.text()
		txt = y.upper()
		self.lineEditMin.setText(txt)

		self.data1 = "N="+txt
		self.on_editMax()

	def on_editMax(self):
		y = self.lineEditMax.text()
		txt = y.upper()
		self.lineEditMax.setText(txt)
		self.data2 = "N="+txt

		self.flagChange = False
		
		try:
			self.flagOutL = False
			value1 = self.parent.newlist.index(self.data1)
			value2 = self.parent.newlist.index(self.data2)

			self.flagChange = True
			value1 = value1 - 2
			value2 = value2 + 2

			valF = self.parent.newlist[value1:value2]
			#print("valF:",valF)
			self.check.clear()
			for i in range(2,len(valF),4):
				self.check.append(valF[i].replace('N=',''))

			self.btnCheckBox()

		except:
			self.flagChange = True
			if self.data1 != None and self.data1 !='N=':
				try:
					val1 = self.parent.newlist.index(self.data1)

					val1 = val1 - 2
					valF = self.parent.newlist[val1:val1+3]
					self.check.clear()
					for i in range(2,len(valF),4):
						self.check.append(valF[i].replace('N=',''))

					self.btnCheckBox()
				except:
					self.listWidget.clear()
			else:
				self.listWidget.clear()

			if self.data2 != None and self.data2 != 'N=':
				#print("no se encuentra")
				self.flagOutL = True
				self.listWidget.clear()
			#else:
				#print("data2 esta vacio")

	def uncheck_check(self):
		#print("uncheck_check")
		self.tempList.clear()
		for index in range(self.listWidget.count()):
			if self.listWidget.item(index).checkState() == QtCore.Qt.Checked:
				#print("check:",self.listWidget.item(index).text())
				self.tempList.append(self.listWidget.item(index).text())

		for i in range(2,len(self.parent.newlist),4):
			for j in range(len(self.tempList)):
				if 'N='+self.tempList[j] == self.parent.newlist[i]:
					self.loadProg.append(self.parent.newlist[i-2])
					self.loadProg.append(self.parent.newlist[i-1])
					self.loadProg.append(self.parent.newlist[i])
					self.loadProg.append(self.parent.newlist[i+1])

	def btnCheckBox(self):
		if self.flagChange != False:
			self.flagChange = False
			self.listWidget.clear()

			for i in range(len(self.check)):
				item = QtWidgets.QListWidgetItem(self.check[i])

				if shared.DEV[int(self.check[i])][0] == False:
					item.setFlags(QtCore.Qt.ItemIsUserCheckable)
					item.setCheckState(QtCore.Qt.Unchecked)
				else:
					item.setFlags(item.flags()|QtCore.Qt.ItemIsUserCheckable)
					item.setCheckState(QtCore.Qt.Checked)	

				self.listWidget.addItem(item)

	def on_cb_textPrograms(self):
		files=self.ls2("/home/ditsa/DitsaNet/ProfileEditorPrograms/")
		for file in files:
			nf = file.replace('.txt','')
			self.textPrograms.addItem(nf)

	def ls2(self,path): 
		return [obj.name for obj in scandir(path) if obj.is_file()]


	def on_clicked_textPrograms(self):
		self.nameFile = self.textPrograms.currentText()
		if self.nameFile != '':
			openFile = self.nameFile+".txt"
			#print("nameFile:",self.nameFile)
			archivo_texto = open("/home/ditsa/DitsaNet/ProfileEditorPrograms/"+openFile,"r")
			self.programJson = archivo_texto.read()
			archivo_texto.close()
			#print("json:",self.programJson)

	def chtext(self,flag,addr):
		if flag == 'msg':
			self.textEdit.append("Send programs...")
		elif flag == 'None':
			self.textEdit.append("ERROR COMM: "+addr)
		elif flag == 'PASS':
			self.textEdit.append("Load successful in Addr: "+addr)
		elif flag == 'FAIL':
			self.textEdit.append("Fail Load Addr: "+addr)
		elif flag == 'PASS,RUN':
			self.textEdit.append("run successful in Addr: "+addr)
		elif flag == 'FAIL,RUN':
			self.textEdit.append("Fail run Addr: "+addr)

		QtGui.QGuiApplication.processEvents()

	def on_bttnDoneClicked(self):
		print("clickDone")
		#----------------------------- Detiene thread -----------------------------#
		time.sleep(0.5) 
		self.parent.threadTimer(False)
		self.parent.threadData(False)
		#---------------------------- Extrae valor Addr ---------------------------#
		self.uncheck_check()
		self.addrs.clear()
		for i in range(3,len(self.loadProg),4):
			addr = self.loadProg[i].split('A=')
			self.addrs.append(addr[1])
		self.loadProg.clear()
		self.textEdit.clear()
		#---------------------------- Envia json a xmegas -------------------------#		
		self.chtext("msg","None")

		#for j in range(len(self.parent.saveprograms)):
		if self.textPrograms.currentText() != '':

			for j in range(len(useHostname)):
				section = self.parent.tempAddr[j]
				for i in range(len(section)):
					for k in range(len(self.addrs)):
						if section[i] == self.addrs[k]:

						#for i in range(len(self.addrs)):
							if int(section[i]) > 16:
								self.flagSect = True
								#print("section:",section[i])
								#print("i:",i+1)
								x = BCmb.writeProgramClient(useHostname[j],usePort[j],i+1,self.nameFile+self.programJson)

							else:
								x = BCmb.writeProgramClient(useHostname[j],usePort[j],int(self.addrs[k]),self.nameFile+self.programJson)

							#print("xx:",x)
							if x != None:
								if x == 'PASS':
									print("addr:",self.addrs[k])
									self.chtext(x,self.addrs[k])

									#self.checkPrograms(self.addrs[k])
									#self.parent.saveprograms.append(self.nameFile)
									#self.parent.saveprograms.append('A='+self.addrs[k])

									#self.settingsPrograms()

									#time.sleep(0.5)
									if self.flagSect != True:
										run = BCmb.runClient(useHostname[j],usePort[j],int(self.addrs[k]))
									else:
										run = BCmb.runClient(useHostname[j],usePort[j],i+1)
					
									if run != None:
										if run == 'PASS,RUN':
											self.chtext(run,self.addrs[k])

										else:
											self.chtext(run,self.addrs[k])
											self.flagFail = True

									else:
										self.chtext('None',self.addrs[k])
										self.flagFail = True
							
								else:
									self.chtext(x,self.addrs[k])
									self.flagFail = True

							else:
								self.chtext('None',self.addrs[k])
								self.flagFail = True
		else:
			for j in range(len(useHostname)):
				section = self.parent.tempAddr[j]
				for i in range(len(section)):
					for k in range(len(self.addrs)):
						if section[i] == self.addrs[k]:

						#for i in range(len(self.addrs)):
							x = BCmb.runClient(useHostname[j],usePort[j],int(self.addrs[k]))

							if x != None:
								if x == 'PASS,RUN':
									self.chtext(x,self.addrs[k])

								else:
									self.chtext(x,self.addrs[k])
									self.flagFail = True

							else:
								self.chtext('None',self.addrs[k])
								self.flagFail = True
								

		if self.flagFail != True:
			time.sleep(3)
			self.close()
		#solo falta realizar pruebas con comunicacion

	def checkPrograms(self,addr):
		print("checkPrograms")
		if self.parent.saveprograms!= None:
			if len(self.parent.saveprograms) != 0:
				for j in range(1,len(self.parent.saveprograms),2):
					if 'A='+addr == self.parent.saveprograms[j]:
						#print("entra",'A='+addr)
						self.parent.saveprograms.pop(j)	
						self.parent.saveprograms.pop(j-1)		
						break			

	def settingsPrograms(self):
		print("settingsPr")
		#settings = QtCore.QSettings('/home/ditsa/DitsaNet/Settings/fileprograms.ini', QtCore.QSettings.NativeFormat)
		#settings.setValue("saveprograms",self.parent.saveprograms)

		#print("saveP:",self.parent.saveprograms)
			
	def on_bttnCancelClicked(self):
		self.close()
		#cambiar este widget estructuralo mejor

	def loadTableW(self):
		print("loadProgramsTable")
		self.on_clicked_textPrograms()
		if self.nameFile != '':
			x = self.programJson.replace('[','')
			y = x.replace(']','')
			w = y.replace('{','')
			v = w.replace('}','')
			z = v.replace('"','')
			new = z.split('T:')

			#print("pJ:",programJson)
			#print("y:",y)
			#print("w:",w)
			#print("v:",v)
			#print("z:",z)
			#print("new:",new)
			steps = len(new)-3
			#print("Steps:",steps) #rows este valor es el numero de steps -3 (begin,end,'')
			self.tableWidget.setRowCount(steps)
			
			self.st = 0
			for i in range(len(new)):
				comp= new[i].split(',')
				for j in range(len(comp)-1):
					if comp[j] == 'Ch':
						self.st += 1
						#print("Carga")
						#print("comp:",comp)
						#print("len:",len(comp)-1) 
						self.tabItem('Charge',self.st-1,j)
						if len(comp)-1 == 5: # 5 implica /Carga/Current/AH-T/MaxTmp/MinTmp
							comp2 = comp[j+1].split(':')
							comp3 = comp[j+2].split(':')
							comp4 = comp[j+3].split(':')
							comp5 = comp[j+4].split(':')
							
							if comp2[0]=='C':
								current = float(comp2[1])
								self.tabItem(str(current),self.st-1,j+1)
							if comp3[0]=='A':
								ampH = float(comp3[1])
								self.tabItem(str(ampH)+'    AH',self.st-1,j+2)
							else:
								ampH = float(comp3[1])
								self.tabItem(str(ampH)+'    T',self.st-1,j+2)
							if comp4[0]=='M':
								maxTmp = float(comp4[1])
								self.tabItem(str(maxTmp),self.st-1,j+3)
							if comp5[0]=='m':
								minTmp = float(comp5[1])
								self.tabItem(str(minTmp),self.st-1,j+4)

						else: # 3 implica /Carga/Current/AH-T
							comp2 = comp[j+1].split(':')
							comp3 = comp[j+2].split(':')
							
							if comp2[0]=='C':
								current = float(comp2[1])
								self.tabItem(str(current),self.st-1,j+1)

							if comp3[0]=='A':
								ampH = float(comp3[1])
								self.tabItem(str(ampH)+'    AH',self.st-1,j+2)
							else:
								ampH = float(comp3[1])
								self.tabItem(str(ampH)+'    T',self.st-1,j+2)

					elif comp[j] =='Pa':
						self.st +=1
						self.tabItem('Pause',self.st-1,j)
						comp2 = comp[j+1].split(':')
						if comp2[0] =='           H':
							time = float(comp2[1])
							self.tabItem('-',self.st-1,j+1)
							self.tabItem(str(time)+'    T',self.st-1,j+2)
							self.tabItem('-',self.st-1,j+3)
							self.tabItem('-',self.st-1,j+4)

	def tabItem(self,name,rw,col):
		lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
		item = QtWidgets.QTableWidgetItem(name)
		item.setTextAlignment(QtCore.Qt.AlignCenter)
		item.setFont(lblt)
		#item.setBackground(QtGui.QColor('lightblue'))
		item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
		self.tableWidget.setItem(rw,col,item)

	flagClickR = False
	def on_bttnArrowR(self):
		#print("arrowR")
		if self.flagClickR != True and self.flagClickL !=True:
			self.flagClickR = True
			self.setFixedSize(533, 421)

		elif self.flagClickR != False and self.flagClickL !=False:
			self.flagClickR = False
			self.setFixedSize(392, 663)

		elif self.flagClickR != True and self.flagClickL !=False:
			self.flagClickR = True
			self.setFixedSize(533, 663)

		elif self.flagClickR != False and self.flagClickL !=True:
			self.flagClickR = False
			self.setFixedSize(392, 421)

		if self.flagOutL != True:
			self.btnCheckBox()


	flagClickL = False
	def on_bttnArrowL(self):
		#print("arrowL")
		if self.flagClickL != True and self.flagClickR != True:
			self.flagClickL = True
			self.setFixedSize(392, 663)

		elif self.flagClickL != False and self.flagClickR != False:
			self.flagClickL = False
			self.setFixedSize(533, 421)

		elif self.flagClickL != True and self.flagClickR !=False:
			self.flagClickL = True
			self.setFixedSize(533, 663)

		elif self.flagClickL != False and self.flagClickR !=True:
			self.flagClickL = False
			self.setFixedSize(392, 421)

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	WindowCh = QtWidgets.QDialog()
	ui = Ui_WindowCh()
	ui.setupUi(WindowCh)
	WindowCh.show()
	sys.exit(app.exec_())
'''