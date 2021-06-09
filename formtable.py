# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formtable.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import csv
from os import scandir

class Ui_FormTable(object):
	def setupUi(self, FormTable):
	#def __init__(self,parent=None):
	#	super(Ui_FormTable, self).__init__()
	#	self.parent = parent
		FormTable.setObjectName("FormTable")
		FormTable.setFixedSize(1330, 820)
		self.treeWidget = QtWidgets.QTreeWidget(FormTable)
		self.treeWidget.setGeometry(QtCore.QRect(9, 9, 131, 791))
		self.treeWidget.setObjectName("treeWidget")
		self.treeWidget.headerItem().setText(0, "1")
		self.treeWidget.setHeaderLabel("Report")
		self.treeWidget.header().setDefaultAlignment(QtCore.Qt.AlignCenter)

		self.tableWidget = QtWidgets.QTableWidget(FormTable)
		self.tableWidget.setGeometry(QtCore.QRect(150, 10, 1070, 791))  #381 , 271
		self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
		self.tableWidget.setColumnCount(12)
		self.tableWidget.setAlternatingRowColors(True)
		self.tableWidget.setObjectName("tableWidget")

		self.retranslateUi(FormTable)
		QtCore.QMetaObject.connectSlotsByName(FormTable)

		FormTable.showEvent = self.showEvent

		self.flagshow = False
		self.treeWidget.itemClicked.connect(self.ontreeClick)

		self.FormTable = FormTable

	def retranslateUi(self, FormTable):
		_translate = QtCore.QCoreApplication.translate
		FormTable.setWindowTitle(_translate("FormTable", "Reports"))#+self.reportName))
		self.tableWidget.setColumnWidth(0,150)
		self.tableWidget.setColumnWidth(3,90)
		self.tableWidget.setColumnWidth(4,90)
		self.tableWidget.setColumnWidth(9,90)

	def showEvent(self,event):
		print("showFormtable")
		if self.flagshow != True:
			self.flagshow = True
			self.nameFile() #agrega todos los reportes al treewidget
			itemTree = self.treeWidget.topLevelItem(0)
			itemTree.setSelected(True)
			self.treeWidget.setCurrentItem(itemTree,0)
			self.ontreeClick()

	def ontreeClick(self):
		x = self.treeWidget.currentItem().text(0)
		with open('/home/ditsa/DitsaNet/FormationDataFiles/'+x+'.xls') as csvarchivo:
			entrada = csv.reader(csvarchivo)
			i = 0
			for reg in entrada:
				i+=1
				self.tableWidget.setRowCount(i+1)
				for j in range(12):
					lblt = QtGui.QFont("Arial",10, QtGui.QFont.Normal)
					item = QtWidgets.QTableWidgetItem(reg[j])
					item.setTextAlignment(QtCore.Qt.AlignCenter)
					item.setFont(lblt)
					item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
					self.tableWidget.setItem(i-1,j,item)
		
	def nameFile(self):			
		files=self.ls1("/home/ditsa/DitsaNet/FormationDataFiles/")
		for file in files:
			self.treeWidget.topLevelItemCount() + 1
			nf = file.replace('.xls','')
			topLevel = QtWidgets.QTreeWidgetItem()
			topLevel.setText(0,nf)
			self.treeWidget.addTopLevelItem(topLevel)


	def ls1(self,path): 
		return [obj.name for obj in scandir(path) if obj.is_file()]


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	FormTable = QtWidgets.QWidget()
	ui = Ui_FormTable()
	ui.setupUi(FormTable)
	FormTable.show()
	sys.exit(app.exec_())
