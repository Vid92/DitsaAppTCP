# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


from formmodule import Ui_FormModule


class Ui_Form(QtWidgets.QWidget):
	#def setupUi(self, Form):
	def __init__(self,parent=None):
		super(Ui_Form, self).__init__()
		self.parent = parent

		self.setObjectName("Form")
		self.resize(1460, 348)
		self.horizontalLayout = QtWidgets.QHBoxLayout(self)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.tableWidget = QtWidgets.QTableWidget(self)
		self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
		self.tableWidget.setRowCount(10)
		self.tableWidget.setColumnCount(10)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.horizontalHeader().setVisible(False)
		#self.tableWidget.horizontalHeader().setHighlightSections(False)
		#self.tableWidget.horizontalHeader().setMinimumSectionSize(20) #141
		self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
		self.tableWidget.verticalHeader().setVisible(False)
		#self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
		#self.tableWidget.verticalHeader().setHighlightSections(True)
		#self.tableWidget.verticalHeader().setMinimumSectionSize(10) #31
		self.tableWidget.verticalHeader().setDefaultSectionSize(51)
		self.horizontalLayout.addWidget(self.tableWidget)

		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

		self.auxMylist = list()

		#self.tableWidget.mousePressEvent = self.mousePressEvent
		#self.tableWidget.mouseReleaseEvent = self.mouseReleaseEvent
		

		self.tableWidget.cellPressed.connect(self.on_cellClickedTableW)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))


	def showEvent(self,event):
		print("showE")
		self.populateColumnRow()
		self.populateCircuit()
		self.populateLabel()

	def populateColumnRow(self):
		print("populateColumnRow")
		z = self.parent.tabWidget.currentIndex() + 1
		if z == 0:
			z = 1

		for i in range(len(self.parent.rowCol)):
			if self.parent.rowCol[i] == str(z)+'%':
				j = self.parent.rowCol

				tmp = j[i+1].split()
				for i in range(2):
					if i == 0:
						y = tmp[0].partition('R=')
						self.zx = int(y[2])
						self.tableWidget.setRowCount(self.zx)
					else:
						y = tmp[1].partition('C=')
						self.zy = int(y[2])
						self.tableWidget.setColumnCount(self.zy)

				for n in range(self.zx):
					for k in range(self.zy):
						item = QtWidgets.QTableWidgetItem()
						item.setFlags(QtCore.Qt.ItemIsEnabled)
						self.tableWidget.setItem(n,k,item)

		#print("TT:",self.parent.rowCol)

	def populateCircuit(self): 
		print("PopulateCircuit")
		for i in range(0,len(self.parent.mylist),4):
			numberTab = self.parent.mylist[i]
			coordCell = self.parent.mylist #i+1 
			#nameCell = self.parent.mylist#[i+2]
			addrCell = self.parent.mylist[i+3]

			z = self.parent.tabWidget.currentIndex() + 1 
			k = numberTab.replace('%','')

			if z == 0:
				z = 1

			#print("z",z)
			#print("k",k)
			if k == str(z):
				nameCell = self.parent.mylist[i+2].split()
				#print("nameCell:",nameCell)
				nameF = nameCell[0].partition('N=')
				tmp = coordCell[i+1].split()
				for i in range(2):
					if i == 0:
						y = tmp[0].partition('X=')
						coordx = y[2]
					else:
						y = tmp[1].partition('Y=')
						coordy = y[2]

				cbText = self.parent.comboBox.currentText()
				form = Ui_FormModule(nameF[2],cbText,self)
				self.tableWidget.setCellWidget(int(coordx),int(coordy),form)

	def populateLabel(self):
		print("PopulateLabel")
		for i in range(0,len(self.parent.mylabel),3):
			numberTabL = self.parent.mylabel[i]
			coordCellL = self.parent.mylabel #[i+1]
			nameCellL = self.parent.mylabel[i+2]

			z = self.parent.tabWidget.currentIndex() + 1 
			k = numberTabL.replace('%','')

			if z == 0:
				z = 1

			#print("z2",z)
			#print("k2",k)
			label = nameCellL.split('#')
			number = label[1].split('$')
			lblt = QtGui.QFont("Arial",int(number[0]), QtGui.QFont.Black)
			item = QtWidgets.QTableWidgetItem(label[0])

			if number[1] == 'AT':
				item.setTextAlignment(QtCore.Qt.AlignTop)
			else:
				item.setTextAlignment(QtCore.Qt.AlignBottom)

			item.setFont(lblt)
			item.setBackground(QtGui.QColor('white'))

			if k == str(z):
				tmpL = coordCellL[i+1].split()
				for i in range(2):
					if i == 0:
						y = tmpL[0].partition('X=')
						coordx = y[2]
					else:
						y = tmpL[1].partition('Y=')
						coordy = y[2]
				item.setFlags(QtCore.Qt.ItemIsEnabled)
				self.tableWidget.setItem(int(coordx),int(coordy),item)

	def contextMenuEvent(self,event):
		print("contextEvent")
		self.popMenu = QtWidgets.QMenu(self)
		startAct = self.popMenu.addAction('Start')
		pauseAct = self.popMenu.addAction('Pause')
		stopAct = self.popMenu.addAction('Stop')

		action = self.popMenu.exec_(self.tableWidget.mapToGlobal(event.pos()))

	def on_cellClickedTableW(self):
		print("ClickTable") #averguar si donde se hizo click esta en list
		vx = self.tableWidget.currentRow()
		vy = self.tableWidget.currentColumn()
		vz = self.parent.tabWidget.currentIndex() + 1

		coord = 'X='+str(vx)+' Y='+str(vy)
		tab = str(vz)+'%'
		#print("coord:",coord)
		#for i in self.tableWidget.cellActivated(vx,vy):
		#	print("entro select")

		for i in range(0,len(self.parent.mylist),4):
			numberTab = self.parent.mylist[i]
			coordCell = self.parent.mylist[i+1] 
			#nameCell = self.parent.mylist#[i+2]
			##addrCell = self.parent.mylist[i+3]

			z = self.parent.tabWidget.currentIndex() + 1 
			
			if tab == numberTab:
				print("tab0:",tab)
				if coord == coordCell:
					print("coordC:",coordCell)
					##numberTab = self.parent.mylist[i]
					##coordCell = self.parent.mylist #i+1 
					#nameCell = self.parent.mylist#[i+2]
					##addrCell = self.parent.mylist[i+3]

					##z = self.parent.tabWidget.currentIndex() + 1 
					k = numberTab.replace('%','')

					if z == 0:
						z = 1

					#print("z",z)
					#print("k",k)
					if k == str(z):
						nameCell = self.parent.mylist[i+2].split()
						#print("nameCell:",nameCell)
						nameF = nameCell[0].partition('N=')
						tmp = self.parent.mylist[i+1].split()
						for i in range(2):
							if i == 0:
								y = tmp[0].partition('X=')
								coordx = y[2]
							else:
								y = tmp[1].partition('Y=')
								coordy = y[2]

						cbText = self.parent.comboBox.currentText()
						form = Ui_FormModule(nameF[2],cbText,self)
						form.changeModule()
						form.selectionLabel()
						self.tableWidget.setCellWidget(int(coordx),int(coordy),form)
						

	def totalMylist(self):
		self.auxMylist = self.parent.mylist[:]

'''
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	#ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
'''