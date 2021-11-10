# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reconnectmodule.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import time 
from devicemainboard import BCmb
from appsettings import useIp,usePort

from ordened import NameOrdened
import shared


class Ui_recModule(QtWidgets.QDialog):
	#def setupUi(self, recModule):
	def __init__(self,parent=None):
		super(Ui_recModule, self).__init__()
		self.parent = parent

		self.setObjectName("recModule")
		self.setFixedSize(332,331) #332,331
		#self.resize(472, 331)
		self.buttonBox = QtWidgets.QDialogButtonBox(self)
		self.buttonBox.setGeometry(QtCore.QRect(80, 120, 161, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.listWidget = QtWidgets.QListWidget(self)
		self.listWidget.setGeometry(QtCore.QRect(331, 0, 141, 331))
		self.listWidget.setObjectName("listWidget")
		self.lineEditMin = QtWidgets.QLineEdit(self)
		self.lineEditMin.setGeometry(QtCore.QRect(60, 60, 80, 25))
		self.lineEditMin.setObjectName("lineEditMin")
		self.lineEditMax = QtWidgets.QLineEdit(self)
		self.lineEditMax.setGeometry(QtCore.QRect(180, 60, 80, 25))
		self.lineEditMax.setObjectName("lineEditMax")
		self.textEdit = QtWidgets.QTextEdit(self)
		self.textEdit.setGeometry(QtCore.QRect(0, 180, 331, 151))
		self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
		self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.textEdit.setObjectName("textEdit")
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QtCore.QRect(150, 60, 20, 25))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.lblModules = QtWidgets.QLabel(self)
		self.lblModules.setGeometry(QtCore.QRect(85, 20, 150, 20))
		self.lblModules.setObjectName("lblModules")
		self.widget = QtWidgets.QWidget(self)
		self.widget.setGeometry(QtCore.QRect(20, 150, 311, 27))
		self.widget.setObjectName("widget")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.BtnArrowR = QtWidgets.QPushButton(self.widget)
		self.BtnArrowR.setObjectName("BtnArrowR")
		self.horizontalLayout_2.addWidget(self.BtnArrowR)

		self.retranslateUi(self)
		#self.buttonBox.accepted.connect(self.accept)#cierra la ventana con un click
		#self.buttonBox.rejected.connect(self.reject)
		QtCore.QMetaObject.connectSlotsByName(self)

		self.check = list() 
		self.tempList = list()
		self.loadProg = list()
		self.addrs = list()

		self.flagChange = False
		self.flagFail = False	#flag para controlar el cierre de recmodule

	def retranslateUi(self, recModule):
		_translate = QtCore.QCoreApplication.translate
		recModule.setWindowTitle(_translate("recModule", "Reconnect"))
		self.label.setText(_translate("recModule", "-"))
		self.lblModules.setText(_translate("recModule", "Selection of Modules"))
		self.BtnArrowR.setText(_translate("recModule", ">>"))

		#conexion a funciones
		self.BtnArrowR.clicked.connect(self.on_bttnArrowR)
		self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.btnOk)
		self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.btnCancel)

		self.lineEditMin.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditMax.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEditMin.setMaxLength(8)
		self.lineEditMax.setMaxLength(8)
		self.lineEditMin.textChanged.connect(self.on_editMin)
		self.lineEditMax.textChanged.connect(self.on_editMax)

	def showEvent(self,event):
		pass

	def closeEvent(self,event):
		pass

	def on_editMin(self): #captura el dato en lineeditMin
		y = self.lineEditMin.text()
		self.txt = y.upper()
		self.lineEditMin.setText(self.txt)

		#print("tmpA:",self.parent.newlist)

		self.data1 = "N="+self.txt
		self.on_editMax()

	def on_editMax(self): #captura el dato en lineeditMax
		y = self.lineEditMax.text()
		self.txt2 = y.upper()
		self.lineEditMax.setText(self.txt2)

		self.data2 = "N="+self.txt2
		self.flagChange = False

		try:
			self.flagOutL = False

			value1 = self.parent.newlist.index(self.data1)
			value2 = self.parent.newlist.index(self.data2)

			self.flagChange = True
			value1 = value1 - 2
			value2 = value2 + 2

			valF = self.parent.newlist[value1:value2]
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
				self.flagOutL = True
				self.listWidget.clear()

	def chtext(self,flag,addr):
		if flag == 'msg':
			self.textEdit.append("Comm Reconnect")
		elif flag == 'None':
			self.textEdit.append("ERROR COMM: "+addr)
		elif flag == 'PASS':
			self.textEdit.append("Reconnect successful in Addr: "+addr)
		elif flag == 'FAIL':
			self.textEdit.append("Fail reconnect Addr: "+addr)

		QtGui.QGuiApplication.processEvents()

	def btnOk(self):
		print("btnOkRec")
		#----------------------------- Detiene thread -----------------------------#
		#time.sleep(0.5)
		#self.parent.threadData(False) 
		#---------------------------- Extrae valor Addr ---------------------------#	
		self.uncheck_check()
		self.addrs.clear()

		if len(self.loadProg) != 0:
			for i in range(3,len(self.loadProg),4):
				addr = self.loadProg[i].split('A=')
				self.addrs.append(addr[1])

			self.loadProg.clear()
			self.textEdit.clear()
			#---------------------------- Envia comando run ---------------------------#
			self.chtext("msg","None")
			
			for j in range(len(useIp)):
				section = self.parent.tempAddr[j]
				for i in range(len(section)):
					for k in range(len(self.addrs)):
						if section[i] == self.addrs[k]:
							
							if int(section[i]) > 16:
								print("section:",section[i])
								print("i:",i+1)
								x = BCmb.pingClient(useIp[j],usePort[j],i+1)

							else:
								x = BCmb.pingClient(useIp[j],usePort[j],int(self.addrs[k]))
								#time.sleep(0.3)#sujeto a cambios
					
							print("x:",x)
							if x != None:
								if x == 'PASS':
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
		else:
			if self.flagFail != True:
				time.sleep(3)
				self.close()

	def btnCancel(self):
		#print("btnCancel")
		self.close()

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
				item.setFlags(item.flags()|QtCore.Qt.ItemIsUserCheckable)
				item.setCheckState(QtCore.Qt.Checked)	
	
				self.listWidget.addItem(item)

	flagClickR = False
	def on_bttnArrowR(self):
		#print("btnArrowR")
		if self.flagClickR != True:
			self.flagClickR = True
			self.setFixedSize(472,331)
		else:
			self.flagClickR = False
			self.setFixedSize(332,331)

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	pauseModule = QtWidgets.QDialog()
	ui = Ui_pauseModule()
	ui.setupUi(pauseModule)
	pauseModule.show()
	sys.exit(app.exec_())
'''