# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from windowch import Ui_WindowCh

from datalistenermemory import DataListenerMemory
#from demo import Thread
from devicemainboard import BCmb
import shared
import time
import threading
import appsettings 
from appsettings import useHostname
from datetime import timedelta

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1536, 823)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
		self.tabWidget.setGeometry(QtCore.QRect(20, 80, 1451, 691))
		self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
		self.tabWidget.setTabsClosable(False)
		self.tabWidget.setObjectName("tabWidget")
		self.tbPage1 = QtWidgets.QWidget()
		self.tbPage1.setObjectName("tbPage1")
		self.lblPage1 = QtWidgets.QLabel(self.tbPage1)
		self.lblPage1.setGeometry(QtCore.QRect(40, 30, 631, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.lblPage1.setFont(font)
		self.lblPage1.setObjectName("lblPage1")
		self.lblName1_1 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_1.setGeometry(QtCore.QRect(90, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_1.setFont(font)
		self.lblName1_1.setObjectName("lblName1_1")
		self.pbProgram1_1 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_1.setGeometry(QtCore.QRect(90, 170, 141, 31))
		self.pbProgram1_1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_1.setProperty("value", 24)
		self.pbProgram1_1.setObjectName("pbProgram1_1")
		self.cmdDisplay1_1 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_1.setGeometry(QtCore.QRect(90, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_1.setFont(font)
		self.cmdDisplay1_1.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_1.setFlat(True)
		self.cmdDisplay1_1.setObjectName("cmdDisplay1_1")
		self.chkSel1_1 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_1.setGeometry(QtCore.QRect(70, 120, 86, 20))
		self.chkSel1_1.setText("")
		self.chkSel1_1.setObjectName("chkSel1_1")
		self.chkSel1_2 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_2.setGeometry(QtCore.QRect(260, 120, 86, 20))
		self.chkSel1_2.setText("")
		self.chkSel1_2.setObjectName("chkSel1_2")
		self.lblName1_2 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_2.setGeometry(QtCore.QRect(280, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_2.setFont(font)
		self.lblName1_2.setObjectName("lblName1_2")
		self.cmdDisplay1_2 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_2.setGeometry(QtCore.QRect(280, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_2.setFont(font)
		self.cmdDisplay1_2.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_2.setFlat(True)
		self.cmdDisplay1_2.setObjectName("cmdDisplay1_2")
		self.pbProgram1_2 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_2.setGeometry(QtCore.QRect(280, 170, 141, 31))
		self.pbProgram1_2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_2.setProperty("value", 24)
		self.pbProgram1_2.setObjectName("pbProgram1_2")
		self.chkSel1_3 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_3.setGeometry(QtCore.QRect(450, 120, 86, 20))
		self.chkSel1_3.setText("")
		self.chkSel1_3.setObjectName("chkSel1_3")
		self.lblName1_3 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_3.setGeometry(QtCore.QRect(470, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_3.setFont(font)
		self.lblName1_3.setObjectName("lblName1_3")
		self.cmdDisplay1_3 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_3.setGeometry(QtCore.QRect(470, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_3.setFont(font)
		self.cmdDisplay1_3.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_3.setFlat(True)
		self.cmdDisplay1_3.setObjectName("cmdDisplay1_3")
		self.pbProgram1_3 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
		self.pbProgram1_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_3.setProperty("value", 24)
		self.pbProgram1_3.setObjectName("pbProgram1_3")
		self.chkSel1_4 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_4.setGeometry(QtCore.QRect(640, 120, 86, 20))
		self.chkSel1_4.setText("")
		self.chkSel1_4.setObjectName("chkSel1_4")
		self.lblName1_4 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_4.setGeometry(QtCore.QRect(660, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_4.setFont(font)
		self.lblName1_4.setObjectName("lblName1_4")
		self.cmdDisplay1_4 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_4.setGeometry(QtCore.QRect(660, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_4.setFont(font)
		self.cmdDisplay1_4.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_4.setFlat(True)
		self.cmdDisplay1_4.setObjectName("cmdDisplay1_4")
		self.pbProgram1_4 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_4.setGeometry(QtCore.QRect(660, 170, 141, 31))
		self.pbProgram1_4.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_4.setProperty("value", 24)
		self.pbProgram1_4.setObjectName("pbProgram1_4")
		self.chkSel1_5 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_5.setGeometry(QtCore.QRect(830, 120, 86, 20))
		self.chkSel1_5.setText("")
		self.chkSel1_5.setObjectName("chkSel1_5")
		self.lblName1_5 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_5.setGeometry(QtCore.QRect(850, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_5.setFont(font)
		self.lblName1_5.setObjectName("lblName1_5")
		self.cmdDisplay1_5 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_5.setGeometry(QtCore.QRect(850, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_5.setFont(font)
		self.cmdDisplay1_5.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_5.setFlat(True)
		self.cmdDisplay1_5.setObjectName("cmdDisplay1_5")
		self.pbProgram1_5 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_5.setGeometry(QtCore.QRect(850, 170, 141, 31))
		self.pbProgram1_5.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_5.setProperty("value", 24)
		self.pbProgram1_5.setObjectName("pbProgram1_5")
		self.chkSel1_6 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_6.setGeometry(QtCore.QRect(1020, 120, 86, 20))
		self.chkSel1_6.setText("")
		self.chkSel1_6.setObjectName("chkSel1_6")
		self.lblName1_6 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_6.setGeometry(QtCore.QRect(1040, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_6.setFont(font)
		self.lblName1_6.setObjectName("lblName1_6")
		self.cmdDisplay1_6 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_6.setGeometry(QtCore.QRect(1040, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_6.setFont(font)
		self.cmdDisplay1_6.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_6.setFlat(True)
		self.cmdDisplay1_6.setObjectName("cmdDisplay1_6")
		self.pbProgram1_6 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_6.setGeometry(QtCore.QRect(1040, 170, 141, 31))
		self.pbProgram1_6.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_6.setProperty("value", 24)
		self.pbProgram1_6.setObjectName("pbProgram1_6")
		self.chkSel1_7 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_7.setGeometry(QtCore.QRect(1210, 120, 86, 20))
		self.chkSel1_7.setText("")
		self.chkSel1_7.setObjectName("chkSel1_7")
		self.lblName1_7 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_7.setGeometry(QtCore.QRect(1230, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_7.setFont(font)
		self.lblName1_7.setObjectName("lblName1_7")
		self.cmdDisplay1_7 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_7.setGeometry(QtCore.QRect(1230, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_7.setFont(font)
		self.cmdDisplay1_7.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_7.setFlat(True)
		self.cmdDisplay1_7.setObjectName("cmdDisplay1_7")
		self.pbProgram1_7 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_7.setGeometry(QtCore.QRect(1230, 170, 141, 31))
		self.pbProgram1_7.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_7.setProperty("value", 24)
		self.pbProgram1_7.setObjectName("pbProgram1_7")
		self.chkSel1_8 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_8.setGeometry(QtCore.QRect(70, 250, 86, 20))
		self.chkSel1_8.setText("")
		self.chkSel1_8.setObjectName("chkSel1_8")
		self.lblName1_8 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_8.setGeometry(QtCore.QRect(90, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_8.setFont(font)
		self.lblName1_8.setObjectName("lblName1_8")
		self.cmdDisplay1_8 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_8.setGeometry(QtCore.QRect(90, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_8.setFont(font)
		self.cmdDisplay1_8.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_8.setFlat(True)
		self.cmdDisplay1_8.setObjectName("cmdDisplay1_8")
		self.pbProgram1_8 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_8.setGeometry(QtCore.QRect(90, 300, 141, 31))
		self.pbProgram1_8.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_8.setProperty("value", 24)
		self.pbProgram1_8.setObjectName("pbProgram1_8")
		self.chkSel1_9 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_9.setGeometry(QtCore.QRect(260, 250, 86, 20))
		self.chkSel1_9.setText("")
		self.chkSel1_9.setObjectName("chkSel1_9")
		self.lblName1_9 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_9.setGeometry(QtCore.QRect(280, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_9.setFont(font)
		self.lblName1_9.setObjectName("lblName1_9")
		self.cmdDisplay1_9 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_9.setGeometry(QtCore.QRect(280, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_9.setFont(font)
		self.cmdDisplay1_9.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_9.setFlat(True)
		self.cmdDisplay1_9.setObjectName("cmdDisplay1_9")
		self.pbProgram1_9 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_9.setGeometry(QtCore.QRect(280, 300, 141, 31))
		self.pbProgram1_9.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_9.setProperty("value", 24)
		self.pbProgram1_9.setObjectName("pbProgram1_9")
		self.chkSel1_10 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_10.setGeometry(QtCore.QRect(450, 250, 86, 20))
		self.chkSel1_10.setText("")
		self.chkSel1_10.setObjectName("chkSel1_10")
		self.lblName1_10 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_10.setGeometry(QtCore.QRect(470, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_10.setFont(font)
		self.lblName1_10.setObjectName("lblName1_10")
		self.cmdDisplay1_10 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_10.setGeometry(QtCore.QRect(470, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_10.setFont(font)
		self.cmdDisplay1_10.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_10.setFlat(True)
		self.cmdDisplay1_10.setObjectName("cmdDisplay1_10")
		self.pbProgram1_10 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_10.setGeometry(QtCore.QRect(470, 300, 141, 31))
		self.pbProgram1_10.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_10.setProperty("value", 24)
		self.pbProgram1_10.setObjectName("pbProgram1_10")
		self.chkSel1_11 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_11.setGeometry(QtCore.QRect(640, 250, 86, 20))
		self.chkSel1_11.setText("")
		self.chkSel1_11.setObjectName("chkSel1_11")
		self.lblName1_11 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_11.setGeometry(QtCore.QRect(660, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_11.setFont(font)
		self.lblName1_11.setObjectName("lblName1_11")
		self.cmdDisplay1_11 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_11.setGeometry(QtCore.QRect(660, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_11.setFont(font)
		self.cmdDisplay1_11.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_11.setFlat(True)
		self.cmdDisplay1_11.setObjectName("cmdDisplay1_11")
		self.pbProgram1_11 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_11.setGeometry(QtCore.QRect(660, 300, 141, 31))
		self.pbProgram1_11.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_11.setProperty("value", 24)
		self.pbProgram1_11.setObjectName("pbProgram1_11")
		self.chkSel1_12 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_12.setGeometry(QtCore.QRect(830, 250, 86, 20))
		self.chkSel1_12.setText("")
		self.chkSel1_12.setObjectName("chkSel1_12")
		self.lblName1_12 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_12.setGeometry(QtCore.QRect(850, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_12.setFont(font)
		self.lblName1_12.setObjectName("lblName1_12")
		self.cmdDisplay1_12 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_12.setGeometry(QtCore.QRect(850, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_12.setFont(font)
		self.cmdDisplay1_12.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_12.setFlat(True)
		self.cmdDisplay1_12.setObjectName("cmdDisplay1_12")
		self.pbProgram1_12 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_12.setGeometry(QtCore.QRect(850, 300, 141, 31))
		self.pbProgram1_12.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_12.setProperty("value", 24)
		self.pbProgram1_12.setObjectName("pbProgram1_12")
		self.chkSel1_13 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_13.setGeometry(QtCore.QRect(1020, 250, 86, 20))
		self.chkSel1_13.setText("")
		self.chkSel1_13.setObjectName("chkSel1_13")
		self.lblName1_13 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_13.setGeometry(QtCore.QRect(1040, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_13.setFont(font)
		self.lblName1_13.setObjectName("lblName1_13")
		self.cmdDisplay1_13 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_13.setGeometry(QtCore.QRect(1040, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_13.setFont(font)
		self.cmdDisplay1_13.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_13.setFlat(True)
		self.cmdDisplay1_13.setObjectName("cmdDisplay1_13")
		self.pbProgram1_13 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_13.setGeometry(QtCore.QRect(1040, 300, 141, 31))
		self.pbProgram1_13.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_13.setProperty("value", 24)
		self.pbProgram1_13.setObjectName("pbProgram1_13")
		self.chkSel1_14 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_14.setGeometry(QtCore.QRect(1210, 250, 86, 20))
		self.chkSel1_14.setText("")
		self.chkSel1_14.setObjectName("chkSel1_14")
		self.lblName1_14 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_14.setGeometry(QtCore.QRect(1230, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_14.setFont(font)
		self.lblName1_14.setObjectName("lblName1_14")
		self.cmdDisplay1_14 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_14.setGeometry(QtCore.QRect(1230, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_14.setFont(font)
		self.cmdDisplay1_14.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_14.setFlat(True)
		self.cmdDisplay1_14.setObjectName("cmdDisplay1_14")
		self.pbProgram1_14 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_14.setGeometry(QtCore.QRect(1230, 300, 141, 31))
		self.pbProgram1_14.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_14.setProperty("value", 24)
		self.pbProgram1_14.setObjectName("pbProgram1_14")
		self.chkSel1_15 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_15.setGeometry(QtCore.QRect(70, 380, 86, 20))
		self.chkSel1_15.setText("")
		self.chkSel1_15.setObjectName("chkSel1_15")
		self.lblName1_15 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_15.setGeometry(QtCore.QRect(90, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_15.setFont(font)
		self.lblName1_15.setObjectName("lblName1_15")
		self.cmdDisplay1_15 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_15.setGeometry(QtCore.QRect(90, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_15.setFont(font)
		self.cmdDisplay1_15.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_15.setFlat(True)
		self.cmdDisplay1_15.setObjectName("cmdDisplay1_15")
		self.pbProgram1_15 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_15.setGeometry(QtCore.QRect(90, 430, 141, 31))
		self.pbProgram1_15.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_15.setProperty("value", 24)
		self.pbProgram1_15.setObjectName("pbProgram1_15")
		self.chkSel1_16 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_16.setGeometry(QtCore.QRect(260, 380, 86, 20))
		self.chkSel1_16.setText("")
		self.chkSel1_16.setObjectName("chkSel1_16")
		self.lblName1_16 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_16.setGeometry(QtCore.QRect(280, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_16.setFont(font)
		self.lblName1_16.setObjectName("lblName1_16")
		self.cmdDisplay1_16 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_16.setGeometry(QtCore.QRect(280, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_16.setFont(font)
		self.cmdDisplay1_16.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_16.setFlat(True)
		self.cmdDisplay1_16.setObjectName("cmdDisplay1_16")
		self.pbProgram1_16 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_16.setGeometry(QtCore.QRect(280, 430, 141, 31))
		self.pbProgram1_16.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_16.setProperty("value", 24)
		self.pbProgram1_16.setObjectName("pbProgram1_16")
		self.chkSel1_17 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_17.setGeometry(QtCore.QRect(450, 380, 86, 20))
		self.chkSel1_17.setText("")
		self.chkSel1_17.setObjectName("chkSel1_17")
		self.lblName1_17 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_17.setGeometry(QtCore.QRect(470, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_17.setFont(font)
		self.lblName1_17.setObjectName("lblName1_17")
		self.cmdDisplay1_17 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_17.setGeometry(QtCore.QRect(470, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_17.setFont(font)
		self.cmdDisplay1_17.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_17.setFlat(True)
		self.cmdDisplay1_17.setObjectName("cmdDisplay1_17")
		self.pbProgram1_17 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_17.setGeometry(QtCore.QRect(470, 430, 141, 31))
		self.pbProgram1_17.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_17.setProperty("value", 24)
		self.pbProgram1_17.setObjectName("pbProgram1_17")
		self.chkSel1_18 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_18.setGeometry(QtCore.QRect(640, 380, 86, 20))
		self.chkSel1_18.setText("")
		self.chkSel1_18.setObjectName("chkSel1_18")
		self.lblName1_18 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_18.setGeometry(QtCore.QRect(660, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_18.setFont(font)
		self.lblName1_18.setObjectName("lblName1_18")
		self.cmdDisplay1_18 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_18.setGeometry(QtCore.QRect(660, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_18.setFont(font)
		self.cmdDisplay1_18.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_18.setFlat(True)
		self.cmdDisplay1_18.setObjectName("cmdDisplay1_18")
		self.pbProgram1_18 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_18.setGeometry(QtCore.QRect(660, 430, 141, 31))
		self.pbProgram1_18.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_18.setProperty("value", 24)
		self.pbProgram1_18.setObjectName("pbProgram1_18")
		self.chkSel1_19 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_19.setGeometry(QtCore.QRect(830, 380, 86, 20))
		self.chkSel1_19.setText("")
		self.chkSel1_19.setObjectName("chkSel1_19")
		self.lblName1_19 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_19.setGeometry(QtCore.QRect(850, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_19.setFont(font)
		self.lblName1_19.setObjectName("lblName1_19")
		self.cmdDisplay1_19 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_19.setGeometry(QtCore.QRect(850, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_19.setFont(font)
		self.cmdDisplay1_19.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_19.setFlat(True)
		self.cmdDisplay1_19.setObjectName("cmdDisplay1_19")
		self.pbProgram1_19 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_19.setGeometry(QtCore.QRect(850, 430, 141, 31))
		self.pbProgram1_19.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_19.setProperty("value", 24)
		self.pbProgram1_19.setObjectName("pbProgram1_19")
		self.chkSel1_20 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_20.setGeometry(QtCore.QRect(1020, 380, 86, 20))
		self.chkSel1_20.setText("")
		self.chkSel1_20.setObjectName("chkSel1_20")
		self.lblName1_20 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_20.setGeometry(QtCore.QRect(1040, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_20.setFont(font)
		self.lblName1_20.setObjectName("lblName1_20")
		self.cmdDisplay1_20 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_20.setGeometry(QtCore.QRect(1040, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_20.setFont(font)
		self.cmdDisplay1_20.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_20.setFlat(True)
		self.cmdDisplay1_20.setObjectName("cmdDisplay1_20")
		self.pbProgram1_20 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_20.setGeometry(QtCore.QRect(1040, 430, 141, 31))
		self.pbProgram1_20.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_20.setProperty("value", 24)
		self.pbProgram1_20.setObjectName("pbProgram1_20")
		self.chkSel1_21 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_21.setGeometry(QtCore.QRect(1210, 380, 86, 20))
		self.chkSel1_21.setText("")
		self.chkSel1_21.setObjectName("chkSel1_21")
		self.lblName1_21 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_21.setGeometry(QtCore.QRect(1230, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_21.setFont(font)
		self.lblName1_21.setObjectName("lblName1_21")
		self.cmdDisplay1_21 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_21.setGeometry(QtCore.QRect(1230, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_21.setFont(font)
		self.cmdDisplay1_21.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_21.setFlat(True)
		self.cmdDisplay1_21.setObjectName("cmdDisplay1_21")
		self.pbProgram1_21 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_21.setGeometry(QtCore.QRect(1230, 430, 141, 31))
		self.pbProgram1_21.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_21.setProperty("value", 24)
		self.pbProgram1_21.setObjectName("pbProgram1_21")
		self.chkSel1_22 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_22.setGeometry(QtCore.QRect(70, 510, 86, 20))
		self.chkSel1_22.setText("")
		self.chkSel1_22.setObjectName("chkSel1_22")
		self.lblName1_22 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_22.setGeometry(QtCore.QRect(90, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_22.setFont(font)
		self.lblName1_22.setObjectName("lblName1_22")
		self.cmdDisplay1_22 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_22.setGeometry(QtCore.QRect(90, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_22.setFont(font)
		self.cmdDisplay1_22.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_22.setFlat(True)
		self.cmdDisplay1_22.setObjectName("cmdDisplay1_22")
		self.pbProgram1_22 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_22.setGeometry(QtCore.QRect(90, 560, 141, 31))
		self.pbProgram1_22.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_22.setProperty("value", 24)
		self.pbProgram1_22.setObjectName("pbProgram1_22")
		self.chkSel1_23 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_23.setGeometry(QtCore.QRect(260, 510, 86, 20))
		self.chkSel1_23.setText("")
		self.chkSel1_23.setObjectName("chkSel1_23")
		self.lblName1_23 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_23.setGeometry(QtCore.QRect(280, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_23.setFont(font)
		self.lblName1_23.setObjectName("lblName1_23")
		self.cmdDisplay1_23 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_23.setGeometry(QtCore.QRect(280, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_23.setFont(font)
		self.cmdDisplay1_23.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_23.setFlat(True)
		self.cmdDisplay1_23.setObjectName("cmdDisplay1_23")
		self.pbProgram1_23 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_23.setGeometry(QtCore.QRect(280, 560, 141, 31))
		self.pbProgram1_23.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_23.setProperty("value", 24)
		self.pbProgram1_23.setObjectName("pbProgram1_23")
		self.chkSel1_24 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_24.setGeometry(QtCore.QRect(450, 510, 86, 20))
		self.chkSel1_24.setText("")
		self.chkSel1_24.setObjectName("chkSel1_24")
		self.lblName1_24 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_24.setGeometry(QtCore.QRect(470, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_24.setFont(font)
		self.lblName1_24.setObjectName("lblName1_24")
		self.cmdDisplay1_24 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_24.setGeometry(QtCore.QRect(470, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_24.setFont(font)
		self.cmdDisplay1_24.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_24.setFlat(True)
		self.cmdDisplay1_24.setObjectName("cmdDisplay1_24")
		self.pbProgram1_24 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_24.setGeometry(QtCore.QRect(470, 560, 141, 31))
		self.pbProgram1_24.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_24.setProperty("value", 24)
		self.pbProgram1_24.setObjectName("pbProgram1_24")
		self.chkSel1_25 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_25.setGeometry(QtCore.QRect(640, 510, 86, 20))
		self.chkSel1_25.setText("")
		self.chkSel1_25.setObjectName("chkSel1_25")
		self.lblName1_25 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_25.setGeometry(QtCore.QRect(660, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_25.setFont(font)
		self.lblName1_25.setObjectName("lblName1_25")
		self.cmdDisplay1_25 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_25.setGeometry(QtCore.QRect(660, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_25.setFont(font)
		self.cmdDisplay1_25.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_25.setFlat(True)
		self.cmdDisplay1_25.setObjectName("cmdDisplay1_25")
		self.pbProgram1_25 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_25.setGeometry(QtCore.QRect(660, 560, 141, 31))
		self.pbProgram1_25.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_25.setProperty("value", 24)
		self.pbProgram1_25.setObjectName("pbProgram1_25")
		self.chkSel1_26 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_26.setGeometry(QtCore.QRect(830, 510, 86, 20))
		self.chkSel1_26.setText("")
		self.chkSel1_26.setObjectName("chkSel1_26")
		self.lblName1_26 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_26.setGeometry(QtCore.QRect(850, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_26.setFont(font)
		self.lblName1_26.setObjectName("lblName1_26")
		self.cmdDisplay1_26 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_26.setGeometry(QtCore.QRect(850, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_26.setFont(font)
		self.cmdDisplay1_26.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_26.setFlat(True)
		self.cmdDisplay1_26.setObjectName("cmdDisplay1_26")
		self.pbProgram1_26 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_26.setGeometry(QtCore.QRect(850, 560, 141, 31))
		self.pbProgram1_26.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_26.setProperty("value", 24)
		self.pbProgram1_26.setObjectName("pbProgram1_26")
		self.chkSel1_27 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_27.setGeometry(QtCore.QRect(1020, 510, 86, 20))
		self.chkSel1_27.setText("")
		self.chkSel1_27.setObjectName("chkSel1_27")
		self.lblName1_27 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_27.setGeometry(QtCore.QRect(1040, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_27.setFont(font)
		self.lblName1_27.setObjectName("lblName1_27")
		self.cmdDisplay1_27 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_27.setGeometry(QtCore.QRect(1040, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_27.setFont(font)
		self.cmdDisplay1_27.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_27.setFlat(True)
		self.cmdDisplay1_27.setObjectName("cmdDisplay1_27")
		self.pbProgram1_27 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_27.setGeometry(QtCore.QRect(1040, 560, 141, 31))
		self.pbProgram1_27.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_27.setProperty("value", 24)
		self.pbProgram1_27.setObjectName("pbProgram1_27")
		self.chkSel1_28 = QtWidgets.QCheckBox(self.tbPage1)
		self.chkSel1_28.setGeometry(QtCore.QRect(1210, 510, 86, 20))
		self.chkSel1_28.setText("")
		self.chkSel1_28.setObjectName("chkSel1_28")
		self.lblName1_28 = QtWidgets.QLabel(self.tbPage1)
		self.lblName1_28.setGeometry(QtCore.QRect(1230, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName1_28.setFont(font)
		self.lblName1_28.setObjectName("lblName1_28")
		self.cmdDisplay1_28 = QtWidgets.QPushButton(self.tbPage1)
		self.cmdDisplay1_28.setGeometry(QtCore.QRect(1230, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay1_28.setFont(font)
		self.cmdDisplay1_28.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay1_28.setFlat(True)
		self.cmdDisplay1_28.setObjectName("cmdDisplay1_28")
		self.pbProgram1_28 = QtWidgets.QProgressBar(self.tbPage1)
		self.pbProgram1_28.setGeometry(QtCore.QRect(1230, 560, 141, 31))
		self.pbProgram1_28.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram1_28.setProperty("value", 24)
		self.pbProgram1_28.setObjectName("pbProgram1_28")
		self.tabWidget.addTab(self.tbPage1, "")
		self.tbPage2 = QtWidgets.QWidget()
		self.tbPage2.setObjectName("tbPage2")
		self.lblPage2 = QtWidgets.QLabel(self.tbPage2)
		self.lblPage2.setGeometry(QtCore.QRect(40, 30, 671, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.lblPage2.setFont(font)
		self.lblPage2.setObjectName("lblPage2")
		self.chkSel2_1 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_1.setGeometry(QtCore.QRect(70, 120, 86, 20))
		self.chkSel2_1.setText("")
		self.chkSel2_1.setObjectName("chkSel2_1")
		self.lblName2_1 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_1.setGeometry(QtCore.QRect(90, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_1.setFont(font)
		self.lblName2_1.setObjectName("lblName2_1")
		self.cmdDisplay2_1 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_1.setGeometry(QtCore.QRect(90, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_1.setFont(font)
		self.cmdDisplay2_1.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_1.setFlat(True)
		self.cmdDisplay2_1.setObjectName("cmdDisplay2_1")
		self.pbProgram2_1 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_1.setGeometry(QtCore.QRect(90, 170, 141, 31))
		self.pbProgram2_1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_1.setProperty("value", 24)
		self.pbProgram2_1.setObjectName("pbProgram2_1")
		self.chkSel2_2 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_2.setGeometry(QtCore.QRect(260, 120, 86, 20))
		self.chkSel2_2.setText("")
		self.chkSel2_2.setObjectName("chkSel2_2")
		self.lblName2_2 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_2.setGeometry(QtCore.QRect(280, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_2.setFont(font)
		self.lblName2_2.setObjectName("lblName2_2")
		self.cmdDisplay2_2 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_2.setGeometry(QtCore.QRect(280, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_2.setFont(font)
		self.cmdDisplay2_2.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_2.setFlat(True)
		self.cmdDisplay2_2.setObjectName("cmdDisplay2_2")
		self.pbProgram2_2 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_2.setGeometry(QtCore.QRect(280, 170, 141, 31))
		self.pbProgram2_2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_2.setProperty("value", 24)
		self.pbProgram2_2.setObjectName("pbProgram2_2")
		self.lblName2_3 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_3.setGeometry(QtCore.QRect(470, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_3.setFont(font)
		self.lblName2_3.setObjectName("lblName2_3")
		self.pbProgram2_3 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
		self.pbProgram2_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_3.setProperty("value", 24)
		self.pbProgram2_3.setObjectName("pbProgram2_3")
		self.cmdDisplay2_3 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_3.setGeometry(QtCore.QRect(470, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_3.setFont(font)
		self.cmdDisplay2_3.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_3.setFlat(True)
		self.cmdDisplay2_3.setObjectName("cmdDisplay2_3")
		self.chkSel2_3 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_3.setGeometry(QtCore.QRect(450, 120, 86, 20))
		self.chkSel2_3.setText("")
		self.chkSel2_3.setObjectName("chkSel2_3")
		self.lblName2_4 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_4.setGeometry(QtCore.QRect(660, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_4.setFont(font)
		self.lblName2_4.setObjectName("lblName2_4")
		self.pbProgram2_4 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_4.setGeometry(QtCore.QRect(660, 170, 141, 31))
		self.pbProgram2_4.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_4.setProperty("value", 24)
		self.pbProgram2_4.setObjectName("pbProgram2_4")
		self.cmdDisplay2_4 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_4.setGeometry(QtCore.QRect(660, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_4.setFont(font)
		self.cmdDisplay2_4.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_4.setFlat(True)
		self.cmdDisplay2_4.setObjectName("cmdDisplay2_4")
		self.chkSel2_4 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_4.setGeometry(QtCore.QRect(640, 120, 86, 20))
		self.chkSel2_4.setText("")
		self.chkSel2_4.setObjectName("chkSel2_4")
		self.cmdDisplay2_5 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_5.setGeometry(QtCore.QRect(850, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_5.setFont(font)
		self.cmdDisplay2_5.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_5.setFlat(True)
		self.cmdDisplay2_5.setObjectName("cmdDisplay2_5")
		self.lblName2_5 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_5.setGeometry(QtCore.QRect(850, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_5.setFont(font)
		self.lblName2_5.setObjectName("lblName2_5")
		self.pbProgram2_5 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_5.setGeometry(QtCore.QRect(850, 170, 141, 31))
		self.pbProgram2_5.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_5.setProperty("value", 24)
		self.pbProgram2_5.setObjectName("pbProgram2_5")
		self.chkSel2_5 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_5.setGeometry(QtCore.QRect(830, 120, 86, 20))
		self.chkSel2_5.setText("")
		self.chkSel2_5.setObjectName("chkSel2_5")
		self.cmdDisplay2_6 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_6.setGeometry(QtCore.QRect(1040, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_6.setFont(font)
		self.cmdDisplay2_6.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_6.setFlat(True)
		self.cmdDisplay2_6.setObjectName("cmdDisplay2_6")
		self.lblName2_6 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_6.setGeometry(QtCore.QRect(1040, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_6.setFont(font)
		self.lblName2_6.setObjectName("lblName2_6")
		self.pbProgram2_6 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_6.setGeometry(QtCore.QRect(1040, 170, 141, 31))
		self.pbProgram2_6.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_6.setProperty("value", 24)
		self.pbProgram2_6.setObjectName("pbProgram2_6")
		self.chkSel2_6 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_6.setGeometry(QtCore.QRect(1020, 120, 86, 20))
		self.chkSel2_6.setText("")
		self.chkSel2_6.setObjectName("chkSel2_6")
		self.cmdDisplay2_7 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_7.setGeometry(QtCore.QRect(1230, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_7.setFont(font)
		self.cmdDisplay2_7.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_7.setFlat(True)
		self.cmdDisplay2_7.setObjectName("cmdDisplay2_7")
		self.lblName2_7 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_7.setGeometry(QtCore.QRect(1230, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_7.setFont(font)
		self.lblName2_7.setObjectName("lblName2_7")
		self.pbProgram2_7 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_7.setGeometry(QtCore.QRect(1230, 170, 141, 31))
		self.pbProgram2_7.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_7.setProperty("value", 24)
		self.pbProgram2_7.setObjectName("pbProgram2_7")
		self.chkSel2_7 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_7.setGeometry(QtCore.QRect(1210, 120, 86, 20))
		self.chkSel2_7.setText("")
		self.chkSel2_7.setObjectName("chkSel2_7")
		self.cmdDisplay2_8 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_8.setGeometry(QtCore.QRect(90, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_8.setFont(font)
		self.cmdDisplay2_8.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_8.setFlat(True)
		self.cmdDisplay2_8.setObjectName("cmdDisplay2_8")
		self.lblName2_8 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_8.setGeometry(QtCore.QRect(90, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_8.setFont(font)
		self.lblName2_8.setObjectName("lblName2_8")
		self.pbProgram2_8 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_8.setGeometry(QtCore.QRect(90, 300, 141, 31))
		self.pbProgram2_8.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_8.setProperty("value", 24)
		self.pbProgram2_8.setObjectName("pbProgram2_8")
		self.chkSel2_8 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_8.setGeometry(QtCore.QRect(70, 250, 86, 20))
		self.chkSel2_8.setText("")
		self.chkSel2_8.setObjectName("chkSel2_8")
		self.cmdDisplay2_9 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_9.setGeometry(QtCore.QRect(280, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_9.setFont(font)
		self.cmdDisplay2_9.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_9.setFlat(True)
		self.cmdDisplay2_9.setObjectName("cmdDisplay2_9")
		self.lblName2_9 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_9.setGeometry(QtCore.QRect(280, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_9.setFont(font)
		self.lblName2_9.setObjectName("lblName2_9")
		self.pbProgram2_9 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_9.setGeometry(QtCore.QRect(280, 300, 141, 31))
		self.pbProgram2_9.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_9.setProperty("value", 24)
		self.pbProgram2_9.setObjectName("pbProgram2_9")
		self.chkSel2_9 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_9.setGeometry(QtCore.QRect(260, 250, 86, 20))
		self.chkSel2_9.setText("")
		self.chkSel2_9.setObjectName("chkSel2_9")
		self.cmdDisplay2_10 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_10.setGeometry(QtCore.QRect(470, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_10.setFont(font)
		self.cmdDisplay2_10.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_10.setFlat(True)
		self.cmdDisplay2_10.setObjectName("cmdDisplay2_10")
		self.lblName2_10 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_10.setGeometry(QtCore.QRect(470, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_10.setFont(font)
		self.lblName2_10.setObjectName("lblName2_10")
		self.pbProgram2_10 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_10.setGeometry(QtCore.QRect(470, 300, 141, 31))
		self.pbProgram2_10.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_10.setProperty("value", 24)
		self.pbProgram2_10.setObjectName("pbProgram2_10")
		self.chkSel2_10 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_10.setGeometry(QtCore.QRect(450, 250, 86, 20))
		self.chkSel2_10.setText("")
		self.chkSel2_10.setObjectName("chkSel2_10")
		self.cmdDisplay2_11 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_11.setGeometry(QtCore.QRect(660, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_11.setFont(font)
		self.cmdDisplay2_11.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_11.setFlat(True)
		self.cmdDisplay2_11.setObjectName("cmdDisplay2_11")
		self.lblName2_11 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_11.setGeometry(QtCore.QRect(660, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_11.setFont(font)
		self.lblName2_11.setObjectName("lblName2_11")
		self.pbProgram2_11 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_11.setGeometry(QtCore.QRect(660, 300, 141, 31))
		self.pbProgram2_11.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_11.setProperty("value", 24)
		self.pbProgram2_11.setObjectName("pbProgram2_11")
		self.chkSel2_11 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_11.setGeometry(QtCore.QRect(640, 250, 86, 20))
		self.chkSel2_11.setText("")
		self.chkSel2_11.setObjectName("chkSel2_11")
		self.cmdDisplay2_12 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_12.setGeometry(QtCore.QRect(850, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_12.setFont(font)
		self.cmdDisplay2_12.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_12.setFlat(True)
		self.cmdDisplay2_12.setObjectName("cmdDisplay2_12")
		self.lblName2_12 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_12.setGeometry(QtCore.QRect(850, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_12.setFont(font)
		self.lblName2_12.setObjectName("lblName2_12")
		self.pbProgram2_12 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_12.setGeometry(QtCore.QRect(850, 300, 141, 31))
		self.pbProgram2_12.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_12.setProperty("value", 24)
		self.pbProgram2_12.setObjectName("pbProgram2_12")
		self.chkSel2_12 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_12.setGeometry(QtCore.QRect(830, 250, 86, 20))
		self.chkSel2_12.setText("")
		self.chkSel2_12.setObjectName("chkSel2_12")
		self.cmdDisplay2_13 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_13.setGeometry(QtCore.QRect(1040, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_13.setFont(font)
		self.cmdDisplay2_13.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_13.setFlat(True)
		self.cmdDisplay2_13.setObjectName("cmdDisplay2_13")
		self.lblName2_13 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_13.setGeometry(QtCore.QRect(1040, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_13.setFont(font)
		self.lblName2_13.setObjectName("lblName2_13")
		self.pbProgram2_13 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_13.setGeometry(QtCore.QRect(1040, 300, 141, 31))
		self.pbProgram2_13.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_13.setProperty("value", 24)
		self.pbProgram2_13.setObjectName("pbProgram2_13")
		self.chkSel2_13 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_13.setGeometry(QtCore.QRect(1020, 250, 86, 20))
		self.chkSel2_13.setText("")
		self.chkSel2_13.setObjectName("chkSel2_13")
		self.cmdDisplay2_14 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_14.setGeometry(QtCore.QRect(1230, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_14.setFont(font)
		self.cmdDisplay2_14.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_14.setFlat(True)
		self.cmdDisplay2_14.setObjectName("cmdDisplay2_14")
		self.lblName2_14 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_14.setGeometry(QtCore.QRect(1230, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_14.setFont(font)
		self.lblName2_14.setObjectName("lblName2_14")
		self.pbProgram2_14 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_14.setGeometry(QtCore.QRect(1230, 300, 141, 31))
		self.pbProgram2_14.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_14.setProperty("value", 24)
		self.pbProgram2_14.setObjectName("pbProgram2_14")
		self.chkSel2_14 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_14.setGeometry(QtCore.QRect(1210, 250, 86, 20))
		self.chkSel2_14.setText("")
		self.chkSel2_14.setObjectName("chkSel2_14")
		self.cmdDisplay2_15 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_15.setGeometry(QtCore.QRect(90, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_15.setFont(font)
		self.cmdDisplay2_15.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_15.setFlat(True)
		self.cmdDisplay2_15.setObjectName("cmdDisplay2_15")
		self.lblName2_15 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_15.setGeometry(QtCore.QRect(90, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_15.setFont(font)
		self.lblName2_15.setObjectName("lblName2_15")
		self.pbProgram2_15 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_15.setGeometry(QtCore.QRect(90, 430, 141, 31))
		self.pbProgram2_15.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_15.setProperty("value", 24)
		self.pbProgram2_15.setObjectName("pbProgram2_15")
		self.chkSel2_15 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_15.setGeometry(QtCore.QRect(70, 380, 86, 20))
		self.chkSel2_15.setText("")
		self.chkSel2_15.setObjectName("chkSel2_15")
		self.cmdDisplay2_16 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_16.setGeometry(QtCore.QRect(280, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_16.setFont(font)
		self.cmdDisplay2_16.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_16.setFlat(True)
		self.cmdDisplay2_16.setObjectName("cmdDisplay2_16")
		self.lblName2_16 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_16.setGeometry(QtCore.QRect(280, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_16.setFont(font)
		self.lblName2_16.setObjectName("lblName2_16")
		self.pbProgram2_16 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_16.setGeometry(QtCore.QRect(280, 430, 141, 31))
		self.pbProgram2_16.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_16.setProperty("value", 24)
		self.pbProgram2_16.setObjectName("pbProgram2_16")
		self.chkSel2_16 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_16.setGeometry(QtCore.QRect(260, 380, 86, 20))
		self.chkSel2_16.setText("")
		self.chkSel2_16.setObjectName("chkSel2_16")
		self.cmdDisplay2_17 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_17.setGeometry(QtCore.QRect(470, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_17.setFont(font)
		self.cmdDisplay2_17.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_17.setFlat(True)
		self.cmdDisplay2_17.setObjectName("cmdDisplay2_17")
		self.lblName2_17 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_17.setGeometry(QtCore.QRect(470, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_17.setFont(font)
		self.lblName2_17.setObjectName("lblName2_17")
		self.pbProgram2_17 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_17.setGeometry(QtCore.QRect(470, 430, 141, 31))
		self.pbProgram2_17.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_17.setProperty("value", 24)
		self.pbProgram2_17.setObjectName("pbProgram2_17")
		self.chkSel2_17 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_17.setGeometry(QtCore.QRect(450, 380, 86, 20))
		self.chkSel2_17.setText("")
		self.chkSel2_17.setObjectName("chkSel2_17")
		self.cmdDisplay2_18 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_18.setGeometry(QtCore.QRect(660, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_18.setFont(font)
		self.cmdDisplay2_18.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_18.setFlat(True)
		self.cmdDisplay2_18.setObjectName("cmdDisplay2_18")
		self.lblName2_18 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_18.setGeometry(QtCore.QRect(660, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_18.setFont(font)
		self.lblName2_18.setObjectName("lblName2_18")
		self.pbProgram2_18 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_18.setGeometry(QtCore.QRect(660, 430, 141, 31))
		self.pbProgram2_18.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_18.setProperty("value", 24)
		self.pbProgram2_18.setObjectName("pbProgram2_18")
		self.chkSel2_18 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_18.setGeometry(QtCore.QRect(640, 380, 86, 20))
		self.chkSel2_18.setText("")
		self.chkSel2_18.setObjectName("chkSel2_18")
		self.cmdDisplay2_19 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_19.setGeometry(QtCore.QRect(850, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_19.setFont(font)
		self.cmdDisplay2_19.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_19.setFlat(True)
		self.cmdDisplay2_19.setObjectName("cmdDisplay2_19")
		self.lblName2_19 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_19.setGeometry(QtCore.QRect(850, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_19.setFont(font)
		self.lblName2_19.setObjectName("lblName2_19")
		self.pbProgram2_19 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_19.setGeometry(QtCore.QRect(850, 430, 141, 31))
		self.pbProgram2_19.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_19.setProperty("value", 24)
		self.pbProgram2_19.setObjectName("pbProgram2_19")
		self.chkSel2_19 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_19.setGeometry(QtCore.QRect(830, 380, 86, 20))
		self.chkSel2_19.setText("")
		self.chkSel2_19.setObjectName("chkSel2_19")
		self.cmdDisplay2_20 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_20.setGeometry(QtCore.QRect(1040, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_20.setFont(font)
		self.cmdDisplay2_20.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_20.setFlat(True)
		self.cmdDisplay2_20.setObjectName("cmdDisplay2_20")
		self.lblName2_20 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_20.setGeometry(QtCore.QRect(1040, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_20.setFont(font)
		self.lblName2_20.setObjectName("lblName2_20")
		self.pbProgram2_20 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_20.setGeometry(QtCore.QRect(1040, 430, 141, 31))
		self.pbProgram2_20.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_20.setProperty("value", 24)
		self.pbProgram2_20.setObjectName("pbProgram2_20")
		self.chkSel2_20 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_20.setGeometry(QtCore.QRect(1020, 380, 86, 20))
		self.chkSel2_20.setText("")
		self.chkSel2_20.setObjectName("chkSel2_20")
		self.cmdDisplay2_21 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_21.setGeometry(QtCore.QRect(1230, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_21.setFont(font)
		self.cmdDisplay2_21.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_21.setFlat(True)
		self.cmdDisplay2_21.setObjectName("cmdDisplay2_21")
		self.lblName2_21 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_21.setGeometry(QtCore.QRect(1230, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_21.setFont(font)
		self.lblName2_21.setObjectName("lblName2_21")
		self.pbProgram2_21 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_21.setGeometry(QtCore.QRect(1230, 430, 141, 31))
		self.pbProgram2_21.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_21.setProperty("value", 24)
		self.pbProgram2_21.setObjectName("pbProgram2_21")
		self.chkSel2_21 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_21.setGeometry(QtCore.QRect(1210, 380, 86, 20))
		self.chkSel2_21.setText("")
		self.chkSel2_21.setObjectName("chkSel2_21")
		self.cmdDisplay2_22 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_22.setGeometry(QtCore.QRect(90, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_22.setFont(font)
		self.cmdDisplay2_22.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_22.setFlat(True)
		self.cmdDisplay2_22.setObjectName("cmdDisplay2_22")
		self.lblName2_22 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_22.setGeometry(QtCore.QRect(90, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_22.setFont(font)
		self.lblName2_22.setObjectName("lblName2_22")
		self.pbProgram2_22 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_22.setGeometry(QtCore.QRect(90, 560, 141, 31))
		self.pbProgram2_22.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_22.setProperty("value", 24)
		self.pbProgram2_22.setObjectName("pbProgram2_22")
		self.chkSel2_22 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_22.setGeometry(QtCore.QRect(70, 510, 86, 20))
		self.chkSel2_22.setText("")
		self.chkSel2_22.setObjectName("chkSel2_22")
		self.cmdDisplay2_23 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_23.setGeometry(QtCore.QRect(280, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_23.setFont(font)
		self.cmdDisplay2_23.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_23.setFlat(True)
		self.cmdDisplay2_23.setObjectName("cmdDisplay2_23")
		self.lblName2_23 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_23.setGeometry(QtCore.QRect(280, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_23.setFont(font)
		self.lblName2_23.setObjectName("lblName2_23")
		self.pbProgram2_23 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_23.setGeometry(QtCore.QRect(280, 560, 141, 31))
		self.pbProgram2_23.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_23.setProperty("value", 24)
		self.pbProgram2_23.setObjectName("pbProgram2_23")
		self.chkSel2_23 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_23.setGeometry(QtCore.QRect(260, 510, 86, 20))
		self.chkSel2_23.setText("")
		self.chkSel2_23.setObjectName("chkSel2_23")
		self.cmdDisplay2_24 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_24.setGeometry(QtCore.QRect(470, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_24.setFont(font)
		self.cmdDisplay2_24.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_24.setFlat(True)
		self.cmdDisplay2_24.setObjectName("cmdDisplay2_24")
		self.lblName2_24 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_24.setGeometry(QtCore.QRect(470, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_24.setFont(font)
		self.lblName2_24.setObjectName("lblName2_24")
		self.pbProgram2_24 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_24.setGeometry(QtCore.QRect(470, 560, 141, 31))
		self.pbProgram2_24.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_24.setProperty("value", 24)
		self.pbProgram2_24.setObjectName("pbProgram2_24")
		self.chkSel2_24 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_24.setGeometry(QtCore.QRect(450, 510, 86, 20))
		self.chkSel2_24.setText("")
		self.chkSel2_24.setObjectName("chkSel2_24")
		self.cmdDisplay2_25 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_25.setGeometry(QtCore.QRect(660, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_25.setFont(font)
		self.cmdDisplay2_25.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_25.setFlat(True)
		self.cmdDisplay2_25.setObjectName("cmdDisplay2_25")
		self.lblName2_25 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_25.setGeometry(QtCore.QRect(660, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_25.setFont(font)
		self.lblName2_25.setObjectName("lblName2_25")
		self.pbProgram2_25 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_25.setGeometry(QtCore.QRect(660, 560, 141, 31))
		self.pbProgram2_25.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_25.setProperty("value", 24)
		self.pbProgram2_25.setObjectName("pbProgram2_25")
		self.chkSel2_25 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_25.setGeometry(QtCore.QRect(640, 510, 86, 20))
		self.chkSel2_25.setText("")
		self.chkSel2_25.setObjectName("chkSel2_25")
		self.cmdDisplay2_26 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_26.setGeometry(QtCore.QRect(850, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_26.setFont(font)
		self.cmdDisplay2_26.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_26.setFlat(True)
		self.cmdDisplay2_26.setObjectName("cmdDisplay2_26")
		self.lblName2_26 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_26.setGeometry(QtCore.QRect(850, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_26.setFont(font)
		self.lblName2_26.setObjectName("lblName2_26")
		self.pbProgram2_26 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_26.setGeometry(QtCore.QRect(850, 560, 141, 31))
		self.pbProgram2_26.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_26.setProperty("value", 24)
		self.pbProgram2_26.setObjectName("pbProgram2_26")
		self.chkSel2_26 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_26.setGeometry(QtCore.QRect(830, 510, 86, 20))
		self.chkSel2_26.setText("")
		self.chkSel2_26.setObjectName("chkSel2_26")
		self.cmdDisplay2_27 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_27.setGeometry(QtCore.QRect(1040, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_27.setFont(font)
		self.cmdDisplay2_27.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_27.setFlat(True)
		self.cmdDisplay2_27.setObjectName("cmdDisplay2_27")
		self.lblName2_27 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_27.setGeometry(QtCore.QRect(1040, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_27.setFont(font)
		self.lblName2_27.setObjectName("lblName2_27")
		self.pbProgram2_27 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_27.setGeometry(QtCore.QRect(1040, 560, 141, 31))
		self.pbProgram2_27.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_27.setProperty("value", 24)
		self.pbProgram2_27.setObjectName("pbProgram2_27")
		self.chkSel2_27 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_27.setGeometry(QtCore.QRect(1020, 510, 86, 20))
		self.chkSel2_27.setText("")
		self.chkSel2_27.setObjectName("chkSel2_27")
		self.cmdDisplay2_28 = QtWidgets.QPushButton(self.tbPage2)
		self.cmdDisplay2_28.setGeometry(QtCore.QRect(1230, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay2_28.setFont(font)
		self.cmdDisplay2_28.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay2_28.setFlat(True)
		self.cmdDisplay2_28.setObjectName("cmdDisplay2_28")
		self.lblName2_28 = QtWidgets.QLabel(self.tbPage2)
		self.lblName2_28.setGeometry(QtCore.QRect(1230, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName2_28.setFont(font)
		self.lblName2_28.setObjectName("lblName2_28")
		self.pbProgram2_28 = QtWidgets.QProgressBar(self.tbPage2)
		self.pbProgram2_28.setGeometry(QtCore.QRect(1230, 560, 141, 31))
		self.pbProgram2_28.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram2_28.setProperty("value", 24)
		self.pbProgram2_28.setObjectName("pbProgram2_28")
		self.chkSel2_28 = QtWidgets.QCheckBox(self.tbPage2)
		self.chkSel2_28.setGeometry(QtCore.QRect(1210, 510, 86, 20))
		self.chkSel2_28.setText("")
		self.chkSel2_28.setObjectName("chkSel2_28")
		self.tabWidget.addTab(self.tbPage2, "")
		self.tbPage3 = QtWidgets.QWidget()
		self.tbPage3.setObjectName("tbPage3")
		self.lblPage3 = QtWidgets.QLabel(self.tbPage3)
		self.lblPage3.setGeometry(QtCore.QRect(40, 30, 671, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.lblPage3.setFont(font)
		self.lblPage3.setObjectName("lblPage3")
		self.cmdDisplay3_1 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_1.setGeometry(QtCore.QRect(90, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_1.setFont(font)
		self.cmdDisplay3_1.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_1.setFlat(True)
		self.cmdDisplay3_1.setObjectName("cmdDisplay3_1")
		self.lblName3_1 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_1.setGeometry(QtCore.QRect(90, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_1.setFont(font)
		self.lblName3_1.setObjectName("lblName3_1")
		self.pbProgram3_1 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_1.setGeometry(QtCore.QRect(90, 170, 141, 31))
		self.pbProgram3_1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_1.setProperty("value", 24)
		self.pbProgram3_1.setObjectName("pbProgram3_1")
		self.chkSel3_1 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_1.setGeometry(QtCore.QRect(70, 120, 86, 20))
		self.chkSel3_1.setText("")
		self.chkSel3_1.setObjectName("chkSel3_1")
		self.pbProgram3_2 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_2.setGeometry(QtCore.QRect(280, 170, 141, 31))
		self.pbProgram3_2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_2.setProperty("value", 24)
		self.pbProgram3_2.setObjectName("pbProgram3_2")
		self.chkSel3_2 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_2.setGeometry(QtCore.QRect(260, 120, 86, 20))
		self.chkSel3_2.setText("")
		self.chkSel3_2.setObjectName("chkSel3_2")
		self.lblName3_2 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_2.setGeometry(QtCore.QRect(280, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_2.setFont(font)
		self.lblName3_2.setObjectName("lblName3_2")
		self.cmdDisplay3_2 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_2.setGeometry(QtCore.QRect(280, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_2.setFont(font)
		self.cmdDisplay3_2.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_2.setFlat(True)
		self.cmdDisplay3_2.setObjectName("cmdDisplay3_2")
		self.pbProgram3_3 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
		self.pbProgram3_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_3.setProperty("value", 24)
		self.pbProgram3_3.setObjectName("pbProgram3_3")
		self.chkSel3_3 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_3.setGeometry(QtCore.QRect(450, 120, 86, 20))
		self.chkSel3_3.setText("")
		self.chkSel3_3.setObjectName("chkSel3_3")
		self.lblName3_3 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_3.setGeometry(QtCore.QRect(470, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_3.setFont(font)
		self.lblName3_3.setObjectName("lblName3_3")
		self.cmdDisplay3_3 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_3.setGeometry(QtCore.QRect(470, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_3.setFont(font)
		self.cmdDisplay3_3.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_3.setFlat(True)
		self.cmdDisplay3_3.setObjectName("cmdDisplay3_3")
		self.pbProgram3_4 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_4.setGeometry(QtCore.QRect(660, 170, 141, 31))
		self.pbProgram3_4.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_4.setProperty("value", 24)
		self.pbProgram3_4.setObjectName("pbProgram3_4")
		self.chkSel3_4 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_4.setGeometry(QtCore.QRect(640, 120, 86, 20))
		self.chkSel3_4.setText("")
		self.chkSel3_4.setObjectName("chkSel3_4")
		self.lblName3_4 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_4.setGeometry(QtCore.QRect(660, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_4.setFont(font)
		self.lblName3_4.setObjectName("lblName3_4")
		self.cmdDisplay3_4 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_4.setGeometry(QtCore.QRect(660, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_4.setFont(font)
		self.cmdDisplay3_4.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_4.setFlat(True)
		self.cmdDisplay3_4.setObjectName("cmdDisplay3_4")
		self.pbProgram3_5 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_5.setGeometry(QtCore.QRect(850, 170, 141, 31))
		self.pbProgram3_5.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_5.setProperty("value", 24)
		self.pbProgram3_5.setObjectName("pbProgram3_5")
		self.chkSel3_5 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_5.setGeometry(QtCore.QRect(830, 120, 86, 20))
		self.chkSel3_5.setText("")
		self.chkSel3_5.setObjectName("chkSel3_5")
		self.lblName3_5 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_5.setGeometry(QtCore.QRect(850, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_5.setFont(font)
		self.lblName3_5.setObjectName("lblName3_5")
		self.cmdDisplay3_5 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_5.setGeometry(QtCore.QRect(850, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_5.setFont(font)
		self.cmdDisplay3_5.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_5.setFlat(True)
		self.cmdDisplay3_5.setObjectName("cmdDisplay3_5")
		self.pbProgram3_6 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_6.setGeometry(QtCore.QRect(1040, 170, 141, 31))
		self.pbProgram3_6.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_6.setProperty("value", 24)
		self.pbProgram3_6.setObjectName("pbProgram3_6")
		self.chkSel3_6 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_6.setGeometry(QtCore.QRect(1020, 120, 86, 20))
		self.chkSel3_6.setText("")
		self.chkSel3_6.setObjectName("chkSel3_6")
		self.lblName3_6 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_6.setGeometry(QtCore.QRect(1040, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_6.setFont(font)
		self.lblName3_6.setObjectName("lblName3_6")
		self.cmdDisplay3_6 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_6.setGeometry(QtCore.QRect(1040, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_6.setFont(font)
		self.cmdDisplay3_6.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_6.setFlat(True)
		self.cmdDisplay3_6.setObjectName("cmdDisplay3_6")
		self.pbProgram3_7 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_7.setGeometry(QtCore.QRect(1230, 170, 141, 31))
		self.pbProgram3_7.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_7.setProperty("value", 24)
		self.pbProgram3_7.setObjectName("pbProgram3_7")
		self.chkSel3_7 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_7.setGeometry(QtCore.QRect(1210, 120, 86, 20))
		self.chkSel3_7.setText("")
		self.chkSel3_7.setObjectName("chkSel3_7")
		self.lblName3_7 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_7.setGeometry(QtCore.QRect(1230, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_7.setFont(font)
		self.lblName3_7.setObjectName("lblName3_7")
		self.cmdDisplay3_7 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_7.setGeometry(QtCore.QRect(1230, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_7.setFont(font)
		self.cmdDisplay3_7.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_7.setFlat(True)
		self.cmdDisplay3_7.setObjectName("cmdDisplay3_7")
		self.pbProgram3_8 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_8.setGeometry(QtCore.QRect(90, 300, 141, 31))
		self.pbProgram3_8.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_8.setProperty("value", 24)
		self.pbProgram3_8.setObjectName("pbProgram3_8")
		self.chkSel3_8 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_8.setGeometry(QtCore.QRect(70, 250, 86, 20))
		self.chkSel3_8.setText("")
		self.chkSel3_8.setObjectName("chkSel3_8")
		self.lblName3_8 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_8.setGeometry(QtCore.QRect(90, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_8.setFont(font)
		self.lblName3_8.setObjectName("lblName3_8")
		self.cmdDisplay3_8 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_8.setGeometry(QtCore.QRect(90, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_8.setFont(font)
		self.cmdDisplay3_8.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_8.setFlat(True)
		self.cmdDisplay3_8.setObjectName("cmdDisplay3_8")
		self.pbProgram3_9 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_9.setGeometry(QtCore.QRect(280, 300, 141, 31))
		self.pbProgram3_9.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_9.setProperty("value", 24)
		self.pbProgram3_9.setObjectName("pbProgram3_9")
		self.chkSel3_9 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_9.setGeometry(QtCore.QRect(260, 250, 86, 20))
		self.chkSel3_9.setText("")
		self.chkSel3_9.setObjectName("chkSel3_9")
		self.lblName3_9 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_9.setGeometry(QtCore.QRect(280, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_9.setFont(font)
		self.lblName3_9.setObjectName("lblName3_9")
		self.cmdDisplay3_9 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_9.setGeometry(QtCore.QRect(280, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_9.setFont(font)
		self.cmdDisplay3_9.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_9.setFlat(True)
		self.cmdDisplay3_9.setObjectName("cmdDisplay3_9")
		self.pbProgram3_10 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_10.setGeometry(QtCore.QRect(470, 300, 141, 31))
		self.pbProgram3_10.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_10.setProperty("value", 24)
		self.pbProgram3_10.setObjectName("pbProgram3_10")
		self.chkSel3_10 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_10.setGeometry(QtCore.QRect(450, 250, 86, 20))
		self.chkSel3_10.setText("")
		self.chkSel3_10.setObjectName("chkSel3_10")
		self.lblName3_10 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_10.setGeometry(QtCore.QRect(470, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_10.setFont(font)
		self.lblName3_10.setObjectName("lblName3_10")
		self.cmdDisplay3_10 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_10.setGeometry(QtCore.QRect(470, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_10.setFont(font)
		self.cmdDisplay3_10.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_10.setFlat(True)
		self.cmdDisplay3_10.setObjectName("cmdDisplay3_10")
		self.pbProgram3_11 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_11.setGeometry(QtCore.QRect(660, 300, 141, 31))
		self.pbProgram3_11.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_11.setProperty("value", 24)
		self.pbProgram3_11.setObjectName("pbProgram3_11")
		self.chkSel3_11 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_11.setGeometry(QtCore.QRect(640, 250, 86, 20))
		self.chkSel3_11.setText("")
		self.chkSel3_11.setObjectName("chkSel3_11")
		self.lblName3_11 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_11.setGeometry(QtCore.QRect(660, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_11.setFont(font)
		self.lblName3_11.setObjectName("lblName3_11")
		self.cmdDisplay3_11 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_11.setGeometry(QtCore.QRect(660, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_11.setFont(font)
		self.cmdDisplay3_11.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_11.setFlat(True)
		self.cmdDisplay3_11.setObjectName("cmdDisplay3_11")
		self.pbProgram3_12 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_12.setGeometry(QtCore.QRect(850, 300, 141, 31))
		self.pbProgram3_12.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_12.setProperty("value", 24)
		self.pbProgram3_12.setObjectName("pbProgram3_12")
		self.chkSel3_12 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_12.setGeometry(QtCore.QRect(830, 250, 86, 20))
		self.chkSel3_12.setText("")
		self.chkSel3_12.setObjectName("chkSel3_12")
		self.lblName3_12 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_12.setGeometry(QtCore.QRect(850, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_12.setFont(font)
		self.lblName3_12.setObjectName("lblName3_12")
		self.cmdDisplay3_12 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_12.setGeometry(QtCore.QRect(850, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_12.setFont(font)
		self.cmdDisplay3_12.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_12.setFlat(True)
		self.cmdDisplay3_12.setObjectName("cmdDisplay3_12")
		self.pbProgram3_13 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_13.setGeometry(QtCore.QRect(1040, 300, 141, 31))
		self.pbProgram3_13.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_13.setProperty("value", 24)
		self.pbProgram3_13.setObjectName("pbProgram3_13")
		self.chkSel3_13 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_13.setGeometry(QtCore.QRect(1020, 250, 86, 20))
		self.chkSel3_13.setText("")
		self.chkSel3_13.setObjectName("chkSel3_13")
		self.lblName3_13 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_13.setGeometry(QtCore.QRect(1040, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_13.setFont(font)
		self.lblName3_13.setObjectName("lblName3_13")
		self.cmdDisplay3_13 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_13.setGeometry(QtCore.QRect(1040, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_13.setFont(font)
		self.cmdDisplay3_13.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_13.setFlat(True)
		self.cmdDisplay3_13.setObjectName("cmdDisplay3_13")
		self.pbProgram3_14 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_14.setGeometry(QtCore.QRect(1230, 300, 141, 31))
		self.pbProgram3_14.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_14.setProperty("value", 24)
		self.pbProgram3_14.setObjectName("pbProgram3_14")
		self.chkSel3_14 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_14.setGeometry(QtCore.QRect(1210, 250, 86, 20))
		self.chkSel3_14.setText("")
		self.chkSel3_14.setObjectName("chkSel3_14")
		self.lblName3_14 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_14.setGeometry(QtCore.QRect(1230, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_14.setFont(font)
		self.lblName3_14.setObjectName("lblName3_14")
		self.cmdDisplay3_14 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_14.setGeometry(QtCore.QRect(1230, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_14.setFont(font)
		self.cmdDisplay3_14.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_14.setFlat(True)
		self.cmdDisplay3_14.setObjectName("cmdDisplay3_14")
		self.pbProgram3_15 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_15.setGeometry(QtCore.QRect(90, 430, 141, 31))
		self.pbProgram3_15.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_15.setProperty("value", 24)
		self.pbProgram3_15.setObjectName("pbProgram3_15")
		self.chkSel3_15 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_15.setGeometry(QtCore.QRect(70, 380, 86, 20))
		self.chkSel3_15.setText("")
		self.chkSel3_15.setObjectName("chkSel3_15")
		self.lblName3_15 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_15.setGeometry(QtCore.QRect(90, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_15.setFont(font)
		self.lblName3_15.setObjectName("lblName3_15")
		self.cmdDisplay3_15 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_15.setGeometry(QtCore.QRect(90, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_15.setFont(font)
		self.cmdDisplay3_15.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_15.setFlat(True)
		self.cmdDisplay3_15.setObjectName("cmdDisplay3_15")
		self.pbProgram3_16 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_16.setGeometry(QtCore.QRect(280, 430, 141, 31))
		self.pbProgram3_16.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_16.setProperty("value", 24)
		self.pbProgram3_16.setObjectName("pbProgram3_16")
		self.chkSel3_16 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_16.setGeometry(QtCore.QRect(260, 380, 86, 20))
		self.chkSel3_16.setText("")
		self.chkSel3_16.setObjectName("chkSel3_16")
		self.lblName3_16 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_16.setGeometry(QtCore.QRect(280, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_16.setFont(font)
		self.lblName3_16.setObjectName("lblName3_16")
		self.cmdDisplay3_16 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_16.setGeometry(QtCore.QRect(280, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_16.setFont(font)
		self.cmdDisplay3_16.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_16.setFlat(True)
		self.cmdDisplay3_16.setObjectName("cmdDisplay3_16")
		self.pbProgram3_17 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_17.setGeometry(QtCore.QRect(470, 430, 141, 31))
		self.pbProgram3_17.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_17.setProperty("value", 24)
		self.pbProgram3_17.setObjectName("pbProgram3_17")
		self.chkSel3_17 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_17.setGeometry(QtCore.QRect(450, 380, 86, 20))
		self.chkSel3_17.setText("")
		self.chkSel3_17.setObjectName("chkSel3_17")
		self.lblName3_17 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_17.setGeometry(QtCore.QRect(470, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_17.setFont(font)
		self.lblName3_17.setObjectName("lblName3_17")
		self.cmdDisplay3_17 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_17.setGeometry(QtCore.QRect(470, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_17.setFont(font)
		self.cmdDisplay3_17.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_17.setFlat(True)
		self.cmdDisplay3_17.setObjectName("cmdDisplay3_17")
		self.pbProgram3_18 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_18.setGeometry(QtCore.QRect(660, 430, 141, 31))
		self.pbProgram3_18.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_18.setProperty("value", 24)
		self.pbProgram3_18.setObjectName("pbProgram3_18")
		self.chkSel3_18 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_18.setGeometry(QtCore.QRect(640, 380, 86, 20))
		self.chkSel3_18.setText("")
		self.chkSel3_18.setObjectName("chkSel3_18")
		self.lblName3_18 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_18.setGeometry(QtCore.QRect(660, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_18.setFont(font)
		self.lblName3_18.setObjectName("lblName3_18")
		self.cmdDisplay3_18 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_18.setGeometry(QtCore.QRect(660, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_18.setFont(font)
		self.cmdDisplay3_18.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_18.setFlat(True)
		self.cmdDisplay3_18.setObjectName("cmdDisplay3_18")
		self.pbProgram3_19 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_19.setGeometry(QtCore.QRect(850, 430, 141, 31))
		self.pbProgram3_19.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_19.setProperty("value", 24)
		self.pbProgram3_19.setObjectName("pbProgram3_19")
		self.chkSel3_19 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_19.setGeometry(QtCore.QRect(830, 380, 86, 20))
		self.chkSel3_19.setText("")
		self.chkSel3_19.setObjectName("chkSel3_19")
		self.lblName3_19 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_19.setGeometry(QtCore.QRect(850, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_19.setFont(font)
		self.lblName3_19.setObjectName("lblName3_19")
		self.cmdDisplay3_19 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_19.setGeometry(QtCore.QRect(850, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_19.setFont(font)
		self.cmdDisplay3_19.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_19.setFlat(True)
		self.cmdDisplay3_19.setObjectName("cmdDisplay3_19")
		self.pbProgram3_20 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_20.setGeometry(QtCore.QRect(1040, 430, 141, 31))
		self.pbProgram3_20.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_20.setProperty("value", 24)
		self.pbProgram3_20.setObjectName("pbProgram3_20")
		self.chkSel3_20 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_20.setGeometry(QtCore.QRect(1020, 380, 86, 20))
		self.chkSel3_20.setText("")
		self.chkSel3_20.setObjectName("chkSel3_20")
		self.lblName3_20 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_20.setGeometry(QtCore.QRect(1040, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_20.setFont(font)
		self.lblName3_20.setObjectName("lblName3_20")
		self.cmdDisplay3_20 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_20.setGeometry(QtCore.QRect(1040, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_20.setFont(font)
		self.cmdDisplay3_20.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_20.setFlat(True)
		self.cmdDisplay3_20.setObjectName("cmdDisplay3_20")
		self.pbProgram3_21 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_21.setGeometry(QtCore.QRect(1230, 430, 141, 31))
		self.pbProgram3_21.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_21.setProperty("value", 24)
		self.pbProgram3_21.setObjectName("pbProgram3_21")
		self.chkSel3_21 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_21.setGeometry(QtCore.QRect(1210, 380, 86, 20))
		self.chkSel3_21.setText("")
		self.chkSel3_21.setObjectName("chkSel3_21")
		self.lblName3_21 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_21.setGeometry(QtCore.QRect(1230, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_21.setFont(font)
		self.lblName3_21.setObjectName("lblName3_21")
		self.cmdDisplay3_21 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_21.setGeometry(QtCore.QRect(1230, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_21.setFont(font)
		self.cmdDisplay3_21.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_21.setFlat(True)
		self.cmdDisplay3_21.setObjectName("cmdDisplay3_21")
		self.pbProgram3_22 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_22.setGeometry(QtCore.QRect(90, 560, 141, 31))
		self.pbProgram3_22.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_22.setProperty("value", 24)
		self.pbProgram3_22.setObjectName("pbProgram3_22")
		self.chkSel3_22 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_22.setGeometry(QtCore.QRect(70, 510, 86, 20))
		self.chkSel3_22.setText("")
		self.chkSel3_22.setObjectName("chkSel3_22")
		self.lblName3_22 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_22.setGeometry(QtCore.QRect(90, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_22.setFont(font)
		self.lblName3_22.setObjectName("lblName3_22")
		self.cmdDisplay3_22 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_22.setGeometry(QtCore.QRect(90, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_22.setFont(font)
		self.cmdDisplay3_22.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_22.setFlat(True)
		self.cmdDisplay3_22.setObjectName("cmdDisplay3_22")
		self.pbProgram3_23 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_23.setGeometry(QtCore.QRect(280, 560, 141, 31))
		self.pbProgram3_23.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_23.setProperty("value", 24)
		self.pbProgram3_23.setObjectName("pbProgram3_23")
		self.chkSel3_23 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_23.setGeometry(QtCore.QRect(260, 510, 86, 20))
		self.chkSel3_23.setText("")
		self.chkSel3_23.setObjectName("chkSel3_23")
		self.lblName3_23 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_23.setGeometry(QtCore.QRect(280, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_23.setFont(font)
		self.lblName3_23.setObjectName("lblName3_23")
		self.cmdDisplay3_23 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_23.setGeometry(QtCore.QRect(280, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_23.setFont(font)
		self.cmdDisplay3_23.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_23.setFlat(True)
		self.cmdDisplay3_23.setObjectName("cmdDisplay3_23")
		self.pbProgram3_24 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_24.setGeometry(QtCore.QRect(470, 560, 141, 31))
		self.pbProgram3_24.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_24.setProperty("value", 24)
		self.pbProgram3_24.setObjectName("pbProgram3_24")
		self.chkSel3_24 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_24.setGeometry(QtCore.QRect(450, 510, 86, 20))
		self.chkSel3_24.setText("")
		self.chkSel3_24.setObjectName("chkSel3_24")
		self.lblName3_24 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_24.setGeometry(QtCore.QRect(470, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_24.setFont(font)
		self.lblName3_24.setObjectName("lblName3_24")
		self.cmdDisplay3_24 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_24.setGeometry(QtCore.QRect(470, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_24.setFont(font)
		self.cmdDisplay3_24.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_24.setFlat(True)
		self.cmdDisplay3_24.setObjectName("cmdDisplay3_24")
		self.pbProgram3_25 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_25.setGeometry(QtCore.QRect(660, 560, 141, 31))
		self.pbProgram3_25.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_25.setProperty("value", 24)
		self.pbProgram3_25.setObjectName("pbProgram3_25")
		self.chkSel3_25 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_25.setGeometry(QtCore.QRect(640, 510, 86, 20))
		self.chkSel3_25.setText("")
		self.chkSel3_25.setObjectName("chkSel3_25")
		self.lblName3_25 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_25.setGeometry(QtCore.QRect(660, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_25.setFont(font)
		self.lblName3_25.setObjectName("lblName3_25")
		self.cmdDisplay3_25 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_25.setGeometry(QtCore.QRect(660, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_25.setFont(font)
		self.cmdDisplay3_25.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_25.setFlat(True)
		self.cmdDisplay3_25.setObjectName("cmdDisplay3_25")
		self.pbProgram3_26 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_26.setGeometry(QtCore.QRect(850, 560, 141, 31))
		self.pbProgram3_26.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_26.setProperty("value", 24)
		self.pbProgram3_26.setObjectName("pbProgram3_26")
		self.chkSel3_26 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_26.setGeometry(QtCore.QRect(830, 510, 86, 20))
		self.chkSel3_26.setText("")
		self.chkSel3_26.setObjectName("chkSel3_26")
		self.lblName3_26 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_26.setGeometry(QtCore.QRect(850, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_26.setFont(font)
		self.lblName3_26.setObjectName("lblName3_26")
		self.cmdDisplay3_26 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_26.setGeometry(QtCore.QRect(850, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_26.setFont(font)
		self.cmdDisplay3_26.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_26.setFlat(True)
		self.cmdDisplay3_26.setObjectName("cmdDisplay3_26")
		self.pbProgram3_27 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_27.setGeometry(QtCore.QRect(1040, 560, 141, 31))
		self.pbProgram3_27.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_27.setProperty("value", 24)
		self.pbProgram3_27.setObjectName("pbProgram3_27")
		self.chkSel3_27 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_27.setGeometry(QtCore.QRect(1020, 510, 86, 20))
		self.chkSel3_27.setText("")
		self.chkSel3_27.setObjectName("chkSel3_27")
		self.lblName3_27 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_27.setGeometry(QtCore.QRect(1040, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_27.setFont(font)
		self.lblName3_27.setObjectName("lblName3_27")
		self.cmdDisplay3_27 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_27.setGeometry(QtCore.QRect(1040, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_27.setFont(font)
		self.cmdDisplay3_27.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_27.setFlat(True)
		self.cmdDisplay3_27.setObjectName("cmdDisplay3_27")
		self.pbProgram3_28 = QtWidgets.QProgressBar(self.tbPage3)
		self.pbProgram3_28.setGeometry(QtCore.QRect(1230, 560, 141, 31))
		self.pbProgram3_28.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram3_28.setProperty("value", 24)
		self.pbProgram3_28.setObjectName("pbProgram3_28")
		self.chkSel3_28 = QtWidgets.QCheckBox(self.tbPage3)
		self.chkSel3_28.setGeometry(QtCore.QRect(1210, 510, 86, 20))
		self.chkSel3_28.setText("")
		self.chkSel3_28.setObjectName("chkSel3_28")
		self.lblName3_28 = QtWidgets.QLabel(self.tbPage3)
		self.lblName3_28.setGeometry(QtCore.QRect(1230, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName3_28.setFont(font)
		self.lblName3_28.setObjectName("lblName3_28")
		self.cmdDisplay3_28 = QtWidgets.QPushButton(self.tbPage3)
		self.cmdDisplay3_28.setGeometry(QtCore.QRect(1230, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay3_28.setFont(font)
		self.cmdDisplay3_28.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay3_28.setFlat(True)
		self.cmdDisplay3_28.setObjectName("cmdDisplay3_28")
		self.tabWidget.addTab(self.tbPage3, "")
		self.tbPage4 = QtWidgets.QWidget()
		self.tbPage4.setObjectName("tbPage4")
		self.lblPage4 = QtWidgets.QLabel(self.tbPage4)
		self.lblPage4.setGeometry(QtCore.QRect(40, 30, 671, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.lblPage4.setFont(font)
		self.lblPage4.setObjectName("lblPage4")
		self.pbProgram4_1 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_1.setGeometry(QtCore.QRect(90, 170, 141, 31))
		self.pbProgram4_1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_1.setProperty("value", 24)
		self.pbProgram4_1.setObjectName("pbProgram4_1")
		self.chkSel4_1 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_1.setGeometry(QtCore.QRect(70, 120, 86, 20))
		self.chkSel4_1.setText("")
		self.chkSel4_1.setObjectName("chkSel4_1")
		self.lblName4_1 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_1.setGeometry(QtCore.QRect(90, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_1.setFont(font)
		self.lblName4_1.setObjectName("lblName4_1")
		self.cmdDisplay4_1 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_1.setGeometry(QtCore.QRect(90, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_1.setFont(font)
		self.cmdDisplay4_1.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_1.setFlat(True)
		self.cmdDisplay4_1.setObjectName("cmdDisplay4_1")
		self.cmdDisplay4_2 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_2.setGeometry(QtCore.QRect(280, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_2.setFont(font)
		self.cmdDisplay4_2.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_2.setFlat(True)
		self.cmdDisplay4_2.setObjectName("cmdDisplay4_2")
		self.pbProgram4_2 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_2.setGeometry(QtCore.QRect(280, 170, 141, 31))
		self.pbProgram4_2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_2.setProperty("value", 24)
		self.pbProgram4_2.setObjectName("pbProgram4_2")
		self.lblName4_2 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_2.setGeometry(QtCore.QRect(280, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_2.setFont(font)
		self.lblName4_2.setObjectName("lblName4_2")
		self.chkSel4_2 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_2.setGeometry(QtCore.QRect(260, 120, 86, 20))
		self.chkSel4_2.setText("")
		self.chkSel4_2.setObjectName("chkSel4_2")
		self.cmdDisplay4_3 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_3.setGeometry(QtCore.QRect(470, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_3.setFont(font)
		self.cmdDisplay4_3.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_3.setFlat(True)
		self.cmdDisplay4_3.setObjectName("cmdDisplay4_3")
		self.pbProgram4_3 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
		self.pbProgram4_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_3.setProperty("value", 24)
		self.pbProgram4_3.setObjectName("pbProgram4_3")
		self.lblName4_3 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_3.setGeometry(QtCore.QRect(470, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_3.setFont(font)
		self.lblName4_3.setObjectName("lblName4_3")
		self.chkSel4_3 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_3.setGeometry(QtCore.QRect(450, 120, 86, 20))
		self.chkSel4_3.setText("")
		self.chkSel4_3.setObjectName("chkSel4_3")
		self.cmdDisplay4_4 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_4.setGeometry(QtCore.QRect(660, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_4.setFont(font)
		self.cmdDisplay4_4.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_4.setFlat(True)
		self.cmdDisplay4_4.setObjectName("cmdDisplay4_4")
		self.pbProgram4_4 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_4.setGeometry(QtCore.QRect(660, 170, 141, 31))
		self.pbProgram4_4.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_4.setProperty("value", 24)
		self.pbProgram4_4.setObjectName("pbProgram4_4")
		self.lblName4_4 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_4.setGeometry(QtCore.QRect(660, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_4.setFont(font)
		self.lblName4_4.setObjectName("lblName4_4")
		self.chkSel4_4 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_4.setGeometry(QtCore.QRect(640, 120, 86, 20))
		self.chkSel4_4.setText("")
		self.chkSel4_4.setObjectName("chkSel4_4")
		self.cmdDisplay4_5 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_5.setGeometry(QtCore.QRect(850, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_5.setFont(font)
		self.cmdDisplay4_5.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_5.setFlat(True)
		self.cmdDisplay4_5.setObjectName("cmdDisplay4_5")
		self.pbProgram4_5 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_5.setGeometry(QtCore.QRect(850, 170, 141, 31))
		self.pbProgram4_5.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_5.setProperty("value", 24)
		self.pbProgram4_5.setObjectName("pbProgram4_5")
		self.lblName4_5 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_5.setGeometry(QtCore.QRect(850, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_5.setFont(font)
		self.lblName4_5.setObjectName("lblName4_5")
		self.chkSel4_5 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_5.setGeometry(QtCore.QRect(830, 120, 86, 20))
		self.chkSel4_5.setText("")
		self.chkSel4_5.setObjectName("chkSel4_5")
		self.cmdDisplay4_6 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_6.setGeometry(QtCore.QRect(1040, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_6.setFont(font)
		self.cmdDisplay4_6.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_6.setFlat(True)
		self.cmdDisplay4_6.setObjectName("cmdDisplay4_6")
		self.pbProgram4_6 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_6.setGeometry(QtCore.QRect(1040, 170, 141, 31))
		self.pbProgram4_6.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_6.setProperty("value", 24)
		self.pbProgram4_6.setObjectName("pbProgram4_6")
		self.lblName4_6 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_6.setGeometry(QtCore.QRect(1040, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_6.setFont(font)
		self.lblName4_6.setObjectName("lblName4_6")
		self.chkSel4_6 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_6.setGeometry(QtCore.QRect(1020, 120, 86, 20))
		self.chkSel4_6.setText("")
		self.chkSel4_6.setObjectName("chkSel4_6")
		self.cmdDisplay4_7 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_7.setGeometry(QtCore.QRect(1230, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_7.setFont(font)
		self.cmdDisplay4_7.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_7.setFlat(True)
		self.cmdDisplay4_7.setObjectName("cmdDisplay4_7")
		self.pbProgram4_7 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_7.setGeometry(QtCore.QRect(1230, 170, 141, 31))
		self.pbProgram4_7.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_7.setProperty("value", 24)
		self.pbProgram4_7.setObjectName("pbProgram4_7")
		self.lblName4_7 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_7.setGeometry(QtCore.QRect(1230, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_7.setFont(font)
		self.lblName4_7.setObjectName("lblName4_7")
		self.chkSel4_7 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_7.setGeometry(QtCore.QRect(1210, 120, 86, 20))
		self.chkSel4_7.setText("")
		self.chkSel4_7.setObjectName("chkSel4_7")
		self.cmdDisplay4_8 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_8.setGeometry(QtCore.QRect(90, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_8.setFont(font)
		self.cmdDisplay4_8.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_8.setFlat(True)
		self.cmdDisplay4_8.setObjectName("cmdDisplay4_8")
		self.pbProgram4_8 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_8.setGeometry(QtCore.QRect(90, 300, 141, 31))
		self.pbProgram4_8.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_8.setProperty("value", 24)
		self.pbProgram4_8.setObjectName("pbProgram4_8")
		self.lblName4_8 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_8.setGeometry(QtCore.QRect(90, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_8.setFont(font)
		self.lblName4_8.setObjectName("lblName4_8")
		self.chkSel4_8 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_8.setGeometry(QtCore.QRect(70, 250, 86, 20))
		self.chkSel4_8.setText("")
		self.chkSel4_8.setObjectName("chkSel4_8")
		self.cmdDisplay4_9 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_9.setGeometry(QtCore.QRect(280, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_9.setFont(font)
		self.cmdDisplay4_9.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_9.setFlat(True)
		self.cmdDisplay4_9.setObjectName("cmdDisplay4_9")
		self.pbProgram4_9 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_9.setGeometry(QtCore.QRect(280, 300, 141, 31))
		self.pbProgram4_9.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_9.setProperty("value", 24)
		self.pbProgram4_9.setObjectName("pbProgram4_9")
		self.lblName4_9 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_9.setGeometry(QtCore.QRect(280, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_9.setFont(font)
		self.lblName4_9.setObjectName("lblName4_9")
		self.chkSel4_9 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_9.setGeometry(QtCore.QRect(260, 250, 86, 20))
		self.chkSel4_9.setText("")
		self.chkSel4_9.setObjectName("chkSel4_9")
		self.cmdDisplay4_10 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_10.setGeometry(QtCore.QRect(470, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_10.setFont(font)
		self.cmdDisplay4_10.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_10.setFlat(True)
		self.cmdDisplay4_10.setObjectName("cmdDisplay4_10")
		self.pbProgram4_10 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_10.setGeometry(QtCore.QRect(470, 300, 141, 31))
		self.pbProgram4_10.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_10.setProperty("value", 24)
		self.pbProgram4_10.setObjectName("pbProgram4_10")
		self.lblName4_10 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_10.setGeometry(QtCore.QRect(470, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_10.setFont(font)
		self.lblName4_10.setObjectName("lblName4_10")
		self.chkSel4_10 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_10.setGeometry(QtCore.QRect(450, 250, 86, 20))
		self.chkSel4_10.setText("")
		self.chkSel4_10.setObjectName("chkSel4_10")
		self.cmdDisplay4_11 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_11.setGeometry(QtCore.QRect(660, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_11.setFont(font)
		self.cmdDisplay4_11.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_11.setFlat(True)
		self.cmdDisplay4_11.setObjectName("cmdDisplay4_11")
		self.pbProgram4_11 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_11.setGeometry(QtCore.QRect(660, 300, 141, 31))
		self.pbProgram4_11.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_11.setProperty("value", 24)
		self.pbProgram4_11.setObjectName("pbProgram4_11")
		self.lblName4_11 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_11.setGeometry(QtCore.QRect(660, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_11.setFont(font)
		self.lblName4_11.setObjectName("lblName4_11")
		self.chkSel4_11 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_11.setGeometry(QtCore.QRect(640, 250, 86, 20))
		self.chkSel4_11.setText("")
		self.chkSel4_11.setObjectName("chkSel4_11")
		self.cmdDisplay4_12 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_12.setGeometry(QtCore.QRect(850, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_12.setFont(font)
		self.cmdDisplay4_12.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_12.setFlat(True)
		self.cmdDisplay4_12.setObjectName("cmdDisplay4_12")
		self.pbProgram4_12 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_12.setGeometry(QtCore.QRect(850, 300, 141, 31))
		self.pbProgram4_12.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_12.setProperty("value", 24)
		self.pbProgram4_12.setObjectName("pbProgram4_12")
		self.lblName4_12 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_12.setGeometry(QtCore.QRect(850, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_12.setFont(font)
		self.lblName4_12.setObjectName("lblName4_12")
		self.chkSel4_12 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_12.setGeometry(QtCore.QRect(830, 250, 86, 20))
		self.chkSel4_12.setText("")
		self.chkSel4_12.setObjectName("chkSel4_12")
		self.cmdDisplay4_13 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_13.setGeometry(QtCore.QRect(1040, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_13.setFont(font)
		self.cmdDisplay4_13.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_13.setFlat(True)
		self.cmdDisplay4_13.setObjectName("cmdDisplay4_13")
		self.pbProgram4_13 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_13.setGeometry(QtCore.QRect(1040, 300, 141, 31))
		self.pbProgram4_13.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_13.setProperty("value", 24)
		self.pbProgram4_13.setObjectName("pbProgram4_13")
		self.lblName4_13 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_13.setGeometry(QtCore.QRect(1040, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_13.setFont(font)
		self.lblName4_13.setObjectName("lblName4_13")
		self.chkSel4_13 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_13.setGeometry(QtCore.QRect(1020, 250, 86, 20))
		self.chkSel4_13.setText("")
		self.chkSel4_13.setObjectName("chkSel4_13")
		self.cmdDisplay4_14 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_14.setGeometry(QtCore.QRect(1230, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_14.setFont(font)
		self.cmdDisplay4_14.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_14.setFlat(True)
		self.cmdDisplay4_14.setObjectName("cmdDisplay4_14")
		self.pbProgram4_14 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_14.setGeometry(QtCore.QRect(1230, 300, 141, 31))
		self.pbProgram4_14.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_14.setProperty("value", 24)
		self.pbProgram4_14.setObjectName("pbProgram4_14")
		self.lblName4_14 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_14.setGeometry(QtCore.QRect(1230, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_14.setFont(font)
		self.lblName4_14.setObjectName("lblName4_14")
		self.chkSel4_14 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_14.setGeometry(QtCore.QRect(1210, 250, 86, 20))
		self.chkSel4_14.setText("")
		self.chkSel4_14.setObjectName("chkSel4_14")
		self.cmdDisplay4_15 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_15.setGeometry(QtCore.QRect(90, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_15.setFont(font)
		self.cmdDisplay4_15.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_15.setFlat(True)
		self.cmdDisplay4_15.setObjectName("cmdDisplay4_15")
		self.pbProgram4_15 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_15.setGeometry(QtCore.QRect(90, 430, 141, 31))
		self.pbProgram4_15.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_15.setProperty("value", 24)
		self.pbProgram4_15.setObjectName("pbProgram4_15")
		self.lblName4_15 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_15.setGeometry(QtCore.QRect(90, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_15.setFont(font)
		self.lblName4_15.setObjectName("lblName4_15")
		self.chkSel4_15 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_15.setGeometry(QtCore.QRect(70, 380, 86, 20))
		self.chkSel4_15.setText("")
		self.chkSel4_15.setObjectName("chkSel4_15")
		self.cmdDisplay4_16 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_16.setGeometry(QtCore.QRect(280, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_16.setFont(font)
		self.cmdDisplay4_16.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_16.setFlat(True)
		self.cmdDisplay4_16.setObjectName("cmdDisplay4_16")
		self.pbProgram4_16 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_16.setGeometry(QtCore.QRect(280, 430, 141, 31))
		self.pbProgram4_16.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_16.setProperty("value", 24)
		self.pbProgram4_16.setObjectName("pbProgram4_16")
		self.lblName4_16 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_16.setGeometry(QtCore.QRect(280, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_16.setFont(font)
		self.lblName4_16.setObjectName("lblName4_16")
		self.chkSel4_16 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_16.setGeometry(QtCore.QRect(260, 380, 86, 20))
		self.chkSel4_16.setText("")
		self.chkSel4_16.setObjectName("chkSel4_16")
		self.cmdDisplay4_17 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_17.setGeometry(QtCore.QRect(470, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_17.setFont(font)
		self.cmdDisplay4_17.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_17.setFlat(True)
		self.cmdDisplay4_17.setObjectName("cmdDisplay4_17")
		self.pbProgram4_17 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_17.setGeometry(QtCore.QRect(470, 430, 141, 31))
		self.pbProgram4_17.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_17.setProperty("value", 24)
		self.pbProgram4_17.setObjectName("pbProgram4_17")
		self.lblName4_17 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_17.setGeometry(QtCore.QRect(470, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_17.setFont(font)
		self.lblName4_17.setObjectName("lblName4_17")
		self.chkSel4_17 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_17.setGeometry(QtCore.QRect(450, 380, 86, 20))
		self.chkSel4_17.setText("")
		self.chkSel4_17.setObjectName("chkSel4_17")
		self.cmdDisplay4_18 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_18.setGeometry(QtCore.QRect(660, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_18.setFont(font)
		self.cmdDisplay4_18.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_18.setFlat(True)
		self.cmdDisplay4_18.setObjectName("cmdDisplay4_18")
		self.pbProgram4_18 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_18.setGeometry(QtCore.QRect(660, 430, 141, 31))
		self.pbProgram4_18.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_18.setProperty("value", 24)
		self.pbProgram4_18.setObjectName("pbProgram4_18")
		self.lblName4_18 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_18.setGeometry(QtCore.QRect(660, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_18.setFont(font)
		self.lblName4_18.setObjectName("lblName4_18")
		self.chkSel4_18 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_18.setGeometry(QtCore.QRect(640, 380, 86, 20))
		self.chkSel4_18.setText("")
		self.chkSel4_18.setObjectName("chkSel4_18")
		self.cmdDisplay4_19 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_19.setGeometry(QtCore.QRect(850, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_19.setFont(font)
		self.cmdDisplay4_19.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_19.setFlat(True)
		self.cmdDisplay4_19.setObjectName("cmdDisplay4_19")
		self.pbProgram4_19 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_19.setGeometry(QtCore.QRect(850, 430, 141, 31))
		self.pbProgram4_19.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_19.setProperty("value", 24)
		self.pbProgram4_19.setObjectName("pbProgram4_19")
		self.lblName4_19 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_19.setGeometry(QtCore.QRect(850, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_19.setFont(font)
		self.lblName4_19.setObjectName("lblName4_19")
		self.chkSel4_19 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_19.setGeometry(QtCore.QRect(830, 380, 86, 20))
		self.chkSel4_19.setText("")
		self.chkSel4_19.setObjectName("chkSel4_19")
		self.cmdDisplay4_20 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_20.setGeometry(QtCore.QRect(1040, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_20.setFont(font)
		self.cmdDisplay4_20.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_20.setFlat(True)
		self.cmdDisplay4_20.setObjectName("cmdDisplay4_20")
		self.pbProgram4_20 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_20.setGeometry(QtCore.QRect(1040, 430, 141, 31))
		self.pbProgram4_20.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_20.setProperty("value", 24)
		self.pbProgram4_20.setObjectName("pbProgram4_20")
		self.lblName4_20 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_20.setGeometry(QtCore.QRect(1040, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_20.setFont(font)
		self.lblName4_20.setObjectName("lblName4_20")
		self.chkSel4_20 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_20.setGeometry(QtCore.QRect(1020, 380, 86, 20))
		self.chkSel4_20.setText("")
		self.chkSel4_20.setObjectName("chkSel4_20")
		self.cmdDisplay4_21 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_21.setGeometry(QtCore.QRect(1230, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_21.setFont(font)
		self.cmdDisplay4_21.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_21.setFlat(True)
		self.cmdDisplay4_21.setObjectName("cmdDisplay4_21")
		self.pbProgram4_21 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_21.setGeometry(QtCore.QRect(1230, 430, 141, 31))
		self.pbProgram4_21.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_21.setProperty("value", 24)
		self.pbProgram4_21.setObjectName("pbProgram4_21")
		self.lblName4_21 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_21.setGeometry(QtCore.QRect(1230, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_21.setFont(font)
		self.lblName4_21.setObjectName("lblName4_21")
		self.chkSel4_21 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_21.setGeometry(QtCore.QRect(1210, 380, 86, 20))
		self.chkSel4_21.setText("")
		self.chkSel4_21.setObjectName("chkSel4_21")
		self.cmdDisplay4_22 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_22.setGeometry(QtCore.QRect(90, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_22.setFont(font)
		self.cmdDisplay4_22.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_22.setFlat(True)
		self.cmdDisplay4_22.setObjectName("cmdDisplay4_22")
		self.pbProgram4_22 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_22.setGeometry(QtCore.QRect(90, 560, 141, 31))
		self.pbProgram4_22.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_22.setProperty("value", 24)
		self.pbProgram4_22.setObjectName("pbProgram4_22")
		self.lblName4_22 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_22.setGeometry(QtCore.QRect(90, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_22.setFont(font)
		self.lblName4_22.setObjectName("lblName4_22")
		self.chkSel4_22 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_22.setGeometry(QtCore.QRect(70, 510, 86, 20))
		self.chkSel4_22.setText("")
		self.chkSel4_22.setObjectName("chkSel4_22")
		self.cmdDisplay4_23 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_23.setGeometry(QtCore.QRect(280, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_23.setFont(font)
		self.cmdDisplay4_23.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_23.setFlat(True)
		self.cmdDisplay4_23.setObjectName("cmdDisplay4_23")
		self.pbProgram4_23 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_23.setGeometry(QtCore.QRect(280, 560, 141, 31))
		self.pbProgram4_23.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_23.setProperty("value", 24)
		self.pbProgram4_23.setObjectName("pbProgram4_23")
		self.lblName4_23 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_23.setGeometry(QtCore.QRect(280, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_23.setFont(font)
		self.lblName4_23.setObjectName("lblName4_23")
		self.chkSel4_23 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_23.setGeometry(QtCore.QRect(260, 510, 86, 20))
		self.chkSel4_23.setText("")
		self.chkSel4_23.setObjectName("chkSel4_23")
		self.cmdDisplay4_24 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_24.setGeometry(QtCore.QRect(470, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_24.setFont(font)
		self.cmdDisplay4_24.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_24.setFlat(True)
		self.cmdDisplay4_24.setObjectName("cmdDisplay4_24")
		self.pbProgram4_24 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_24.setGeometry(QtCore.QRect(470, 560, 141, 31))
		self.pbProgram4_24.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_24.setProperty("value", 24)
		self.pbProgram4_24.setObjectName("pbProgram4_24")
		self.lblName4_24 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_24.setGeometry(QtCore.QRect(470, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_24.setFont(font)
		self.lblName4_24.setObjectName("lblName4_24")
		self.chkSel4_24 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_24.setGeometry(QtCore.QRect(450, 510, 86, 20))
		self.chkSel4_24.setText("")
		self.chkSel4_24.setObjectName("chkSel4_24")
		self.cmdDisplay4_25 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_25.setGeometry(QtCore.QRect(660, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_25.setFont(font)
		self.cmdDisplay4_25.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_25.setFlat(True)
		self.cmdDisplay4_25.setObjectName("cmdDisplay4_25")
		self.pbProgram4_25 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_25.setGeometry(QtCore.QRect(660, 560, 141, 31))
		self.pbProgram4_25.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_25.setProperty("value", 24)
		self.pbProgram4_25.setObjectName("pbProgram4_25")
		self.lblName4_25 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_25.setGeometry(QtCore.QRect(660, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_25.setFont(font)
		self.lblName4_25.setObjectName("lblName4_25")
		self.chkSel4_25 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_25.setGeometry(QtCore.QRect(640, 510, 86, 20))
		self.chkSel4_25.setText("")
		self.chkSel4_25.setObjectName("chkSel4_25")
		self.cmdDisplay4_26 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_26.setGeometry(QtCore.QRect(850, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_26.setFont(font)
		self.cmdDisplay4_26.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_26.setFlat(True)
		self.cmdDisplay4_26.setObjectName("cmdDisplay4_26")
		self.pbProgram4_26 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_26.setGeometry(QtCore.QRect(850, 560, 141, 31))
		self.pbProgram4_26.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_26.setProperty("value", 24)
		self.pbProgram4_26.setObjectName("pbProgram4_26")
		self.lblName4_26 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_26.setGeometry(QtCore.QRect(850, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_26.setFont(font)
		self.lblName4_26.setObjectName("lblName4_26")
		self.chkSel4_26 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_26.setGeometry(QtCore.QRect(830, 510, 86, 20))
		self.chkSel4_26.setText("")
		self.chkSel4_26.setObjectName("chkSel4_26")
		self.cmdDisplay4_27 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_27.setGeometry(QtCore.QRect(1040, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_27.setFont(font)
		self.cmdDisplay4_27.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_27.setFlat(True)
		self.cmdDisplay4_27.setObjectName("cmdDisplay4_27")
		self.pbProgram4_27 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_27.setGeometry(QtCore.QRect(1040, 560, 141, 31))
		self.pbProgram4_27.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_27.setProperty("value", 24)
		self.pbProgram4_27.setObjectName("pbProgram4_27")
		self.lblName4_27 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_27.setGeometry(QtCore.QRect(1040, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_27.setFont(font)
		self.lblName4_27.setObjectName("lblName4_27")
		self.chkSel4_27 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_27.setGeometry(QtCore.QRect(1020, 510, 86, 20))
		self.chkSel4_27.setText("")
		self.chkSel4_27.setObjectName("chkSel4_27")
		self.chkSel4_28 = QtWidgets.QCheckBox(self.tbPage4)
		self.chkSel4_28.setGeometry(QtCore.QRect(1210, 510, 86, 20))
		self.chkSel4_28.setText("")
		self.chkSel4_28.setObjectName("chkSel4_28")
		self.cmdDisplay4_28 = QtWidgets.QPushButton(self.tbPage4)
		self.cmdDisplay4_28.setGeometry(QtCore.QRect(1230, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay4_28.setFont(font)
		self.cmdDisplay4_28.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay4_28.setFlat(True)
		self.cmdDisplay4_28.setObjectName("cmdDisplay4_28")
		self.lblName4_28 = QtWidgets.QLabel(self.tbPage4)
		self.lblName4_28.setGeometry(QtCore.QRect(1230, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName4_28.setFont(font)
		self.lblName4_28.setObjectName("lblName4_28")
		self.pbProgram4_28 = QtWidgets.QProgressBar(self.tbPage4)
		self.pbProgram4_28.setGeometry(QtCore.QRect(1230, 560, 141, 31))
		self.pbProgram4_28.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram4_28.setProperty("value", 24)
		self.pbProgram4_28.setObjectName("pbProgram4_28")
		self.tabWidget.addTab(self.tbPage4, "")
		self.tbPage5 = QtWidgets.QWidget()
		self.tbPage5.setObjectName("tbPage5")
		self.lblPage5 = QtWidgets.QLabel(self.tbPage5)
		self.lblPage5.setGeometry(QtCore.QRect(40, 30, 671, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.lblPage5.setFont(font)
		self.lblPage5.setObjectName("lblPage5")
		self.cmdDisplay5_1 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_1.setGeometry(QtCore.QRect(90, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_1.setFont(font)
		self.cmdDisplay5_1.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_1.setFlat(True)
		self.cmdDisplay5_1.setObjectName("cmdDisplay5_1")
		self.pbProgram5_1 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_1.setGeometry(QtCore.QRect(90, 170, 141, 31))
		self.pbProgram5_1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_1.setProperty("value", 24)
		self.pbProgram5_1.setObjectName("pbProgram5_1")
		self.lblName5_1 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_1.setGeometry(QtCore.QRect(90, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_1.setFont(font)
		self.lblName5_1.setObjectName("lblName5_1")
		self.chkSel5_1 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_1.setGeometry(QtCore.QRect(70, 120, 86, 20))
		self.chkSel5_1.setText("")
		self.chkSel5_1.setObjectName("chkSel5_1")
		self.chkSel5_2 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_2.setGeometry(QtCore.QRect(260, 120, 86, 20))
		self.chkSel5_2.setText("")
		self.chkSel5_2.setObjectName("chkSel5_2")
		self.pbProgram5_2 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_2.setGeometry(QtCore.QRect(280, 170, 141, 31))
		self.pbProgram5_2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_2.setProperty("value", 24)
		self.pbProgram5_2.setObjectName("pbProgram5_2")
		self.lblName5_2 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_2.setGeometry(QtCore.QRect(280, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_2.setFont(font)
		self.lblName5_2.setObjectName("lblName5_2")
		self.cmdDisplay5_2 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_2.setGeometry(QtCore.QRect(280, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_2.setFont(font)
		self.cmdDisplay5_2.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_2.setFlat(True)
		self.cmdDisplay5_2.setObjectName("cmdDisplay5_2")
		self.chkSel5_3 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_3.setGeometry(QtCore.QRect(450, 120, 86, 20))
		self.chkSel5_3.setText("")
		self.chkSel5_3.setObjectName("chkSel5_3")
		self.pbProgram5_3 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
		self.pbProgram5_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_3.setProperty("value", 24)
		self.pbProgram5_3.setObjectName("pbProgram5_3")
		self.lblName5_3 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_3.setGeometry(QtCore.QRect(470, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_3.setFont(font)
		self.lblName5_3.setObjectName("lblName5_3")
		self.cmdDisplay5_3 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_3.setGeometry(QtCore.QRect(470, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_3.setFont(font)
		self.cmdDisplay5_3.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_3.setFlat(True)
		self.cmdDisplay5_3.setObjectName("cmdDisplay5_3")
		self.chkSel5_4 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_4.setGeometry(QtCore.QRect(640, 120, 86, 20))
		self.chkSel5_4.setText("")
		self.chkSel5_4.setObjectName("chkSel5_4")
		self.pbProgram5_4 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_4.setGeometry(QtCore.QRect(660, 170, 141, 31))
		self.pbProgram5_4.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_4.setProperty("value", 24)
		self.pbProgram5_4.setObjectName("pbProgram5_4")
		self.lblName5_4 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_4.setGeometry(QtCore.QRect(660, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_4.setFont(font)
		self.lblName5_4.setObjectName("lblName5_4")
		self.cmdDisplay5_4 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_4.setGeometry(QtCore.QRect(660, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_4.setFont(font)
		self.cmdDisplay5_4.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_4.setFlat(True)
		self.cmdDisplay5_4.setObjectName("cmdDisplay5_4")
		self.chkSel5_5 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_5.setGeometry(QtCore.QRect(830, 120, 86, 20))
		self.chkSel5_5.setText("")
		self.chkSel5_5.setObjectName("chkSel5_5")
		self.pbProgram5_5 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_5.setGeometry(QtCore.QRect(850, 170, 141, 31))
		self.pbProgram5_5.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_5.setProperty("value", 24)
		self.pbProgram5_5.setObjectName("pbProgram5_5")
		self.lblName5_5 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_5.setGeometry(QtCore.QRect(850, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_5.setFont(font)
		self.lblName5_5.setObjectName("lblName5_5")
		self.cmdDisplay5_5 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_5.setGeometry(QtCore.QRect(850, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_5.setFont(font)
		self.cmdDisplay5_5.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_5.setFlat(True)
		self.cmdDisplay5_5.setObjectName("cmdDisplay5_5")
		self.chkSel5_6 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_6.setGeometry(QtCore.QRect(1020, 120, 86, 20))
		self.chkSel5_6.setText("")
		self.chkSel5_6.setObjectName("chkSel5_6")
		self.pbProgram5_6 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_6.setGeometry(QtCore.QRect(1040, 170, 141, 31))
		self.pbProgram5_6.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_6.setProperty("value", 24)
		self.pbProgram5_6.setObjectName("pbProgram5_6")
		self.lblName5_6 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_6.setGeometry(QtCore.QRect(1040, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_6.setFont(font)
		self.lblName5_6.setObjectName("lblName5_6")
		self.cmdDisplay5_6 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_6.setGeometry(QtCore.QRect(1040, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_6.setFont(font)
		self.cmdDisplay5_6.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_6.setFlat(True)
		self.cmdDisplay5_6.setObjectName("cmdDisplay5_6")
		self.chkSel5_7 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_7.setGeometry(QtCore.QRect(1210, 120, 86, 20))
		self.chkSel5_7.setText("")
		self.chkSel5_7.setObjectName("chkSel5_7")
		self.pbProgram5_7 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_7.setGeometry(QtCore.QRect(1230, 170, 141, 31))
		self.pbProgram5_7.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_7.setProperty("value", 24)
		self.pbProgram5_7.setObjectName("pbProgram5_7")
		self.lblName5_7 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_7.setGeometry(QtCore.QRect(1230, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_7.setFont(font)
		self.lblName5_7.setObjectName("lblName5_7")
		self.cmdDisplay5_7 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_7.setGeometry(QtCore.QRect(1230, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_7.setFont(font)
		self.cmdDisplay5_7.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_7.setFlat(True)
		self.cmdDisplay5_7.setObjectName("cmdDisplay5_7")
		self.chkSel5_8 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_8.setGeometry(QtCore.QRect(70, 250, 86, 20))
		self.chkSel5_8.setText("")
		self.chkSel5_8.setObjectName("chkSel5_8")
		self.pbProgram5_8 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_8.setGeometry(QtCore.QRect(90, 300, 141, 31))
		self.pbProgram5_8.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_8.setProperty("value", 24)
		self.pbProgram5_8.setObjectName("pbProgram5_8")
		self.lblName5_8 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_8.setGeometry(QtCore.QRect(90, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_8.setFont(font)
		self.lblName5_8.setObjectName("lblName5_8")
		self.cmdDisplay5_8 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_8.setGeometry(QtCore.QRect(90, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_8.setFont(font)
		self.cmdDisplay5_8.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_8.setFlat(True)
		self.cmdDisplay5_8.setObjectName("cmdDisplay5_8")
		self.chkSel5_9 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_9.setGeometry(QtCore.QRect(260, 250, 86, 20))
		self.chkSel5_9.setText("")
		self.chkSel5_9.setObjectName("chkSel5_9")
		self.pbProgram5_9 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_9.setGeometry(QtCore.QRect(280, 300, 141, 31))
		self.pbProgram5_9.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_9.setProperty("value", 24)
		self.pbProgram5_9.setObjectName("pbProgram5_9")
		self.lblName5_9 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_9.setGeometry(QtCore.QRect(280, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_9.setFont(font)
		self.lblName5_9.setObjectName("lblName5_9")
		self.cmdDisplay5_9 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_9.setGeometry(QtCore.QRect(280, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_9.setFont(font)
		self.cmdDisplay5_9.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_9.setFlat(True)
		self.cmdDisplay5_9.setObjectName("cmdDisplay5_9")
		self.chkSel5_10 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_10.setGeometry(QtCore.QRect(450, 250, 86, 20))
		self.chkSel5_10.setText("")
		self.chkSel5_10.setObjectName("chkSel5_10")
		self.pbProgram5_10 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_10.setGeometry(QtCore.QRect(470, 300, 141, 31))
		self.pbProgram5_10.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_10.setProperty("value", 24)
		self.pbProgram5_10.setObjectName("pbProgram5_10")
		self.lblName5_10 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_10.setGeometry(QtCore.QRect(470, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_10.setFont(font)
		self.lblName5_10.setObjectName("lblName5_10")
		self.cmdDisplay5_10 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_10.setGeometry(QtCore.QRect(470, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_10.setFont(font)
		self.cmdDisplay5_10.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_10.setFlat(True)
		self.cmdDisplay5_10.setObjectName("cmdDisplay5_10")
		self.chkSel5_11 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_11.setGeometry(QtCore.QRect(640, 250, 86, 20))
		self.chkSel5_11.setText("")
		self.chkSel5_11.setObjectName("chkSel5_11")
		self.pbProgram5_11 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_11.setGeometry(QtCore.QRect(660, 300, 141, 31))
		self.pbProgram5_11.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_11.setProperty("value", 24)
		self.pbProgram5_11.setObjectName("pbProgram5_11")
		self.lblName5_11 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_11.setGeometry(QtCore.QRect(660, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_11.setFont(font)
		self.lblName5_11.setObjectName("lblName5_11")
		self.cmdDisplay5_11 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_11.setGeometry(QtCore.QRect(660, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_11.setFont(font)
		self.cmdDisplay5_11.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_11.setFlat(True)
		self.cmdDisplay5_11.setObjectName("cmdDisplay5_11")
		self.chkSel5_12 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_12.setGeometry(QtCore.QRect(830, 250, 86, 20))
		self.chkSel5_12.setText("")
		self.chkSel5_12.setObjectName("chkSel5_12")
		self.pbProgram5_12 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_12.setGeometry(QtCore.QRect(850, 300, 141, 31))
		self.pbProgram5_12.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_12.setProperty("value", 24)
		self.pbProgram5_12.setObjectName("pbProgram5_12")
		self.lblName5_12 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_12.setGeometry(QtCore.QRect(850, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_12.setFont(font)
		self.lblName5_12.setObjectName("lblName5_12")
		self.cmdDisplay5_12 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_12.setGeometry(QtCore.QRect(850, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_12.setFont(font)
		self.cmdDisplay5_12.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_12.setFlat(True)
		self.cmdDisplay5_12.setObjectName("cmdDisplay5_12")
		self.chkSel5_13 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_13.setGeometry(QtCore.QRect(1020, 250, 86, 20))
		self.chkSel5_13.setText("")
		self.chkSel5_13.setObjectName("chkSel5_13")
		self.pbProgram5_13 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_13.setGeometry(QtCore.QRect(1040, 300, 141, 31))
		self.pbProgram5_13.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_13.setProperty("value", 24)
		self.pbProgram5_13.setObjectName("pbProgram5_13")
		self.lblName5_13 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_13.setGeometry(QtCore.QRect(1040, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_13.setFont(font)
		self.lblName5_13.setObjectName("lblName5_13")
		self.cmdDisplay5_13 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_13.setGeometry(QtCore.QRect(1040, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_13.setFont(font)
		self.cmdDisplay5_13.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_13.setFlat(True)
		self.cmdDisplay5_13.setObjectName("cmdDisplay5_13")
		self.chkSel5_14 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_14.setGeometry(QtCore.QRect(1210, 250, 86, 20))
		self.chkSel5_14.setText("")
		self.chkSel5_14.setObjectName("chkSel5_14")
		self.pbProgram5_14 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_14.setGeometry(QtCore.QRect(1230, 300, 141, 31))
		self.pbProgram5_14.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_14.setProperty("value", 24)
		self.pbProgram5_14.setObjectName("pbProgram5_14")
		self.lblName5_14 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_14.setGeometry(QtCore.QRect(1230, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_14.setFont(font)
		self.lblName5_14.setObjectName("lblName5_14")
		self.cmdDisplay5_14 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_14.setGeometry(QtCore.QRect(1230, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_14.setFont(font)
		self.cmdDisplay5_14.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_14.setFlat(True)
		self.cmdDisplay5_14.setObjectName("cmdDisplay5_14")
		self.chkSel5_15 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_15.setGeometry(QtCore.QRect(70, 380, 86, 20))
		self.chkSel5_15.setText("")
		self.chkSel5_15.setObjectName("chkSel5_15")
		self.pbProgram5_15 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_15.setGeometry(QtCore.QRect(90, 430, 141, 31))
		self.pbProgram5_15.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_15.setProperty("value", 24)
		self.pbProgram5_15.setObjectName("pbProgram5_15")
		self.lblName5_15 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_15.setGeometry(QtCore.QRect(90, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_15.setFont(font)
		self.lblName5_15.setObjectName("lblName5_15")
		self.cmdDisplay5_15 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_15.setGeometry(QtCore.QRect(90, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_15.setFont(font)
		self.cmdDisplay5_15.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_15.setFlat(True)
		self.cmdDisplay5_15.setObjectName("cmdDisplay5_15")
		self.chkSel5_16 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_16.setGeometry(QtCore.QRect(260, 380, 86, 20))
		self.chkSel5_16.setText("")
		self.chkSel5_16.setObjectName("chkSel5_16")
		self.pbProgram5_16 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_16.setGeometry(QtCore.QRect(280, 430, 141, 31))
		self.pbProgram5_16.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_16.setProperty("value", 24)
		self.pbProgram5_16.setObjectName("pbProgram5_16")
		self.lblName5_16 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_16.setGeometry(QtCore.QRect(280, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_16.setFont(font)
		self.lblName5_16.setObjectName("lblName5_16")
		self.cmdDisplay5_16 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_16.setGeometry(QtCore.QRect(280, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_16.setFont(font)
		self.cmdDisplay5_16.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_16.setFlat(True)
		self.cmdDisplay5_16.setObjectName("cmdDisplay5_16")
		self.chkSel5_17 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_17.setGeometry(QtCore.QRect(450, 380, 86, 20))
		self.chkSel5_17.setText("")
		self.chkSel5_17.setObjectName("chkSel5_17")
		self.pbProgram5_17 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_17.setGeometry(QtCore.QRect(470, 430, 141, 31))
		self.pbProgram5_17.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_17.setProperty("value", 24)
		self.pbProgram5_17.setObjectName("pbProgram5_17")
		self.lblName5_17 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_17.setGeometry(QtCore.QRect(470, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_17.setFont(font)
		self.lblName5_17.setObjectName("lblName5_17")
		self.cmdDisplay5_17 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_17.setGeometry(QtCore.QRect(470, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_17.setFont(font)
		self.cmdDisplay5_17.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_17.setFlat(True)
		self.cmdDisplay5_17.setObjectName("cmdDisplay5_17")
		self.chkSel5_18 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_18.setGeometry(QtCore.QRect(640, 380, 86, 20))
		self.chkSel5_18.setText("")
		self.chkSel5_18.setObjectName("chkSel5_18")
		self.pbProgram5_18 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_18.setGeometry(QtCore.QRect(660, 430, 141, 31))
		self.pbProgram5_18.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_18.setProperty("value", 24)
		self.pbProgram5_18.setObjectName("pbProgram5_18")
		self.lblName5_18 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_18.setGeometry(QtCore.QRect(660, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_18.setFont(font)
		self.lblName5_18.setObjectName("lblName5_18")
		self.cmdDisplay5_18 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_18.setGeometry(QtCore.QRect(660, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_18.setFont(font)
		self.cmdDisplay5_18.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_18.setFlat(True)
		self.cmdDisplay5_18.setObjectName("cmdDisplay5_18")
		self.chkSel5_19 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_19.setGeometry(QtCore.QRect(830, 380, 86, 20))
		self.chkSel5_19.setText("")
		self.chkSel5_19.setObjectName("chkSel5_19")
		self.pbProgram5_19 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_19.setGeometry(QtCore.QRect(850, 430, 141, 31))
		self.pbProgram5_19.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_19.setProperty("value", 24)
		self.pbProgram5_19.setObjectName("pbProgram5_19")
		self.lblName5_19 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_19.setGeometry(QtCore.QRect(850, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_19.setFont(font)
		self.lblName5_19.setObjectName("lblName5_19")
		self.cmdDisplay5_19 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_19.setGeometry(QtCore.QRect(850, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_19.setFont(font)
		self.cmdDisplay5_19.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_19.setFlat(True)
		self.cmdDisplay5_19.setObjectName("cmdDisplay5_19")
		self.chkSel5_20 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_20.setGeometry(QtCore.QRect(1020, 380, 86, 20))
		self.chkSel5_20.setText("")
		self.chkSel5_20.setObjectName("chkSel5_20")
		self.pbProgram5_20 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_20.setGeometry(QtCore.QRect(1040, 430, 141, 31))
		self.pbProgram5_20.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_20.setProperty("value", 24)
		self.pbProgram5_20.setObjectName("pbProgram5_20")
		self.lblName5_20 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_20.setGeometry(QtCore.QRect(1040, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_20.setFont(font)
		self.lblName5_20.setObjectName("lblName5_20")
		self.cmdDisplay5_20 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_20.setGeometry(QtCore.QRect(1040, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_20.setFont(font)
		self.cmdDisplay5_20.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_20.setFlat(True)
		self.cmdDisplay5_20.setObjectName("cmdDisplay5_20")
		self.chkSel5_21 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_21.setGeometry(QtCore.QRect(1210, 380, 86, 20))
		self.chkSel5_21.setText("")
		self.chkSel5_21.setObjectName("chkSel5_21")
		self.pbProgram5_21 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_21.setGeometry(QtCore.QRect(1230, 430, 141, 31))
		self.pbProgram5_21.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_21.setProperty("value", 24)
		self.pbProgram5_21.setObjectName("pbProgram5_21")
		self.lblName5_21 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_21.setGeometry(QtCore.QRect(1230, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_21.setFont(font)
		self.lblName5_21.setObjectName("lblName5_21")
		self.cmdDisplay5_21 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_21.setGeometry(QtCore.QRect(1230, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_21.setFont(font)
		self.cmdDisplay5_21.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_21.setFlat(True)
		self.cmdDisplay5_21.setObjectName("cmdDisplay5_21")
		self.chkSel5_22 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_22.setGeometry(QtCore.QRect(70, 510, 86, 20))
		self.chkSel5_22.setText("")
		self.chkSel5_22.setObjectName("chkSel5_22")
		self.pbProgram5_22 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_22.setGeometry(QtCore.QRect(90, 560, 141, 31))
		self.pbProgram5_22.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_22.setProperty("value", 24)
		self.pbProgram5_22.setObjectName("pbProgram5_22")
		self.lblName5_22 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_22.setGeometry(QtCore.QRect(90, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_22.setFont(font)
		self.lblName5_22.setObjectName("lblName5_22")
		self.cmdDisplay5_22 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_22.setGeometry(QtCore.QRect(90, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_22.setFont(font)
		self.cmdDisplay5_22.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_22.setFlat(True)
		self.cmdDisplay5_22.setObjectName("cmdDisplay5_22")
		self.chkSel5_23 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_23.setGeometry(QtCore.QRect(260, 510, 86, 20))
		self.chkSel5_23.setText("")
		self.chkSel5_23.setObjectName("chkSel5_23")
		self.pbProgram5_23 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_23.setGeometry(QtCore.QRect(280, 560, 141, 31))
		self.pbProgram5_23.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_23.setProperty("value", 24)
		self.pbProgram5_23.setObjectName("pbProgram5_23")
		self.lblName5_23 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_23.setGeometry(QtCore.QRect(280, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_23.setFont(font)
		self.lblName5_23.setObjectName("lblName5_23")
		self.cmdDisplay5_23 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_23.setGeometry(QtCore.QRect(280, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_23.setFont(font)
		self.cmdDisplay5_23.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_23.setFlat(True)
		self.cmdDisplay5_23.setObjectName("cmdDisplay5_23")
		self.chkSel5_24 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_24.setGeometry(QtCore.QRect(450, 510, 86, 20))
		self.chkSel5_24.setText("")
		self.chkSel5_24.setObjectName("chkSel5_24")
		self.pbProgram5_24 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_24.setGeometry(QtCore.QRect(470, 560, 141, 31))
		self.pbProgram5_24.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_24.setProperty("value", 24)
		self.pbProgram5_24.setObjectName("pbProgram5_24")
		self.lblName5_24 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_24.setGeometry(QtCore.QRect(470, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_24.setFont(font)
		self.lblName5_24.setObjectName("lblName5_24")
		self.cmdDisplay5_24 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_24.setGeometry(QtCore.QRect(470, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_24.setFont(font)
		self.cmdDisplay5_24.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_24.setFlat(True)
		self.cmdDisplay5_24.setObjectName("cmdDisplay5_24")
		self.chkSel5_25 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_25.setGeometry(QtCore.QRect(640, 510, 86, 20))
		self.chkSel5_25.setText("")
		self.chkSel5_25.setObjectName("chkSel5_25")
		self.pbProgram5_25 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_25.setGeometry(QtCore.QRect(660, 560, 141, 31))
		self.pbProgram5_25.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_25.setProperty("value", 24)
		self.pbProgram5_25.setObjectName("pbProgram5_25")
		self.lblName5_25 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_25.setGeometry(QtCore.QRect(660, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_25.setFont(font)
		self.lblName5_25.setObjectName("lblName5_25")
		self.cmdDisplay5_25 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_25.setGeometry(QtCore.QRect(660, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_25.setFont(font)
		self.cmdDisplay5_25.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_25.setFlat(True)
		self.cmdDisplay5_25.setObjectName("cmdDisplay5_25")
		self.chkSel5_26 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_26.setGeometry(QtCore.QRect(830, 510, 86, 20))
		self.chkSel5_26.setText("")
		self.chkSel5_26.setObjectName("chkSel5_26")
		self.pbProgram5_26 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_26.setGeometry(QtCore.QRect(850, 560, 141, 31))
		self.pbProgram5_26.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_26.setProperty("value", 24)
		self.pbProgram5_26.setObjectName("pbProgram5_26")
		self.lblName5_26 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_26.setGeometry(QtCore.QRect(850, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_26.setFont(font)
		self.lblName5_26.setObjectName("lblName5_26")
		self.cmdDisplay5_26 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_26.setGeometry(QtCore.QRect(850, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_26.setFont(font)
		self.cmdDisplay5_26.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_26.setFlat(True)
		self.cmdDisplay5_26.setObjectName("cmdDisplay5_26")
		self.chkSel5_27 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_27.setGeometry(QtCore.QRect(1020, 510, 86, 20))
		self.chkSel5_27.setText("")
		self.chkSel5_27.setObjectName("chkSel5_27")
		self.pbProgram5_27 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_27.setGeometry(QtCore.QRect(1040, 560, 141, 31))
		self.pbProgram5_27.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_27.setProperty("value", 24)
		self.pbProgram5_27.setObjectName("pbProgram5_27")
		self.lblName5_27 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_27.setGeometry(QtCore.QRect(1040, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_27.setFont(font)
		self.lblName5_27.setObjectName("lblName5_27")
		self.cmdDisplay5_27 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_27.setGeometry(QtCore.QRect(1040, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_27.setFont(font)
		self.cmdDisplay5_27.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_27.setFlat(True)
		self.cmdDisplay5_27.setObjectName("cmdDisplay5_27")
		self.chkSel5_28 = QtWidgets.QCheckBox(self.tbPage5)
		self.chkSel5_28.setGeometry(QtCore.QRect(1210, 510, 86, 20))
		self.chkSel5_28.setText("")
		self.chkSel5_28.setObjectName("chkSel5_28")
		self.pbProgram5_28 = QtWidgets.QProgressBar(self.tbPage5)
		self.pbProgram5_28.setGeometry(QtCore.QRect(1230, 560, 141, 31))
		self.pbProgram5_28.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram5_28.setProperty("value", 24)
		self.pbProgram5_28.setObjectName("pbProgram5_28")
		self.lblName5_28 = QtWidgets.QLabel(self.tbPage5)
		self.lblName5_28.setGeometry(QtCore.QRect(1230, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName5_28.setFont(font)
		self.lblName5_28.setObjectName("lblName5_28")
		self.cmdDisplay5_28 = QtWidgets.QPushButton(self.tbPage5)
		self.cmdDisplay5_28.setGeometry(QtCore.QRect(1230, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay5_28.setFont(font)
		self.cmdDisplay5_28.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay5_28.setFlat(True)
		self.cmdDisplay5_28.setObjectName("cmdDisplay5_28")
		self.tabWidget.addTab(self.tbPage5, "")
		self.tbPage6 = QtWidgets.QWidget()
		self.tbPage6.setObjectName("tbPage6")
		self.lblPage6 = QtWidgets.QLabel(self.tbPage6)
		self.lblPage6.setGeometry(QtCore.QRect(40, 30, 671, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.lblPage6.setFont(font)
		self.lblPage6.setObjectName("lblPage6")
		self.chkSel6_1 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_1.setGeometry(QtCore.QRect(70, 120, 86, 20))
		self.chkSel6_1.setText("")
		self.chkSel6_1.setObjectName("chkSel6_1")
		self.pbProgram6_1 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_1.setGeometry(QtCore.QRect(90, 170, 141, 31))
		self.pbProgram6_1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_1.setProperty("value", 24)
		self.pbProgram6_1.setObjectName("pbProgram6_1")
		self.lblName6_1 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_1.setGeometry(QtCore.QRect(90, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_1.setFont(font)
		self.lblName6_1.setObjectName("lblName6_1")
		self.cmdDisplay6_1 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_1.setGeometry(QtCore.QRect(90, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_1.setFont(font)
		self.cmdDisplay6_1.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_1.setFlat(True)
		self.cmdDisplay6_1.setObjectName("cmdDisplay6_1")
		self.lblName6_2 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_2.setGeometry(QtCore.QRect(280, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_2.setFont(font)
		self.lblName6_2.setObjectName("lblName6_2")
		self.chkSel6_2 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_2.setGeometry(QtCore.QRect(260, 120, 86, 20))
		self.chkSel6_2.setText("")
		self.chkSel6_2.setObjectName("chkSel6_2")
		self.cmdDisplay6_2 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_2.setGeometry(QtCore.QRect(280, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_2.setFont(font)
		self.cmdDisplay6_2.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_2.setFlat(True)
		self.cmdDisplay6_2.setObjectName("cmdDisplay6_2")
		self.pbProgram6_2 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_2.setGeometry(QtCore.QRect(280, 170, 141, 31))
		self.pbProgram6_2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_2.setProperty("value", 24)
		self.pbProgram6_2.setObjectName("pbProgram6_2")
		self.lblName6_3 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_3.setGeometry(QtCore.QRect(470, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_3.setFont(font)
		self.lblName6_3.setObjectName("lblName6_3")
		self.chkSel6_3 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_3.setGeometry(QtCore.QRect(450, 120, 86, 20))
		self.chkSel6_3.setText("")
		self.chkSel6_3.setObjectName("chkSel6_3")
		self.cmdDisplay6_3 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_3.setGeometry(QtCore.QRect(470, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_3.setFont(font)
		self.cmdDisplay6_3.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_3.setFlat(True)
		self.cmdDisplay6_3.setObjectName("cmdDisplay6_3")
		self.pbProgram6_3 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
		self.pbProgram6_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_3.setProperty("value", 24)
		self.pbProgram6_3.setObjectName("pbProgram6_3")
		self.lblName6_4 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_4.setGeometry(QtCore.QRect(660, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_4.setFont(font)
		self.lblName6_4.setObjectName("lblName6_4")
		self.chkSel6_4 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_4.setGeometry(QtCore.QRect(640, 120, 86, 20))
		self.chkSel6_4.setText("")
		self.chkSel6_4.setObjectName("chkSel6_4")
		self.cmdDisplay6_4 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_4.setGeometry(QtCore.QRect(660, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_4.setFont(font)
		self.cmdDisplay6_4.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_4.setFlat(True)
		self.cmdDisplay6_4.setObjectName("cmdDisplay6_4")
		self.pbProgram6_4 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_4.setGeometry(QtCore.QRect(660, 170, 141, 31))
		self.pbProgram6_4.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_4.setProperty("value", 24)
		self.pbProgram6_4.setObjectName("pbProgram6_4")
		self.lblName6_5 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_5.setGeometry(QtCore.QRect(850, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_5.setFont(font)
		self.lblName6_5.setObjectName("lblName6_5")
		self.chkSel6_5 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_5.setGeometry(QtCore.QRect(830, 120, 86, 20))
		self.chkSel6_5.setText("")
		self.chkSel6_5.setObjectName("chkSel6_5")
		self.cmdDisplay6_5 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_5.setGeometry(QtCore.QRect(850, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_5.setFont(font)
		self.cmdDisplay6_5.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_5.setFlat(True)
		self.cmdDisplay6_5.setObjectName("cmdDisplay6_5")
		self.pbProgram6_5 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_5.setGeometry(QtCore.QRect(850, 170, 141, 31))
		self.pbProgram6_5.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_5.setProperty("value", 24)
		self.pbProgram6_5.setObjectName("pbProgram6_5")
		self.lblName6_6 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_6.setGeometry(QtCore.QRect(1040, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_6.setFont(font)
		self.lblName6_6.setObjectName("lblName6_6")
		self.chkSel6_6 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_6.setGeometry(QtCore.QRect(1020, 120, 86, 20))
		self.chkSel6_6.setText("")
		self.chkSel6_6.setObjectName("chkSel6_6")
		self.cmdDisplay6_6 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_6.setGeometry(QtCore.QRect(1040, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_6.setFont(font)
		self.cmdDisplay6_6.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_6.setFlat(True)
		self.cmdDisplay6_6.setObjectName("cmdDisplay6_6")
		self.pbProgram6_6 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_6.setGeometry(QtCore.QRect(1040, 170, 141, 31))
		self.pbProgram6_6.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_6.setProperty("value", 24)
		self.pbProgram6_6.setObjectName("pbProgram6_6")
		self.lblName6_7 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_7.setGeometry(QtCore.QRect(1230, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_7.setFont(font)
		self.lblName6_7.setObjectName("lblName6_7")
		self.chkSel6_7 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_7.setGeometry(QtCore.QRect(1210, 120, 86, 20))
		self.chkSel6_7.setText("")
		self.chkSel6_7.setObjectName("chkSel6_7")
		self.cmdDisplay6_7 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_7.setGeometry(QtCore.QRect(1230, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_7.setFont(font)
		self.cmdDisplay6_7.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_7.setFlat(True)
		self.cmdDisplay6_7.setObjectName("cmdDisplay6_7")
		self.pbProgram6_7 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_7.setGeometry(QtCore.QRect(1230, 170, 141, 31))
		self.pbProgram6_7.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_7.setProperty("value", 24)
		self.pbProgram6_7.setObjectName("pbProgram6_7")
		self.lblName6_8 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_8.setGeometry(QtCore.QRect(90, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_8.setFont(font)
		self.lblName6_8.setObjectName("lblName6_8")
		self.chkSel6_8 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_8.setGeometry(QtCore.QRect(70, 250, 86, 20))
		self.chkSel6_8.setText("")
		self.chkSel6_8.setObjectName("chkSel6_8")
		self.cmdDisplay6_8 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_8.setGeometry(QtCore.QRect(90, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_8.setFont(font)
		self.cmdDisplay6_8.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_8.setFlat(True)
		self.cmdDisplay6_8.setObjectName("cmdDisplay6_8")
		self.pbProgram6_8 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_8.setGeometry(QtCore.QRect(90, 300, 141, 31))
		self.pbProgram6_8.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_8.setProperty("value", 24)
		self.pbProgram6_8.setObjectName("pbProgram6_8")
		self.lblName6_9 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_9.setGeometry(QtCore.QRect(280, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_9.setFont(font)
		self.lblName6_9.setObjectName("lblName6_9")
		self.chkSel6_9 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_9.setGeometry(QtCore.QRect(260, 250, 86, 20))
		self.chkSel6_9.setText("")
		self.chkSel6_9.setObjectName("chkSel6_9")
		self.cmdDisplay6_9 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_9.setGeometry(QtCore.QRect(280, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_9.setFont(font)
		self.cmdDisplay6_9.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_9.setFlat(True)
		self.cmdDisplay6_9.setObjectName("cmdDisplay6_9")
		self.pbProgram6_9 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_9.setGeometry(QtCore.QRect(280, 300, 141, 31))
		self.pbProgram6_9.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_9.setProperty("value", 24)
		self.pbProgram6_9.setObjectName("pbProgram6_9")
		self.lblName6_10 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_10.setGeometry(QtCore.QRect(470, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_10.setFont(font)
		self.lblName6_10.setObjectName("lblName6_10")
		self.chkSel6_10 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_10.setGeometry(QtCore.QRect(450, 250, 86, 20))
		self.chkSel6_10.setText("")
		self.chkSel6_10.setObjectName("chkSel6_10")
		self.cmdDisplay6_10 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_10.setGeometry(QtCore.QRect(470, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_10.setFont(font)
		self.cmdDisplay6_10.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_10.setFlat(True)
		self.cmdDisplay6_10.setObjectName("cmdDisplay6_10")
		self.pbProgram6_10 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_10.setGeometry(QtCore.QRect(470, 300, 141, 31))
		self.pbProgram6_10.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_10.setProperty("value", 24)
		self.pbProgram6_10.setObjectName("pbProgram6_10")
		self.lblName6_11 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_11.setGeometry(QtCore.QRect(660, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_11.setFont(font)
		self.lblName6_11.setObjectName("lblName6_11")
		self.chkSel6_11 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_11.setGeometry(QtCore.QRect(640, 250, 86, 20))
		self.chkSel6_11.setText("")
		self.chkSel6_11.setObjectName("chkSel6_11")
		self.cmdDisplay6_11 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_11.setGeometry(QtCore.QRect(660, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_11.setFont(font)
		self.cmdDisplay6_11.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_11.setFlat(True)
		self.cmdDisplay6_11.setObjectName("cmdDisplay6_11")
		self.pbProgram6_11 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_11.setGeometry(QtCore.QRect(660, 300, 141, 31))
		self.pbProgram6_11.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_11.setProperty("value", 24)
		self.pbProgram6_11.setObjectName("pbProgram6_11")
		self.lblName6_12 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_12.setGeometry(QtCore.QRect(850, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_12.setFont(font)
		self.lblName6_12.setObjectName("lblName6_12")
		self.chkSel6_12 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_12.setGeometry(QtCore.QRect(830, 250, 86, 20))
		self.chkSel6_12.setText("")
		self.chkSel6_12.setObjectName("chkSel6_12")
		self.cmdDisplay6_12 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_12.setGeometry(QtCore.QRect(850, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_12.setFont(font)
		self.cmdDisplay6_12.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_12.setFlat(True)
		self.cmdDisplay6_12.setObjectName("cmdDisplay6_12")
		self.pbProgram6_12 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_12.setGeometry(QtCore.QRect(850, 300, 141, 31))
		self.pbProgram6_12.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_12.setProperty("value", 24)
		self.pbProgram6_12.setObjectName("pbProgram6_12")
		self.lblName6_13 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_13.setGeometry(QtCore.QRect(1040, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_13.setFont(font)
		self.lblName6_13.setObjectName("lblName6_13")
		self.chkSel6_13 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_13.setGeometry(QtCore.QRect(1020, 250, 86, 20))
		self.chkSel6_13.setText("")
		self.chkSel6_13.setObjectName("chkSel6_13")
		self.cmdDisplay6_13 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_13.setGeometry(QtCore.QRect(1040, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_13.setFont(font)
		self.cmdDisplay6_13.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_13.setFlat(True)
		self.cmdDisplay6_13.setObjectName("cmdDisplay6_13")
		self.pbProgram6_13 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_13.setGeometry(QtCore.QRect(1040, 300, 141, 31))
		self.pbProgram6_13.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_13.setProperty("value", 24)
		self.pbProgram6_13.setObjectName("pbProgram6_13")
		self.lblName6_14 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_14.setGeometry(QtCore.QRect(1230, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_14.setFont(font)
		self.lblName6_14.setObjectName("lblName6_14")
		self.chkSel6_14 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_14.setGeometry(QtCore.QRect(1210, 250, 86, 20))
		self.chkSel6_14.setText("")
		self.chkSel6_14.setObjectName("chkSel6_14")
		self.cmdDisplay6_14 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_14.setGeometry(QtCore.QRect(1230, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_14.setFont(font)
		self.cmdDisplay6_14.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_14.setFlat(True)
		self.cmdDisplay6_14.setObjectName("cmdDisplay6_14")
		self.pbProgram6_14 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_14.setGeometry(QtCore.QRect(1230, 300, 141, 31))
		self.pbProgram6_14.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_14.setProperty("value", 24)
		self.pbProgram6_14.setObjectName("pbProgram6_14")
		self.lblName6_15 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_15.setGeometry(QtCore.QRect(90, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_15.setFont(font)
		self.lblName6_15.setObjectName("lblName6_15")
		self.chkSel6_15 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_15.setGeometry(QtCore.QRect(70, 380, 86, 20))
		self.chkSel6_15.setText("")
		self.chkSel6_15.setObjectName("chkSel6_15")
		self.cmdDisplay6_15 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_15.setGeometry(QtCore.QRect(90, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_15.setFont(font)
		self.cmdDisplay6_15.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_15.setFlat(True)
		self.cmdDisplay6_15.setObjectName("cmdDisplay6_15")
		self.pbProgram6_15 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_15.setGeometry(QtCore.QRect(90, 430, 141, 31))
		self.pbProgram6_15.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_15.setProperty("value", 24)
		self.pbProgram6_15.setObjectName("pbProgram6_15")
		self.lblName6_16 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_16.setGeometry(QtCore.QRect(280, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_16.setFont(font)
		self.lblName6_16.setObjectName("lblName6_16")
		self.chkSel6_16 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_16.setGeometry(QtCore.QRect(260, 380, 86, 20))
		self.chkSel6_16.setText("")
		self.chkSel6_16.setObjectName("chkSel6_16")
		self.cmdDisplay6_16 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_16.setGeometry(QtCore.QRect(280, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_16.setFont(font)
		self.cmdDisplay6_16.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_16.setFlat(True)
		self.cmdDisplay6_16.setObjectName("cmdDisplay6_16")
		self.pbProgram6_16 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_16.setGeometry(QtCore.QRect(280, 430, 141, 31))
		self.pbProgram6_16.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_16.setProperty("value", 24)
		self.pbProgram6_16.setObjectName("pbProgram6_16")
		self.lblName6_17 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_17.setGeometry(QtCore.QRect(470, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_17.setFont(font)
		self.lblName6_17.setObjectName("lblName6_17")
		self.chkSel6_17 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_17.setGeometry(QtCore.QRect(450, 380, 86, 20))
		self.chkSel6_17.setText("")
		self.chkSel6_17.setObjectName("chkSel6_17")
		self.cmdDisplay6_17 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_17.setGeometry(QtCore.QRect(470, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_17.setFont(font)
		self.cmdDisplay6_17.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_17.setFlat(True)
		self.cmdDisplay6_17.setObjectName("cmdDisplay6_17")
		self.pbProgram6_17 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_17.setGeometry(QtCore.QRect(470, 430, 141, 31))
		self.pbProgram6_17.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_17.setProperty("value", 24)
		self.pbProgram6_17.setObjectName("pbProgram6_17")
		self.lblName6_18 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_18.setGeometry(QtCore.QRect(660, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_18.setFont(font)
		self.lblName6_18.setObjectName("lblName6_18")
		self.chkSel6_18 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_18.setGeometry(QtCore.QRect(640, 380, 86, 20))
		self.chkSel6_18.setText("")
		self.chkSel6_18.setObjectName("chkSel6_18")
		self.cmdDisplay6_18 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_18.setGeometry(QtCore.QRect(660, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_18.setFont(font)
		self.cmdDisplay6_18.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_18.setFlat(True)
		self.cmdDisplay6_18.setObjectName("cmdDisplay6_18")
		self.pbProgram6_18 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_18.setGeometry(QtCore.QRect(660, 430, 141, 31))
		self.pbProgram6_18.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_18.setProperty("value", 24)
		self.pbProgram6_18.setObjectName("pbProgram6_18")
		self.lblName6_19 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_19.setGeometry(QtCore.QRect(850, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_19.setFont(font)
		self.lblName6_19.setObjectName("lblName6_19")
		self.chkSel6_19 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_19.setGeometry(QtCore.QRect(830, 380, 86, 20))
		self.chkSel6_19.setText("")
		self.chkSel6_19.setObjectName("chkSel6_19")
		self.cmdDisplay6_19 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_19.setGeometry(QtCore.QRect(850, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_19.setFont(font)
		self.cmdDisplay6_19.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_19.setFlat(True)
		self.cmdDisplay6_19.setObjectName("cmdDisplay6_19")
		self.pbProgram6_19 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_19.setGeometry(QtCore.QRect(850, 430, 141, 31))
		self.pbProgram6_19.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_19.setProperty("value", 24)
		self.pbProgram6_19.setObjectName("pbProgram6_19")
		self.lblName6_20 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_20.setGeometry(QtCore.QRect(1040, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_20.setFont(font)
		self.lblName6_20.setObjectName("lblName6_20")
		self.chkSel6_20 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_20.setGeometry(QtCore.QRect(1020, 380, 86, 20))
		self.chkSel6_20.setText("")
		self.chkSel6_20.setObjectName("chkSel6_20")
		self.cmdDisplay6_20 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_20.setGeometry(QtCore.QRect(1040, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_20.setFont(font)
		self.cmdDisplay6_20.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_20.setFlat(True)
		self.cmdDisplay6_20.setObjectName("cmdDisplay6_20")
		self.pbProgram6_20 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_20.setGeometry(QtCore.QRect(1040, 430, 141, 31))
		self.pbProgram6_20.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_20.setProperty("value", 24)
		self.pbProgram6_20.setObjectName("pbProgram6_20")
		self.lblName6_21 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_21.setGeometry(QtCore.QRect(1230, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_21.setFont(font)
		self.lblName6_21.setObjectName("lblName6_21")
		self.chkSel6_21 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_21.setGeometry(QtCore.QRect(1210, 380, 86, 20))
		self.chkSel6_21.setText("")
		self.chkSel6_21.setObjectName("chkSel6_21")
		self.cmdDisplay6_21 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_21.setGeometry(QtCore.QRect(1230, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_21.setFont(font)
		self.cmdDisplay6_21.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_21.setFlat(True)
		self.cmdDisplay6_21.setObjectName("cmdDisplay6_21")
		self.pbProgram6_21 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_21.setGeometry(QtCore.QRect(1230, 430, 141, 31))
		self.pbProgram6_21.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_21.setProperty("value", 24)
		self.pbProgram6_21.setObjectName("pbProgram6_21")
		self.lblName6_22 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_22.setGeometry(QtCore.QRect(90, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_22.setFont(font)
		self.lblName6_22.setObjectName("lblName6_22")
		self.chkSel6_22 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_22.setGeometry(QtCore.QRect(70, 510, 86, 20))
		self.chkSel6_22.setText("")
		self.chkSel6_22.setObjectName("chkSel6_22")
		self.cmdDisplay6_22 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_22.setGeometry(QtCore.QRect(90, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_22.setFont(font)
		self.cmdDisplay6_22.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_22.setFlat(True)
		self.cmdDisplay6_22.setObjectName("cmdDisplay6_22")
		self.pbProgram6_22 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_22.setGeometry(QtCore.QRect(90, 560, 141, 31))
		self.pbProgram6_22.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_22.setProperty("value", 24)
		self.pbProgram6_22.setObjectName("pbProgram6_22")
		self.lblName6_23 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_23.setGeometry(QtCore.QRect(280, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_23.setFont(font)
		self.lblName6_23.setObjectName("lblName6_23")
		self.chkSel6_23 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_23.setGeometry(QtCore.QRect(260, 510, 86, 20))
		self.chkSel6_23.setText("")
		self.chkSel6_23.setObjectName("chkSel6_23")
		self.cmdDisplay6_23 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_23.setGeometry(QtCore.QRect(280, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_23.setFont(font)
		self.cmdDisplay6_23.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_23.setFlat(True)
		self.cmdDisplay6_23.setObjectName("cmdDisplay6_23")
		self.pbProgram6_23 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_23.setGeometry(QtCore.QRect(280, 560, 141, 31))
		self.pbProgram6_23.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_23.setProperty("value", 24)
		self.pbProgram6_23.setObjectName("pbProgram6_23")
		self.lblName6_24 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_24.setGeometry(QtCore.QRect(470, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_24.setFont(font)
		self.lblName6_24.setObjectName("lblName6_24")
		self.chkSel6_24 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_24.setGeometry(QtCore.QRect(450, 510, 86, 20))
		self.chkSel6_24.setText("")
		self.chkSel6_24.setObjectName("chkSel6_24")
		self.cmdDisplay6_24 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_24.setGeometry(QtCore.QRect(470, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_24.setFont(font)
		self.cmdDisplay6_24.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_24.setFlat(True)
		self.cmdDisplay6_24.setObjectName("cmdDisplay6_24")
		self.pbProgram6_24 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_24.setGeometry(QtCore.QRect(470, 560, 141, 31))
		self.pbProgram6_24.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_24.setProperty("value", 24)
		self.pbProgram6_24.setObjectName("pbProgram6_24")
		self.lblName6_25 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_25.setGeometry(QtCore.QRect(660, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_25.setFont(font)
		self.lblName6_25.setObjectName("lblName6_25")
		self.chkSel6_25 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_25.setGeometry(QtCore.QRect(640, 510, 86, 20))
		self.chkSel6_25.setText("")
		self.chkSel6_25.setObjectName("chkSel6_25")
		self.cmdDisplay6_25 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_25.setGeometry(QtCore.QRect(660, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_25.setFont(font)
		self.cmdDisplay6_25.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_25.setFlat(True)
		self.cmdDisplay6_25.setObjectName("cmdDisplay6_25")
		self.pbProgram6_25 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_25.setGeometry(QtCore.QRect(660, 560, 141, 31))
		self.pbProgram6_25.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_25.setProperty("value", 24)
		self.pbProgram6_25.setObjectName("pbProgram6_25")
		self.lblName6_26 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_26.setGeometry(QtCore.QRect(850, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_26.setFont(font)
		self.lblName6_26.setObjectName("lblName6_26")
		self.chkSel6_26 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_26.setGeometry(QtCore.QRect(830, 510, 86, 20))
		self.chkSel6_26.setText("")
		self.chkSel6_26.setObjectName("chkSel6_26")
		self.cmdDisplay6_26 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_26.setGeometry(QtCore.QRect(850, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_26.setFont(font)
		self.cmdDisplay6_26.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_26.setFlat(True)
		self.cmdDisplay6_26.setObjectName("cmdDisplay6_26")
		self.pbProgram6_26 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_26.setGeometry(QtCore.QRect(850, 560, 141, 31))
		self.pbProgram6_26.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_26.setProperty("value", 24)
		self.pbProgram6_26.setObjectName("pbProgram6_26")
		self.lblName6_27 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_27.setGeometry(QtCore.QRect(1040, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_27.setFont(font)
		self.lblName6_27.setObjectName("lblName6_27")
		self.chkSel6_27 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_27.setGeometry(QtCore.QRect(1020, 510, 86, 20))
		self.chkSel6_27.setText("")
		self.chkSel6_27.setObjectName("chkSel6_27")
		self.cmdDisplay6_27 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_27.setGeometry(QtCore.QRect(1040, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_27.setFont(font)
		self.cmdDisplay6_27.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_27.setFlat(True)
		self.cmdDisplay6_27.setObjectName("cmdDisplay6_27")
		self.pbProgram6_27 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_27.setGeometry(QtCore.QRect(1040, 560, 141, 31))
		self.pbProgram6_27.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_27.setProperty("value", 24)
		self.pbProgram6_27.setObjectName("pbProgram6_27")
		self.lblName6_28 = QtWidgets.QLabel(self.tbPage6)
		self.lblName6_28.setGeometry(QtCore.QRect(1230, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName6_28.setFont(font)
		self.lblName6_28.setObjectName("lblName6_28")
		self.chkSel6_28 = QtWidgets.QCheckBox(self.tbPage6)
		self.chkSel6_28.setGeometry(QtCore.QRect(1210, 510, 86, 20))
		self.chkSel6_28.setText("")
		self.chkSel6_28.setObjectName("chkSel6_28")
		self.cmdDisplay6_28 = QtWidgets.QPushButton(self.tbPage6)
		self.cmdDisplay6_28.setGeometry(QtCore.QRect(1230, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay6_28.setFont(font)
		self.cmdDisplay6_28.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay6_28.setFlat(True)
		self.cmdDisplay6_28.setObjectName("cmdDisplay6_28")
		self.pbProgram6_28 = QtWidgets.QProgressBar(self.tbPage6)
		self.pbProgram6_28.setGeometry(QtCore.QRect(1230, 560, 141, 31))
		self.pbProgram6_28.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram6_28.setProperty("value", 24)
		self.pbProgram6_28.setObjectName("pbProgram6_28")
		self.tabWidget.addTab(self.tbPage6, "")
		self.tbPage7 = QtWidgets.QWidget()
		self.tbPage7.setObjectName("tbPage7")
		self.lblPage7 = QtWidgets.QLabel(self.tbPage7)
		self.lblPage7.setGeometry(QtCore.QRect(40, 30, 671, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.lblPage7.setFont(font)
		self.lblPage7.setObjectName("lblPage7")
		self.lblName7_1 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_1.setGeometry(QtCore.QRect(90, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_1.setFont(font)
		self.lblName7_1.setObjectName("lblName7_1")
		self.chkSel7_1 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_1.setGeometry(QtCore.QRect(70, 120, 86, 20))
		self.chkSel7_1.setText("")
		self.chkSel7_1.setObjectName("chkSel7_1")
		self.cmdDisplay7_1 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_1.setGeometry(QtCore.QRect(90, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_1.setFont(font)
		self.cmdDisplay7_1.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_1.setFlat(True)
		self.cmdDisplay7_1.setObjectName("cmdDisplay7_1")
		self.pbProgram7_1 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_1.setGeometry(QtCore.QRect(90, 170, 141, 31))
		self.pbProgram7_1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_1.setProperty("value", 24)
		self.pbProgram7_1.setObjectName("pbProgram7_1")
		self.cmdDisplay7_2 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_2.setGeometry(QtCore.QRect(280, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_2.setFont(font)
		self.cmdDisplay7_2.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_2.setFlat(True)
		self.cmdDisplay7_2.setObjectName("cmdDisplay7_2")
		self.lblName7_2 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_2.setGeometry(QtCore.QRect(280, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_2.setFont(font)
		self.lblName7_2.setObjectName("lblName7_2")
		self.chkSel7_2 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_2.setGeometry(QtCore.QRect(260, 120, 86, 20))
		self.chkSel7_2.setText("")
		self.chkSel7_2.setObjectName("chkSel7_2")
		self.pbProgram7_2 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_2.setGeometry(QtCore.QRect(280, 170, 141, 31))
		self.pbProgram7_2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_2.setProperty("value", 24)
		self.pbProgram7_2.setObjectName("pbProgram7_2")
		self.cmdDisplay7_3 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_3.setGeometry(QtCore.QRect(470, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_3.setFont(font)
		self.cmdDisplay7_3.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_3.setFlat(True)
		self.cmdDisplay7_3.setObjectName("cmdDisplay7_3")
		self.lblName7_3 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_3.setGeometry(QtCore.QRect(470, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_3.setFont(font)
		self.lblName7_3.setObjectName("lblName7_3")
		self.chkSel7_3 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_3.setGeometry(QtCore.QRect(450, 120, 86, 20))
		self.chkSel7_3.setText("")
		self.chkSel7_3.setObjectName("chkSel7_3")
		self.pbProgram7_3 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
		self.pbProgram7_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_3.setProperty("value", 24)
		self.pbProgram7_3.setObjectName("pbProgram7_3")
		self.cmdDisplay7_4 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_4.setGeometry(QtCore.QRect(660, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_4.setFont(font)
		self.cmdDisplay7_4.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_4.setFlat(True)
		self.cmdDisplay7_4.setObjectName("cmdDisplay7_4")
		self.lblName7_4 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_4.setGeometry(QtCore.QRect(660, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_4.setFont(font)
		self.lblName7_4.setObjectName("lblName7_4")
		self.chkSel7_4 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_4.setGeometry(QtCore.QRect(640, 120, 86, 20))
		self.chkSel7_4.setText("")
		self.chkSel7_4.setObjectName("chkSel7_4")
		self.pbProgram7_4 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_4.setGeometry(QtCore.QRect(660, 170, 141, 31))
		self.pbProgram7_4.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_4.setProperty("value", 24)
		self.pbProgram7_4.setObjectName("pbProgram7_4")
		self.cmdDisplay7_5 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_5.setGeometry(QtCore.QRect(850, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_5.setFont(font)
		self.cmdDisplay7_5.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_5.setFlat(True)
		self.cmdDisplay7_5.setObjectName("cmdDisplay7_5")
		self.lblName7_5 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_5.setGeometry(QtCore.QRect(850, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_5.setFont(font)
		self.lblName7_5.setObjectName("lblName7_5")
		self.chkSel7_5 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_5.setGeometry(QtCore.QRect(830, 120, 86, 20))
		self.chkSel7_5.setText("")
		self.chkSel7_5.setObjectName("chkSel7_5")
		self.pbProgram7_5 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_5.setGeometry(QtCore.QRect(850, 170, 141, 31))
		self.pbProgram7_5.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_5.setProperty("value", 24)
		self.pbProgram7_5.setObjectName("pbProgram7_5")
		self.cmdDisplay7_6 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_6.setGeometry(QtCore.QRect(1040, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_6.setFont(font)
		self.cmdDisplay7_6.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_6.setFlat(True)
		self.cmdDisplay7_6.setObjectName("cmdDisplay7_6")
		self.lblName7_6 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_6.setGeometry(QtCore.QRect(1040, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_6.setFont(font)
		self.lblName7_6.setObjectName("lblName7_6")
		self.chkSel7_6 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_6.setGeometry(QtCore.QRect(1020, 120, 86, 20))
		self.chkSel7_6.setText("")
		self.chkSel7_6.setObjectName("chkSel7_6")
		self.pbProgram7_6 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_6.setGeometry(QtCore.QRect(1040, 170, 141, 31))
		self.pbProgram7_6.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_6.setProperty("value", 24)
		self.pbProgram7_6.setObjectName("pbProgram7_6")
		self.cmdDisplay7_7 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_7.setGeometry(QtCore.QRect(1230, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_7.setFont(font)
		self.cmdDisplay7_7.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_7.setFlat(True)
		self.cmdDisplay7_7.setObjectName("cmdDisplay7_7")
		self.lblName7_7 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_7.setGeometry(QtCore.QRect(1230, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_7.setFont(font)
		self.lblName7_7.setObjectName("lblName7_7")
		self.chkSel7_7 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_7.setGeometry(QtCore.QRect(1210, 120, 86, 20))
		self.chkSel7_7.setText("")
		self.chkSel7_7.setObjectName("chkSel7_7")
		self.pbProgram7_7 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_7.setGeometry(QtCore.QRect(1230, 170, 141, 31))
		self.pbProgram7_7.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_7.setProperty("value", 24)
		self.pbProgram7_7.setObjectName("pbProgram7_7")
		self.cmdDisplay7_8 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_8.setGeometry(QtCore.QRect(90, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_8.setFont(font)
		self.cmdDisplay7_8.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_8.setFlat(True)
		self.cmdDisplay7_8.setObjectName("cmdDisplay7_8")
		self.lblName7_8 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_8.setGeometry(QtCore.QRect(90, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_8.setFont(font)
		self.lblName7_8.setObjectName("lblName7_8")
		self.chkSel7_8 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_8.setGeometry(QtCore.QRect(70, 250, 86, 20))
		self.chkSel7_8.setText("")
		self.chkSel7_8.setObjectName("chkSel7_8")
		self.pbProgram7_8 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_8.setGeometry(QtCore.QRect(90, 300, 141, 31))
		self.pbProgram7_8.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_8.setProperty("value", 24)
		self.pbProgram7_8.setObjectName("pbProgram7_8")
		self.cmdDisplay7_9 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_9.setGeometry(QtCore.QRect(280, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_9.setFont(font)
		self.cmdDisplay7_9.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_9.setFlat(True)
		self.cmdDisplay7_9.setObjectName("cmdDisplay7_9")
		self.lblName7_9 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_9.setGeometry(QtCore.QRect(280, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_9.setFont(font)
		self.lblName7_9.setObjectName("lblName7_9")
		self.chkSel7_9 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_9.setGeometry(QtCore.QRect(260, 250, 86, 20))
		self.chkSel7_9.setText("")
		self.chkSel7_9.setObjectName("chkSel7_9")
		self.pbProgram7_9 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_9.setGeometry(QtCore.QRect(280, 300, 141, 31))
		self.pbProgram7_9.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_9.setProperty("value", 24)
		self.pbProgram7_9.setObjectName("pbProgram7_9")
		self.cmdDisplay7_10 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_10.setGeometry(QtCore.QRect(470, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_10.setFont(font)
		self.cmdDisplay7_10.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_10.setFlat(True)
		self.cmdDisplay7_10.setObjectName("cmdDisplay7_10")
		self.lblName7_10 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_10.setGeometry(QtCore.QRect(470, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_10.setFont(font)
		self.lblName7_10.setObjectName("lblName7_10")
		self.chkSel7_10 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_10.setGeometry(QtCore.QRect(450, 250, 86, 20))
		self.chkSel7_10.setText("")
		self.chkSel7_10.setObjectName("chkSel7_10")
		self.pbProgram7_10 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_10.setGeometry(QtCore.QRect(470, 300, 141, 31))
		self.pbProgram7_10.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_10.setProperty("value", 24)
		self.pbProgram7_10.setObjectName("pbProgram7_10")
		self.cmdDisplay7_11 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_11.setGeometry(QtCore.QRect(660, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_11.setFont(font)
		self.cmdDisplay7_11.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_11.setFlat(True)
		self.cmdDisplay7_11.setObjectName("cmdDisplay7_11")
		self.lblName7_11 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_11.setGeometry(QtCore.QRect(660, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_11.setFont(font)
		self.lblName7_11.setObjectName("lblName7_11")
		self.chkSel7_11 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_11.setGeometry(QtCore.QRect(640, 250, 86, 20))
		self.chkSel7_11.setText("")
		self.chkSel7_11.setObjectName("chkSel7_11")
		self.pbProgram7_11 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_11.setGeometry(QtCore.QRect(660, 300, 141, 31))
		self.pbProgram7_11.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_11.setProperty("value", 24)
		self.pbProgram7_11.setObjectName("pbProgram7_11")
		self.cmdDisplay7_12 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_12.setGeometry(QtCore.QRect(850, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_12.setFont(font)
		self.cmdDisplay7_12.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_12.setFlat(True)
		self.cmdDisplay7_12.setObjectName("cmdDisplay7_12")
		self.lblName7_12 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_12.setGeometry(QtCore.QRect(850, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_12.setFont(font)
		self.lblName7_12.setObjectName("lblName7_12")
		self.chkSel7_12 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_12.setGeometry(QtCore.QRect(830, 250, 86, 20))
		self.chkSel7_12.setText("")
		self.chkSel7_12.setObjectName("chkSel7_12")
		self.pbProgram7_12 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_12.setGeometry(QtCore.QRect(850, 300, 141, 31))
		self.pbProgram7_12.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_12.setProperty("value", 24)
		self.pbProgram7_12.setObjectName("pbProgram7_12")
		self.cmdDisplay7_13 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_13.setGeometry(QtCore.QRect(1040, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_13.setFont(font)
		self.cmdDisplay7_13.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_13.setFlat(True)
		self.cmdDisplay7_13.setObjectName("cmdDisplay7_13")
		self.lblName7_13 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_13.setGeometry(QtCore.QRect(1040, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_13.setFont(font)
		self.lblName7_13.setObjectName("lblName7_13")
		self.chkSel7_13 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_13.setGeometry(QtCore.QRect(1020, 250, 86, 20))
		self.chkSel7_13.setText("")
		self.chkSel7_13.setObjectName("chkSel7_13")
		self.pbProgram7_13 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_13.setGeometry(QtCore.QRect(1040, 300, 141, 31))
		self.pbProgram7_13.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_13.setProperty("value", 24)
		self.pbProgram7_13.setObjectName("pbProgram7_13")
		self.cmdDisplay7_14 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_14.setGeometry(QtCore.QRect(1230, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_14.setFont(font)
		self.cmdDisplay7_14.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_14.setFlat(True)
		self.cmdDisplay7_14.setObjectName("cmdDisplay7_14")
		self.lblName7_14 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_14.setGeometry(QtCore.QRect(1230, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_14.setFont(font)
		self.lblName7_14.setObjectName("lblName7_14")
		self.chkSel7_14 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_14.setGeometry(QtCore.QRect(1210, 250, 86, 20))
		self.chkSel7_14.setText("")
		self.chkSel7_14.setObjectName("chkSel7_14")
		self.pbProgram7_14 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_14.setGeometry(QtCore.QRect(1230, 300, 141, 31))
		self.pbProgram7_14.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_14.setProperty("value", 24)
		self.pbProgram7_14.setObjectName("pbProgram7_14")
		self.cmdDisplay7_15 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_15.setGeometry(QtCore.QRect(90, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_15.setFont(font)
		self.cmdDisplay7_15.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_15.setFlat(True)
		self.cmdDisplay7_15.setObjectName("cmdDisplay7_15")
		self.lblName7_15 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_15.setGeometry(QtCore.QRect(90, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_15.setFont(font)
		self.lblName7_15.setObjectName("lblName7_15")
		self.chkSel7_15 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_15.setGeometry(QtCore.QRect(70, 380, 86, 20))
		self.chkSel7_15.setText("")
		self.chkSel7_15.setObjectName("chkSel7_15")
		self.pbProgram7_15 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_15.setGeometry(QtCore.QRect(90, 430, 141, 31))
		self.pbProgram7_15.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_15.setProperty("value", 24)
		self.pbProgram7_15.setObjectName("pbProgram7_15")
		self.cmdDisplay7_16 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_16.setGeometry(QtCore.QRect(280, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_16.setFont(font)
		self.cmdDisplay7_16.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_16.setFlat(True)
		self.cmdDisplay7_16.setObjectName("cmdDisplay7_16")
		self.lblName7_16 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_16.setGeometry(QtCore.QRect(280, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_16.setFont(font)
		self.lblName7_16.setObjectName("lblName7_16")
		self.chkSel7_16 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_16.setGeometry(QtCore.QRect(260, 380, 86, 20))
		self.chkSel7_16.setText("")
		self.chkSel7_16.setObjectName("chkSel7_16")
		self.pbProgram7_16 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_16.setGeometry(QtCore.QRect(280, 430, 141, 31))
		self.pbProgram7_16.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_16.setProperty("value", 24)
		self.pbProgram7_16.setObjectName("pbProgram7_16")
		self.cmdDisplay7_17 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_17.setGeometry(QtCore.QRect(470, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_17.setFont(font)
		self.cmdDisplay7_17.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_17.setFlat(True)
		self.cmdDisplay7_17.setObjectName("cmdDisplay7_17")
		self.lblName7_17 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_17.setGeometry(QtCore.QRect(470, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_17.setFont(font)
		self.lblName7_17.setObjectName("lblName7_17")
		self.chkSel7_17 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_17.setGeometry(QtCore.QRect(450, 380, 86, 20))
		self.chkSel7_17.setText("")
		self.chkSel7_17.setObjectName("chkSel7_17")
		self.pbProgram7_17 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_17.setGeometry(QtCore.QRect(470, 430, 141, 31))
		self.pbProgram7_17.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_17.setProperty("value", 24)
		self.pbProgram7_17.setObjectName("pbProgram7_17")
		self.cmdDisplay7_18 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_18.setGeometry(QtCore.QRect(660, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_18.setFont(font)
		self.cmdDisplay7_18.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_18.setFlat(True)
		self.cmdDisplay7_18.setObjectName("cmdDisplay7_18")
		self.lblName7_18 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_18.setGeometry(QtCore.QRect(660, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_18.setFont(font)
		self.lblName7_18.setObjectName("lblName7_18")
		self.chkSel7_18 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_18.setGeometry(QtCore.QRect(640, 380, 86, 20))
		self.chkSel7_18.setText("")
		self.chkSel7_18.setObjectName("chkSel7_18")
		self.pbProgram7_18 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_18.setGeometry(QtCore.QRect(660, 430, 141, 31))
		self.pbProgram7_18.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_18.setProperty("value", 24)
		self.pbProgram7_18.setObjectName("pbProgram7_18")
		self.cmdDisplay7_19 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_19.setGeometry(QtCore.QRect(850, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_19.setFont(font)
		self.cmdDisplay7_19.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_19.setFlat(True)
		self.cmdDisplay7_19.setObjectName("cmdDisplay7_19")
		self.lblName7_19 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_19.setGeometry(QtCore.QRect(850, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_19.setFont(font)
		self.lblName7_19.setObjectName("lblName7_19")
		self.chkSel7_19 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_19.setGeometry(QtCore.QRect(830, 380, 86, 20))
		self.chkSel7_19.setText("")
		self.chkSel7_19.setObjectName("chkSel7_19")
		self.pbProgram7_19 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_19.setGeometry(QtCore.QRect(850, 430, 141, 31))
		self.pbProgram7_19.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_19.setProperty("value", 24)
		self.pbProgram7_19.setObjectName("pbProgram7_19")
		self.cmdDisplay7_20 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_20.setGeometry(QtCore.QRect(1040, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_20.setFont(font)
		self.cmdDisplay7_20.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_20.setFlat(True)
		self.cmdDisplay7_20.setObjectName("cmdDisplay7_20")
		self.lblName7_20 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_20.setGeometry(QtCore.QRect(1040, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_20.setFont(font)
		self.lblName7_20.setObjectName("lblName7_20")
		self.chkSel7_20 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_20.setGeometry(QtCore.QRect(1020, 380, 86, 20))
		self.chkSel7_20.setText("")
		self.chkSel7_20.setObjectName("chkSel7_20")
		self.pbProgram7_20 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_20.setGeometry(QtCore.QRect(1040, 430, 141, 31))
		self.pbProgram7_20.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_20.setProperty("value", 24)
		self.pbProgram7_20.setObjectName("pbProgram7_20")
		self.cmdDisplay7_21 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_21.setGeometry(QtCore.QRect(1230, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_21.setFont(font)
		self.cmdDisplay7_21.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_21.setFlat(True)
		self.cmdDisplay7_21.setObjectName("cmdDisplay7_21")
		self.lblName7_21 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_21.setGeometry(QtCore.QRect(1230, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_21.setFont(font)
		self.lblName7_21.setObjectName("lblName7_21")
		self.chkSel7_21 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_21.setGeometry(QtCore.QRect(1210, 380, 86, 20))
		self.chkSel7_21.setText("")
		self.chkSel7_21.setObjectName("chkSel7_21")
		self.pbProgram7_21 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_21.setGeometry(QtCore.QRect(1230, 430, 141, 31))
		self.pbProgram7_21.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_21.setProperty("value", 24)
		self.pbProgram7_21.setObjectName("pbProgram7_21")
		self.cmdDisplay7_22 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_22.setGeometry(QtCore.QRect(90, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_22.setFont(font)
		self.cmdDisplay7_22.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_22.setFlat(True)
		self.cmdDisplay7_22.setObjectName("cmdDisplay7_22")
		self.lblName7_22 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_22.setGeometry(QtCore.QRect(90, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_22.setFont(font)
		self.lblName7_22.setObjectName("lblName7_22")
		self.chkSel7_22 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_22.setGeometry(QtCore.QRect(70, 510, 86, 20))
		self.chkSel7_22.setText("")
		self.chkSel7_22.setObjectName("chkSel7_22")
		self.pbProgram7_22 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_22.setGeometry(QtCore.QRect(90, 560, 141, 31))
		self.pbProgram7_22.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_22.setProperty("value", 24)
		self.pbProgram7_22.setObjectName("pbProgram7_22")
		self.cmdDisplay7_23 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_23.setGeometry(QtCore.QRect(280, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_23.setFont(font)
		self.cmdDisplay7_23.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_23.setFlat(True)
		self.cmdDisplay7_23.setObjectName("cmdDisplay7_23")
		self.lblName7_23 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_23.setGeometry(QtCore.QRect(280, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_23.setFont(font)
		self.lblName7_23.setObjectName("lblName7_23")
		self.chkSel7_23 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_23.setGeometry(QtCore.QRect(260, 510, 86, 20))
		self.chkSel7_23.setText("")
		self.chkSel7_23.setObjectName("chkSel7_23")
		self.pbProgram7_23 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_23.setGeometry(QtCore.QRect(280, 560, 141, 31))
		self.pbProgram7_23.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_23.setProperty("value", 24)
		self.pbProgram7_23.setObjectName("pbProgram7_23")
		self.cmdDisplay7_24 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_24.setGeometry(QtCore.QRect(470, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_24.setFont(font)
		self.cmdDisplay7_24.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_24.setFlat(True)
		self.cmdDisplay7_24.setObjectName("cmdDisplay7_24")
		self.lblName7_24 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_24.setGeometry(QtCore.QRect(470, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_24.setFont(font)
		self.lblName7_24.setObjectName("lblName7_24")
		self.chkSel7_24 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_24.setGeometry(QtCore.QRect(450, 510, 86, 20))
		self.chkSel7_24.setText("")
		self.chkSel7_24.setObjectName("chkSel7_24")
		self.pbProgram7_24 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_24.setGeometry(QtCore.QRect(470, 560, 141, 31))
		self.pbProgram7_24.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_24.setProperty("value", 24)
		self.pbProgram7_24.setObjectName("pbProgram7_24")
		self.cmdDisplay7_25 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_25.setGeometry(QtCore.QRect(660, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_25.setFont(font)
		self.cmdDisplay7_25.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_25.setFlat(True)
		self.cmdDisplay7_25.setObjectName("cmdDisplay7_25")
		self.lblName7_25 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_25.setGeometry(QtCore.QRect(660, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_25.setFont(font)
		self.lblName7_25.setObjectName("lblName7_25")
		self.chkSel7_25 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_25.setGeometry(QtCore.QRect(640, 510, 86, 20))
		self.chkSel7_25.setText("")
		self.chkSel7_25.setObjectName("chkSel7_25")
		self.pbProgram7_25 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_25.setGeometry(QtCore.QRect(660, 560, 141, 31))
		self.pbProgram7_25.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_25.setProperty("value", 24)
		self.pbProgram7_25.setObjectName("pbProgram7_25")
		self.cmdDisplay7_26 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_26.setGeometry(QtCore.QRect(850, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_26.setFont(font)
		self.cmdDisplay7_26.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_26.setFlat(True)
		self.cmdDisplay7_26.setObjectName("cmdDisplay7_26")
		self.lblName7_26 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_26.setGeometry(QtCore.QRect(850, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_26.setFont(font)
		self.lblName7_26.setObjectName("lblName7_26")
		self.chkSel7_26 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_26.setGeometry(QtCore.QRect(830, 510, 86, 20))
		self.chkSel7_26.setText("")
		self.chkSel7_26.setObjectName("chkSel7_26")
		self.pbProgram7_26 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_26.setGeometry(QtCore.QRect(850, 560, 141, 31))
		self.pbProgram7_26.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_26.setProperty("value", 24)
		self.pbProgram7_26.setObjectName("pbProgram7_26")
		self.cmdDisplay7_27 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_27.setGeometry(QtCore.QRect(1040, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_27.setFont(font)
		self.cmdDisplay7_27.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_27.setFlat(True)
		self.cmdDisplay7_27.setObjectName("cmdDisplay7_27")
		self.lblName7_27 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_27.setGeometry(QtCore.QRect(1040, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_27.setFont(font)
		self.lblName7_27.setObjectName("lblName7_27")
		self.chkSel7_27 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_27.setGeometry(QtCore.QRect(1020, 510, 86, 20))
		self.chkSel7_27.setText("")
		self.chkSel7_27.setObjectName("chkSel7_27")
		self.pbProgram7_27 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_27.setGeometry(QtCore.QRect(1040, 560, 141, 31))
		self.pbProgram7_27.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_27.setProperty("value", 24)
		self.pbProgram7_27.setObjectName("pbProgram7_27")
		self.cmdDisplay7_28 = QtWidgets.QPushButton(self.tbPage7)
		self.cmdDisplay7_28.setGeometry(QtCore.QRect(1230, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay7_28.setFont(font)
		self.cmdDisplay7_28.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay7_28.setFlat(True)
		self.cmdDisplay7_28.setObjectName("cmdDisplay7_28")
		self.lblName7_28 = QtWidgets.QLabel(self.tbPage7)
		self.lblName7_28.setGeometry(QtCore.QRect(1230, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName7_28.setFont(font)
		self.lblName7_28.setObjectName("lblName7_28")
		self.chkSel7_28 = QtWidgets.QCheckBox(self.tbPage7)
		self.chkSel7_28.setGeometry(QtCore.QRect(1210, 510, 86, 20))
		self.chkSel7_28.setText("")
		self.chkSel7_28.setObjectName("chkSel7_28")
		self.pbProgram7_28 = QtWidgets.QProgressBar(self.tbPage7)
		self.pbProgram7_28.setGeometry(QtCore.QRect(1230, 560, 141, 31))
		self.pbProgram7_28.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram7_28.setProperty("value", 24)
		self.pbProgram7_28.setObjectName("pbProgram7_28")
		self.tabWidget.addTab(self.tbPage7, "")
		self.tbPage8 = QtWidgets.QWidget()
		self.tbPage8.setObjectName("tbPage8")
		self.lblPage8 = QtWidgets.QLabel(self.tbPage8)
		self.lblPage8.setGeometry(QtCore.QRect(40, 30, 671, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.lblPage8.setFont(font)
		self.lblPage8.setObjectName("lblPage8")
		self.cmdDisplay8_1 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_1.setGeometry(QtCore.QRect(90, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_1.setFont(font)
		self.cmdDisplay8_1.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_1.setFlat(True)
		self.cmdDisplay8_1.setObjectName("cmdDisplay8_1")
		self.lblName8_1 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_1.setGeometry(QtCore.QRect(90, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_1.setFont(font)
		self.lblName8_1.setObjectName("lblName8_1")
		self.chkSel8_1 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_1.setGeometry(QtCore.QRect(70, 120, 86, 20))
		self.chkSel8_1.setText("")
		self.chkSel8_1.setObjectName("chkSel8_1")
		self.pbProgram8_1 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_1.setGeometry(QtCore.QRect(90, 170, 141, 31))
		self.pbProgram8_1.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_1.setProperty("value", 24)
		self.pbProgram8_1.setObjectName("pbProgram8_1")
		self.pbProgram8_2 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_2.setGeometry(QtCore.QRect(280, 170, 141, 31))
		self.pbProgram8_2.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_2.setProperty("value", 24)
		self.pbProgram8_2.setObjectName("pbProgram8_2")
		self.chkSel8_2 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_2.setGeometry(QtCore.QRect(260, 120, 86, 20))
		self.chkSel8_2.setText("")
		self.chkSel8_2.setObjectName("chkSel8_2")
		self.lblName8_2 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_2.setGeometry(QtCore.QRect(280, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_2.setFont(font)
		self.lblName8_2.setObjectName("lblName8_2")
		self.cmdDisplay8_2 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_2.setGeometry(QtCore.QRect(280, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_2.setFont(font)
		self.cmdDisplay8_2.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_2.setFlat(True)
		self.cmdDisplay8_2.setObjectName("cmdDisplay8_2")
		self.pbProgram8_3 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_3.setGeometry(QtCore.QRect(470, 170, 141, 31))
		self.pbProgram8_3.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_3.setProperty("value", 24)
		self.pbProgram8_3.setObjectName("pbProgram8_3")
		self.chkSel8_3 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_3.setGeometry(QtCore.QRect(450, 120, 86, 20))
		self.chkSel8_3.setText("")
		self.chkSel8_3.setObjectName("chkSel8_3")
		self.lblName8_3 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_3.setGeometry(QtCore.QRect(470, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_3.setFont(font)
		self.lblName8_3.setObjectName("lblName8_3")
		self.cmdDisplay8_3 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_3.setGeometry(QtCore.QRect(470, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_3.setFont(font)
		self.cmdDisplay8_3.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_3.setFlat(True)
		self.cmdDisplay8_3.setObjectName("cmdDisplay8_3")
		self.pbProgram8_4 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_4.setGeometry(QtCore.QRect(660, 170, 141, 31))
		self.pbProgram8_4.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_4.setProperty("value", 24)
		self.pbProgram8_4.setObjectName("pbProgram8_4")
		self.chkSel8_4 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_4.setGeometry(QtCore.QRect(640, 120, 86, 20))
		self.chkSel8_4.setText("")
		self.chkSel8_4.setObjectName("chkSel8_4")
		self.lblName8_4 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_4.setGeometry(QtCore.QRect(660, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_4.setFont(font)
		self.lblName8_4.setObjectName("lblName8_4")
		self.cmdDisplay8_4 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_4.setGeometry(QtCore.QRect(660, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_4.setFont(font)
		self.cmdDisplay8_4.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_4.setFlat(True)
		self.cmdDisplay8_4.setObjectName("cmdDisplay8_4")
		self.pbProgram8_5 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_5.setGeometry(QtCore.QRect(850, 170, 141, 31))
		self.pbProgram8_5.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_5.setProperty("value", 24)
		self.pbProgram8_5.setObjectName("pbProgram8_5")
		self.chkSel8_5 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_5.setGeometry(QtCore.QRect(830, 120, 86, 20))
		self.chkSel8_5.setText("")
		self.chkSel8_5.setObjectName("chkSel8_5")
		self.lblName8_5 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_5.setGeometry(QtCore.QRect(850, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_5.setFont(font)
		self.lblName8_5.setObjectName("lblName8_5")
		self.cmdDisplay8_5 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_5.setGeometry(QtCore.QRect(850, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_5.setFont(font)
		self.cmdDisplay8_5.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_5.setFlat(True)
		self.cmdDisplay8_5.setObjectName("cmdDisplay8_5")
		self.pbProgram8_6 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_6.setGeometry(QtCore.QRect(1040, 170, 141, 31))
		self.pbProgram8_6.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_6.setProperty("value", 24)
		self.pbProgram8_6.setObjectName("pbProgram8_6")
		self.chkSel8_6 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_6.setGeometry(QtCore.QRect(1020, 120, 86, 20))
		self.chkSel8_6.setText("")
		self.chkSel8_6.setObjectName("chkSel8_6")
		self.lblName8_6 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_6.setGeometry(QtCore.QRect(1040, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_6.setFont(font)
		self.lblName8_6.setObjectName("lblName8_6")
		self.cmdDisplay8_6 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_6.setGeometry(QtCore.QRect(1040, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_6.setFont(font)
		self.cmdDisplay8_6.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_6.setFlat(True)
		self.cmdDisplay8_6.setObjectName("cmdDisplay8_6")
		self.pbProgram8_7 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_7.setGeometry(QtCore.QRect(1230, 170, 141, 31))
		self.pbProgram8_7.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_7.setProperty("value", 24)
		self.pbProgram8_7.setObjectName("pbProgram8_7")
		self.chkSel8_7 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_7.setGeometry(QtCore.QRect(1210, 120, 86, 20))
		self.chkSel8_7.setText("")
		self.chkSel8_7.setObjectName("chkSel8_7")
		self.lblName8_7 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_7.setGeometry(QtCore.QRect(1230, 90, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_7.setFont(font)
		self.lblName8_7.setObjectName("lblName8_7")
		self.cmdDisplay8_7 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_7.setGeometry(QtCore.QRect(1230, 140, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_7.setFont(font)
		self.cmdDisplay8_7.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_7.setFlat(True)
		self.cmdDisplay8_7.setObjectName("cmdDisplay8_7")
		self.pbProgram8_8 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_8.setGeometry(QtCore.QRect(90, 300, 141, 31))
		self.pbProgram8_8.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_8.setProperty("value", 24)
		self.pbProgram8_8.setObjectName("pbProgram8_8")
		self.chkSel8_8 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_8.setGeometry(QtCore.QRect(70, 250, 86, 20))
		self.chkSel8_8.setText("")
		self.chkSel8_8.setObjectName("chkSel8_8")
		self.lblName8_8 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_8.setGeometry(QtCore.QRect(90, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_8.setFont(font)
		self.lblName8_8.setObjectName("lblName8_8")
		self.cmdDisplay8_8 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_8.setGeometry(QtCore.QRect(90, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_8.setFont(font)
		self.cmdDisplay8_8.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_8.setFlat(True)
		self.cmdDisplay8_8.setObjectName("cmdDisplay8_8")
		self.pbProgram8_9 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_9.setGeometry(QtCore.QRect(280, 300, 141, 31))
		self.pbProgram8_9.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_9.setProperty("value", 24)
		self.pbProgram8_9.setObjectName("pbProgram8_9")
		self.chkSel8_9 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_9.setGeometry(QtCore.QRect(260, 250, 86, 20))
		self.chkSel8_9.setText("")
		self.chkSel8_9.setObjectName("chkSel8_9")
		self.lblName8_9 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_9.setGeometry(QtCore.QRect(280, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_9.setFont(font)
		self.lblName8_9.setObjectName("lblName8_9")
		self.cmdDisplay8_9 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_9.setGeometry(QtCore.QRect(280, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_9.setFont(font)
		self.cmdDisplay8_9.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_9.setFlat(True)
		self.cmdDisplay8_9.setObjectName("cmdDisplay8_9")
		self.pbProgram8_10 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_10.setGeometry(QtCore.QRect(470, 300, 141, 31))
		self.pbProgram8_10.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_10.setProperty("value", 24)
		self.pbProgram8_10.setObjectName("pbProgram8_10")
		self.chkSel8_10 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_10.setGeometry(QtCore.QRect(450, 250, 86, 20))
		self.chkSel8_10.setText("")
		self.chkSel8_10.setObjectName("chkSel8_10")
		self.lblName8_10 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_10.setGeometry(QtCore.QRect(470, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_10.setFont(font)
		self.lblName8_10.setObjectName("lblName8_10")
		self.cmdDisplay8_10 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_10.setGeometry(QtCore.QRect(470, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_10.setFont(font)
		self.cmdDisplay8_10.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_10.setFlat(True)
		self.cmdDisplay8_10.setObjectName("cmdDisplay8_10")
		self.pbProgram8_11 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_11.setGeometry(QtCore.QRect(660, 300, 141, 31))
		self.pbProgram8_11.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_11.setProperty("value", 24)
		self.pbProgram8_11.setObjectName("pbProgram8_11")
		self.chkSel8_11 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_11.setGeometry(QtCore.QRect(640, 250, 86, 20))
		self.chkSel8_11.setText("")
		self.chkSel8_11.setObjectName("chkSel8_11")
		self.lblName8_11 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_11.setGeometry(QtCore.QRect(660, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_11.setFont(font)
		self.lblName8_11.setObjectName("lblName8_11")
		self.cmdDisplay8_11 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_11.setGeometry(QtCore.QRect(660, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_11.setFont(font)
		self.cmdDisplay8_11.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_11.setFlat(True)
		self.cmdDisplay8_11.setObjectName("cmdDisplay8_11")
		self.pbProgram8_12 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_12.setGeometry(QtCore.QRect(850, 300, 141, 31))
		self.pbProgram8_12.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_12.setProperty("value", 24)
		self.pbProgram8_12.setObjectName("pbProgram8_12")
		self.chkSel8_12 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_12.setGeometry(QtCore.QRect(830, 250, 86, 20))
		self.chkSel8_12.setText("")
		self.chkSel8_12.setObjectName("chkSel8_12")
		self.lblName8_12 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_12.setGeometry(QtCore.QRect(850, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_12.setFont(font)
		self.lblName8_12.setObjectName("lblName8_12")
		self.cmdDisplay8_12 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_12.setGeometry(QtCore.QRect(850, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_12.setFont(font)
		self.cmdDisplay8_12.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_12.setFlat(True)
		self.cmdDisplay8_12.setObjectName("cmdDisplay8_12")
		self.pbProgram8_13 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_13.setGeometry(QtCore.QRect(1040, 300, 141, 31))
		self.pbProgram8_13.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_13.setProperty("value", 24)
		self.pbProgram8_13.setObjectName("pbProgram8_13")
		self.chkSel8_13 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_13.setGeometry(QtCore.QRect(1020, 250, 86, 20))
		self.chkSel8_13.setText("")
		self.chkSel8_13.setObjectName("chkSel8_13")
		self.lblName8_13 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_13.setGeometry(QtCore.QRect(1040, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_13.setFont(font)
		self.lblName8_13.setObjectName("lblName8_13")
		self.cmdDisplay8_13 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_13.setGeometry(QtCore.QRect(1040, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_13.setFont(font)
		self.cmdDisplay8_13.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_13.setFlat(True)
		self.cmdDisplay8_13.setObjectName("cmdDisplay8_13")
		self.pbProgram8_14 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_14.setGeometry(QtCore.QRect(1230, 300, 141, 31))
		self.pbProgram8_14.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_14.setProperty("value", 24)
		self.pbProgram8_14.setObjectName("pbProgram8_14")
		self.chkSel8_14 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_14.setGeometry(QtCore.QRect(1210, 250, 86, 20))
		self.chkSel8_14.setText("")
		self.chkSel8_14.setObjectName("chkSel8_14")
		self.lblName8_14 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_14.setGeometry(QtCore.QRect(1230, 220, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_14.setFont(font)
		self.lblName8_14.setObjectName("lblName8_14")
		self.cmdDisplay8_14 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_14.setGeometry(QtCore.QRect(1230, 270, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_14.setFont(font)
		self.cmdDisplay8_14.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_14.setFlat(True)
		self.cmdDisplay8_14.setObjectName("cmdDisplay8_14")
		self.pbProgram8_15 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_15.setGeometry(QtCore.QRect(90, 430, 141, 31))
		self.pbProgram8_15.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_15.setProperty("value", 24)
		self.pbProgram8_15.setObjectName("pbProgram8_15")
		self.chkSel8_15 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_15.setGeometry(QtCore.QRect(70, 380, 86, 20))
		self.chkSel8_15.setText("")
		self.chkSel8_15.setObjectName("chkSel8_15")
		self.lblName8_15 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_15.setGeometry(QtCore.QRect(90, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_15.setFont(font)
		self.lblName8_15.setObjectName("lblName8_15")
		self.cmdDisplay8_15 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_15.setGeometry(QtCore.QRect(90, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_15.setFont(font)
		self.cmdDisplay8_15.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_15.setFlat(True)
		self.cmdDisplay8_15.setObjectName("cmdDisplay8_15")
		self.pbProgram8_16 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_16.setGeometry(QtCore.QRect(280, 430, 141, 31))
		self.pbProgram8_16.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_16.setProperty("value", 24)
		self.pbProgram8_16.setObjectName("pbProgram8_16")
		self.chkSel8_16 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_16.setGeometry(QtCore.QRect(260, 380, 86, 20))
		self.chkSel8_16.setText("")
		self.chkSel8_16.setObjectName("chkSel8_16")
		self.lblName8_16 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_16.setGeometry(QtCore.QRect(280, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_16.setFont(font)
		self.lblName8_16.setObjectName("lblName8_16")
		self.cmdDisplay8_16 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_16.setGeometry(QtCore.QRect(280, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_16.setFont(font)
		self.cmdDisplay8_16.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_16.setFlat(True)
		self.cmdDisplay8_16.setObjectName("cmdDisplay8_16")
		self.pbProgram8_17 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_17.setGeometry(QtCore.QRect(470, 430, 141, 31))
		self.pbProgram8_17.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_17.setProperty("value", 24)
		self.pbProgram8_17.setObjectName("pbProgram8_17")
		self.chkSel8_17 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_17.setGeometry(QtCore.QRect(450, 380, 86, 20))
		self.chkSel8_17.setText("")
		self.chkSel8_17.setObjectName("chkSel8_17")
		self.lblName8_17 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_17.setGeometry(QtCore.QRect(470, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_17.setFont(font)
		self.lblName8_17.setObjectName("lblName8_17")
		self.cmdDisplay8_17 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_17.setGeometry(QtCore.QRect(470, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_17.setFont(font)
		self.cmdDisplay8_17.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_17.setFlat(True)
		self.cmdDisplay8_17.setObjectName("cmdDisplay8_17")
		self.pbProgram8_18 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_18.setGeometry(QtCore.QRect(660, 430, 141, 31))
		self.pbProgram8_18.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_18.setProperty("value", 24)
		self.pbProgram8_18.setObjectName("pbProgram8_18")
		self.chkSel8_18 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_18.setGeometry(QtCore.QRect(640, 380, 86, 20))
		self.chkSel8_18.setText("")
		self.chkSel8_18.setObjectName("chkSel8_18")
		self.lblName8_18 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_18.setGeometry(QtCore.QRect(660, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_18.setFont(font)
		self.lblName8_18.setObjectName("lblName8_18")
		self.cmdDisplay8_18 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_18.setGeometry(QtCore.QRect(660, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_18.setFont(font)
		self.cmdDisplay8_18.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_18.setFlat(True)
		self.cmdDisplay8_18.setObjectName("cmdDisplay8_18")
		self.pbProgram8_19 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_19.setGeometry(QtCore.QRect(850, 430, 141, 31))
		self.pbProgram8_19.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_19.setProperty("value", 24)
		self.pbProgram8_19.setObjectName("pbProgram8_19")
		self.chkSel8_19 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_19.setGeometry(QtCore.QRect(830, 380, 86, 20))
		self.chkSel8_19.setText("")
		self.chkSel8_19.setObjectName("chkSel8_19")
		self.lblName8_19 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_19.setGeometry(QtCore.QRect(850, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_19.setFont(font)
		self.lblName8_19.setObjectName("lblName8_19")
		self.cmdDisplay8_19 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_19.setGeometry(QtCore.QRect(850, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_19.setFont(font)
		self.cmdDisplay8_19.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_19.setFlat(True)
		self.cmdDisplay8_19.setObjectName("cmdDisplay8_19")
		self.pbProgram8_20 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_20.setGeometry(QtCore.QRect(1040, 430, 141, 31))
		self.pbProgram8_20.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_20.setProperty("value", 24)
		self.pbProgram8_20.setObjectName("pbProgram8_20")
		self.chkSel8_20 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_20.setGeometry(QtCore.QRect(1020, 380, 86, 20))
		self.chkSel8_20.setText("")
		self.chkSel8_20.setObjectName("chkSel8_20")
		self.lblName8_20 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_20.setGeometry(QtCore.QRect(1040, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_20.setFont(font)
		self.lblName8_20.setObjectName("lblName8_20")
		self.cmdDisplay8_20 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_20.setGeometry(QtCore.QRect(1040, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_20.setFont(font)
		self.cmdDisplay8_20.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_20.setFlat(True)
		self.cmdDisplay8_20.setObjectName("cmdDisplay8_20")
		self.pbProgram8_21 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_21.setGeometry(QtCore.QRect(1230, 430, 141, 31))
		self.pbProgram8_21.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_21.setProperty("value", 24)
		self.pbProgram8_21.setObjectName("pbProgram8_21")
		self.chkSel8_21 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_21.setGeometry(QtCore.QRect(1210, 380, 86, 20))
		self.chkSel8_21.setText("")
		self.chkSel8_21.setObjectName("chkSel8_21")
		self.lblName8_21 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_21.setGeometry(QtCore.QRect(1230, 350, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_21.setFont(font)
		self.lblName8_21.setObjectName("lblName8_21")
		self.cmdDisplay8_21 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_21.setGeometry(QtCore.QRect(1230, 400, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_21.setFont(font)
		self.cmdDisplay8_21.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_21.setFlat(True)
		self.cmdDisplay8_21.setObjectName("cmdDisplay8_21")
		self.pbProgram8_22 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_22.setGeometry(QtCore.QRect(90, 560, 141, 31))
		self.pbProgram8_22.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_22.setProperty("value", 24)
		self.pbProgram8_22.setObjectName("pbProgram8_22")
		self.chkSel8_22 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_22.setGeometry(QtCore.QRect(70, 510, 86, 20))
		self.chkSel8_22.setText("")
		self.chkSel8_22.setObjectName("chkSel8_22")
		self.lblName8_22 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_22.setGeometry(QtCore.QRect(90, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_22.setFont(font)
		self.lblName8_22.setObjectName("lblName8_22")
		self.cmdDisplay8_22 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_22.setGeometry(QtCore.QRect(90, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_22.setFont(font)
		self.cmdDisplay8_22.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_22.setFlat(True)
		self.cmdDisplay8_22.setObjectName("cmdDisplay8_22")
		self.pbProgram8_23 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_23.setGeometry(QtCore.QRect(280, 560, 141, 31))
		self.pbProgram8_23.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_23.setProperty("value", 24)
		self.pbProgram8_23.setObjectName("pbProgram8_23")
		self.chkSel8_23 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_23.setGeometry(QtCore.QRect(260, 510, 86, 20))
		self.chkSel8_23.setText("")
		self.chkSel8_23.setObjectName("chkSel8_23")
		self.lblName8_23 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_23.setGeometry(QtCore.QRect(280, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_23.setFont(font)
		self.lblName8_23.setObjectName("lblName8_23")
		self.cmdDisplay8_23 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_23.setGeometry(QtCore.QRect(280, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_23.setFont(font)
		self.cmdDisplay8_23.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_23.setFlat(True)
		self.cmdDisplay8_23.setObjectName("cmdDisplay8_23")
		self.pbProgram8_24 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_24.setGeometry(QtCore.QRect(470, 560, 141, 31))
		self.pbProgram8_24.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_24.setProperty("value", 24)
		self.pbProgram8_24.setObjectName("pbProgram8_24")
		self.chkSel8_24 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_24.setGeometry(QtCore.QRect(450, 510, 86, 20))
		self.chkSel8_24.setText("")
		self.chkSel8_24.setObjectName("chkSel8_24")
		self.lblName8_24 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_24.setGeometry(QtCore.QRect(470, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_24.setFont(font)
		self.lblName8_24.setObjectName("lblName8_24")
		self.cmdDisplay8_24 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_24.setGeometry(QtCore.QRect(470, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_24.setFont(font)
		self.cmdDisplay8_24.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_24.setFlat(True)
		self.cmdDisplay8_24.setObjectName("cmdDisplay8_24")
		self.pbProgram8_25 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_25.setGeometry(QtCore.QRect(660, 560, 141, 31))
		self.pbProgram8_25.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_25.setProperty("value", 24)
		self.pbProgram8_25.setObjectName("pbProgram8_25")
		self.chkSel8_25 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_25.setGeometry(QtCore.QRect(640, 510, 86, 20))
		self.chkSel8_25.setText("")
		self.chkSel8_25.setObjectName("chkSel8_25")
		self.lblName8_25 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_25.setGeometry(QtCore.QRect(660, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_25.setFont(font)
		self.lblName8_25.setObjectName("lblName8_25")
		self.cmdDisplay8_25 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_25.setGeometry(QtCore.QRect(660, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_25.setFont(font)
		self.cmdDisplay8_25.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_25.setFlat(True)
		self.cmdDisplay8_25.setObjectName("cmdDisplay8_25")
		self.pbProgram8_26 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_26.setGeometry(QtCore.QRect(850, 560, 141, 31))
		self.pbProgram8_26.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_26.setProperty("value", 24)
		self.pbProgram8_26.setObjectName("pbProgram8_26")
		self.chkSel8_26 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_26.setGeometry(QtCore.QRect(830, 510, 86, 20))
		self.chkSel8_26.setText("")
		self.chkSel8_26.setObjectName("chkSel8_26")
		self.lblName8_26 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_26.setGeometry(QtCore.QRect(850, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_26.setFont(font)
		self.lblName8_26.setObjectName("lblName8_26")
		self.cmdDisplay8_26 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_26.setGeometry(QtCore.QRect(850, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_26.setFont(font)
		self.cmdDisplay8_26.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_26.setFlat(True)
		self.cmdDisplay8_26.setObjectName("cmdDisplay8_26")
		self.pbProgram8_27 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_27.setGeometry(QtCore.QRect(1040, 560, 141, 31))
		self.pbProgram8_27.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_27.setProperty("value", 24)
		self.pbProgram8_27.setObjectName("pbProgram8_27")
		self.chkSel8_27 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_27.setGeometry(QtCore.QRect(1020, 510, 86, 20))
		self.chkSel8_27.setText("")
		self.chkSel8_27.setObjectName("chkSel8_27")
		self.lblName8_27 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_27.setGeometry(QtCore.QRect(1040, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_27.setFont(font)
		self.lblName8_27.setObjectName("lblName8_27")
		self.cmdDisplay8_27 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_27.setGeometry(QtCore.QRect(1040, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_27.setFont(font)
		self.cmdDisplay8_27.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_27.setFlat(True)
		self.cmdDisplay8_27.setObjectName("cmdDisplay8_27")
		self.pbProgram8_28 = QtWidgets.QProgressBar(self.tbPage8)
		self.pbProgram8_28.setGeometry(QtCore.QRect(1230, 560, 141, 31))
		self.pbProgram8_28.setStyleSheet("QProgressBar\n"
"{\n"
"    border: 1px solid black;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: blue;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}")
		self.pbProgram8_28.setProperty("value", 24)
		self.pbProgram8_28.setObjectName("pbProgram8_28")
		self.chkSel8_28 = QtWidgets.QCheckBox(self.tbPage8)
		self.chkSel8_28.setGeometry(QtCore.QRect(1210, 510, 86, 20))
		self.chkSel8_28.setText("")
		self.chkSel8_28.setObjectName("chkSel8_28")
		self.lblName8_28 = QtWidgets.QLabel(self.tbPage8)
		self.lblName8_28.setGeometry(QtCore.QRect(1230, 480, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.lblName8_28.setFont(font)
		self.lblName8_28.setObjectName("lblName8_28")
		self.cmdDisplay8_28 = QtWidgets.QPushButton(self.tbPage8)
		self.cmdDisplay8_28.setGeometry(QtCore.QRect(1230, 530, 141, 32))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.cmdDisplay8_28.setFont(font)
		self.cmdDisplay8_28.setStyleSheet("QPushButton { background-color : blue; color : black; border: 1px solid black; }")
		self.cmdDisplay8_28.setFlat(True)
		self.cmdDisplay8_28.setObjectName("cmdDisplay8_28")
		self.tabWidget.addTab(self.tbPage8, "")

		self.cmdIniciar = QtWidgets.QPushButton(self.centralWidget)
		self.cmdIniciar.setGeometry(QtCore.QRect(160, 0, 91, 32))
		self.cmdIniciar.setObjectName("cmdIniciar")
		self.cmdPausar = QtWidgets.QPushButton(self.centralWidget)
		self.cmdPausar.setGeometry(QtCore.QRect(250, 0, 91, 32))
		self.cmdPausar.setObjectName("cmdPausar")
		self.cmdDetener = QtWidgets.QPushButton(self.centralWidget)
		self.cmdDetener.setGeometry(QtCore.QRect(340, 0, 91, 32))
		self.cmdDetener.setObjectName("cmdDetener")
		self.cmdCargar = QtWidgets.QPushButton(self.centralWidget)
		self.cmdCargar.setGeometry(QtCore.QRect(20, 0, 141, 32))
		self.cmdCargar.setObjectName("cmdCargar")
		MainWindow.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 1536, 22))
		self.menuBar.setObjectName("menuBar")
		self.menuArchivo = QtWidgets.QMenu(self.menuBar)
		self.menuArchivo.setObjectName("menuArchivo")
		self.menuVista = QtWidgets.QMenu(self.menuBar)
		self.menuVista.setObjectName("menuVista")
		self.menuCircuito = QtWidgets.QMenu(self.menuBar)
		self.menuCircuito.setObjectName("menuCircuito")
		self.menuHerramientas = QtWidgets.QMenu(self.menuBar)
		self.menuHerramientas.setObjectName("menuHerramientas")
		self.menuReportes = QtWidgets.QMenu(self.menuBar)
		self.menuReportes.setObjectName("menuReportes")
		MainWindow.setMenuBar(self.menuBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)
		self.actionhh = QtWidgets.QAction(MainWindow)
		self.actionhh.setObjectName("actionhh")
		self.actionjjl = QtWidgets.QAction(MainWindow)
		self.actionjjl.setObjectName("actionjjl")
		self.actionhh_2 = QtWidgets.QAction(MainWindow)
		self.actionhh_2.setObjectName("actionhh_2")
		self.actionjjk = QtWidgets.QAction(MainWindow)
		self.actionjjk.setObjectName("actionjjk")
		self.actionjkjkj = QtWidgets.QAction(MainWindow)
		self.actionjkjkj.setObjectName("actionjkjkj")
		self.menuArchivo.addAction(self.actionhh)
		self.menuVista.addAction(self.actionjjl)
		self.menuCircuito.addAction(self.actionhh_2)
		self.menuHerramientas.addAction(self.actionjjk)
		self.menuReportes.addAction(self.actionjkjkj)
		self.menuBar.addAction(self.menuArchivo.menuAction())
		self.menuBar.addAction(self.menuVista.menuAction())
		self.menuBar.addAction(self.menuCircuito.menuAction())
		self.menuBar.addAction(self.menuHerramientas.menuAction())
		self.menuBar.addAction(self.menuReportes.menuAction())


		#self.retranslateUi()
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


		MainWindow.showEvent = self.showEvent
		MainWindow.closeEvent = self.closeEvent


		self.cmdIniciar.clicked.connect(self.on_cmdIniciar_clicked)

		self.cmdPausar.clicked.connect(self.on_cmdPausar_clicked)

		self.cmdDetener.clicked.connect(self.on_cmdDetener_clicked)

		self.cmdCargar.clicked.connect(self.on_cmdCargarP_clicked)


		self.cmdDisplay1_1.clicked.connect(self.on_cmdDisplay1_clicked)
		self.cmdDisplay1_2.clicked.connect(self.on_cmdDisplay2_clicked)
		'''
		self.cmdDisplay1_3.clicked.connect(self.on_cmdDisplay3_clicked)
		self.cmdDisplay1_4.clicked.connect(self.on_cmdDisplay4_clicked)
		self.cmdDisplay1_5.clicked.connect(self.on_cmdDisplay5_clicked)
		self.cmdDisplay1_6.clicked.connect(self.on_cmdDisplay6_clicked)
		self.cmdDisplay1_7.clicked.connect(self.on_cmdDisplay7_clicked)
		self.cmdDisplay1_8.clicked.connect(self.on_cmdDisplay8_clicked)
		self.cmdDisplay1_9.clicked.connect(self.on_cmdDisplay9_clicked)
		self.cmdDisplay1_10.clicked.connect(self.on_cmdDisplay10_clicked)
		self.cmdDisplay1_11.clicked.connect(self.on_cmdDisplay11_clicked)
		self.cmdDisplay1_12.clicked.connect(self.on_cmdDisplay12_clicked)
		self.cmdDisplay1_13.clicked.connect(self.on_cmdDisplay13_clicked)
		self.cmdDisplay1_14.clicked.connect(self.on_cmdDisplay14_clicked)
		self.cmdDisplay1_15.clicked.connect(self.on_cmdDisplay15_clicked)
		self.cmdDisplay1_16.clicked.connect(self.on_cmdDisplay16_clicked)
		self.cmdDisplay1_17.clicked.connect(self.on_cmdDisplay17_clicked)
		self.cmdDisplay1_18.clicked.connect(self.on_cmdDisplay18_clicked)
		self.cmdDisplay1_19.clicked.connect(self.on_cmdDisplay19_clicked)
		self.cmdDisplay1_20.clicked.connect(self.on_cmdDisplay20_clicked)
		self.cmdDisplay1_21.clicked.connect(self.on_cmdDisplay21_clicked)
		self.cmdDisplay1_22.clicked.connect(self.on_cmdDisplay22_clicked)
		self.cmdDisplay1_23.clicked.connect(self.on_cmdDisplay23_clicked)
		self.cmdDisplay1_24.clicked.connect(self.on_cmdDisplay24_clicked)
		self.cmdDisplay1_25.clicked.connect(self.on_cmdDisplay25_clicked)
		self.cmdDisplay1_26.clicked.connect(self.on_cmdDisplay26_clicked)
		self.cmdDisplay1_27.clicked.connect(self.on_cmdDisplay27_clicked)
		self.cmdDisplay1_28.clicked.connect(self.on_cmdDisplay28_clicked)
		'''

		self.MainWindow = MainWindow


		for i in range(1,29):
			_translate = QtCore.QCoreApplication.translate

			MainWindow.setWindowTitle(_translate("MainWindow", "Ditsa Net 4.0"))

			mylblName = self.MainWindow.findChild(QtWidgets.QLabel,"lblName1_"+str(i))
			mylblName.setText(_translate("MainWindow","MF"+str(i)))

			mylblName2 = self.MainWindow.findChild(QtWidgets.QLabel,"lblName2_"+str(i))
			mylblName2.setText(_translate("MainWindow","MF"+str(i)))

			mylblName3 = self.MainWindow.findChild(QtWidgets.QLabel,"lblName3_"+str(i))
			mylblName3.setText(_translate("MainWindow","MF"+str(i)))

			mylblName4 = self.MainWindow.findChild(QtWidgets.QLabel,"lblName4_"+str(i))
			mylblName4.setText(_translate("MainWindow","MF"+str(i)))

			mylblName5 = self.MainWindow.findChild(QtWidgets.QLabel,"lblName5_"+str(i))
			mylblName5.setText(_translate("MainWindow","MF"+str(i)))

			mylblName6 = self.MainWindow.findChild(QtWidgets.QLabel,"lblName6_"+str(i))
			mylblName6.setText(_translate("MainWindow","MF"+str(i)))

			mylblName7 = self.MainWindow.findChild(QtWidgets.QLabel,"lblName7_"+str(i))
			mylblName7.setText(_translate("MainWindow","MF"+str(i)))

			mylblName8 = self.MainWindow.findChild(QtWidgets.QLabel,"lblName8_"+str(i))
			mylblName8.setText(_translate("MainWindow","MF"+str(i)))


			#mylblPage = self.MainWindow.findChild(QtWidgets.QLabel,"lblPage1")
			#mylblPage.setText(_translate("MainWindow", "Mesa 1"))

			self.lblPage1.setText(_translate("MainWindow", "Mesa 1"))
			self.lblPage2.setText(_translate("MainWindow", "Mesa 2"))
			self.lblPage3.setText(_translate("MainWindow", "Mesa 3"))
			self.lblPage4.setText(_translate("MainWindow", "Mesa 4"))
			self.lblPage5.setText(_translate("MainWindow", "Mesa 5"))
			self.lblPage6.setText(_translate("MainWindow", "Mesa 6"))
			self.lblPage7.setText(_translate("MainWindow", "Mesa 7"))
			self.lblPage8.setText(_translate("MainWindow", "Mesa 8"))

			mypbProgram = self.MainWindow.findChild(QtWidgets.QProgressBar,"pbProgram1_"+str(i))
			mypbProgram.setToolTip(_translate("MainWindow", "Nombre: MF"+str(i)+"\n"
	"Estado: No Conectado\n"
	"Corriente: 25.0\n"
	"Voltaje: 58.0\n"
	"Temperatura: 24.8\n"
	"AH: 0.0\n"
	"Nombre de Programa: 001-SGL\n"
	"Indice del Programa: 501\n"
	"Paso del Programa: 1\n"
	"Step time: 00:01\n"
	"Tiempo Restante: 00:00\n"
	"Tiempo Finalizado: 12/04/2019 20:13\n"
	"ServerID: 0\n"
	"FirstN: 0"))
			myDisplay = self.MainWindow.findChild(QtWidgets.QPushButton,"cmdDisplay1_"+str(i))
			myDisplay.setToolTip(_translate("MainWindow","Nombre: MF"+str(i)+"\n"
	"Estado: No Conectado\n"
	"Corriente: 25.0\n"
	"Voltaje: 58.0\n"
	"Temperatura: 24.8\n"
	"AH: 0.0\n"
	"Nombre de Programa: 001-SGL\n"
	"Indice del Programa: 501\n"
	"Paso del Programa: 1\n"
	"Step time: 00:01\n"
	"Tiempo Restante: 00:00\n"
	"Tiempo Finalizado: 12/04/2019 20:13\n"
	"ServerID: 0\n"
	"FirstN: 0"))
			myDisplay.setText(_translate("MainWindow", "Voltage: 12.6V"))
			mytbPage = self.MainWindow.findChild(QtWidgets.QWidget,"tbPage"+str(i))
			self.tabWidget.setTabText(self.tabWidget.indexOf(mytbPage), _translate("MainWindow", "Mesa "+str(i)))
			
		self.cmdIniciar.setText(_translate("MainWindow", "Iniciar"))
		self.cmdPausar.setText(_translate("MainWindow", "Pausar"))
		self.cmdDetener.setText(_translate("MainWindow", "Detener"))
		self.cmdCargar.setText(_translate("MainWindow", "Cargar Programa"))
		self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
		self.menuVista.setTitle(_translate("MainWindow", "Vista"))
		self.menuCircuito.setTitle(_translate("MainWindow", "Circuito"))
		self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
		self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
		self.actionhh.setText(_translate("MainWindow", "hh"))
		self.actionjjl.setText(_translate("MainWindow", "jjl"))
		self.actionhh_2.setText(_translate("MainWindow", "hh"))
		self.actionjjk.setText(_translate("MainWindow", "jjk"))
		self.actionjkjkj.setText(_translate("MainWindow", "jkjkj"))


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Ditsa Net 4.0"))
		self.lblPage1.setText(_translate("MainWindow", "Mesa 1"))
		
		self.lblName1_1.setText(_translate("MainWindow", "MF1"))
		self.pbProgram1_1.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
		self.cmdDisplay1_1.setToolTip(_translate("MainWindow", "Nombre: MF1\n"
"Estado: No Conectado\n"
"Corriente: 25.0\n"
"Voltaje: 58.0\n"
"Temperatura: 24.8\n"
"AH: 0.0\n"
"Nombre de Programa: 001-SGL\n"
"Indice del Programa: 501\n"
"Paso del Programa: 1\n"
"Step time: 00:01\n"
"Tiempo Restante: 00:00\n"
"Tiempo Finalizado: 12/04/2019 20:13\n"
"ServerID: 0\n"
"FirstN: 0"))
		self.cmdDisplay1_1.setText(_translate("MainWindow", "Voltage: 12.6V"))
	
		self.cmdIniciar.setText(_translate("MainWindow", "Iniciar"))
		self.cmdPausar.setText(_translate("MainWindow", "Pausar"))
		self.cmdDetener.setText(_translate("MainWindow", "Detener"))
		self.cmdCargar.setText(_translate("MainWindow", "Cargar Programa"))
		self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
		self.menuVista.setTitle(_translate("MainWindow", "Vista"))
		self.menuCircuito.setTitle(_translate("MainWindow", "Circuito"))
		self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
		self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
		self.actionhh.setText(_translate("MainWindow", "hh"))
		self.actionjjl.setText(_translate("MainWindow", "jjl"))
		self.actionhh_2.setText(_translate("MainWindow", "hh"))
		self.actionjjk.setText(_translate("MainWindow", "jjk"))
		self.actionjkjkj.setText(_translate("MainWindow", "jkjkj"))


	def unitializeCheckbox(self):
		for i in range(1,28):
			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel1_"+str(i))
			myCheck.setVisible(False)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel2_"+str(i))
			myCheck.setVisible(False)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel3_"+str(i))
			myCheck.setVisible(False)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel4_"+str(i))
			myCheck.setVisible(False)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel5_"+str(i))
			myCheck.setVisible(False)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel6_"+str(i))
			myCheck.setVisible(False)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel7_"+str(i))
			myCheck.setVisible(False)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel8_"+str(i))
			myCheck.setVisible(False)
			myCheck.setCheckState(QtCore.Qt.Unchecked)


	def initializeCheckbox(self):
		for i in range(1,28):
			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel1_"+str(i))
			myCheck.setVisible(True)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel2_"+str(i))
			myCheck.setVisible(True)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel3_"+str(i))
			myCheck.setVisible(True)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel4_"+str(i))
			myCheck.setVisible(True)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel5_"+str(i))
			myCheck.setVisible(True)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel6_"+str(i))
			myCheck.setVisible(True)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel7_"+str(i))
			myCheck.setVisible(True)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel8_"+str(i))
			myCheck.setVisible(True)
			myCheck.setCheckState(QtCore.Qt.Unchecked)

	def showEvent(self, event):
		print("show")
		self.display()

		self.unitializeCheckbox()

		self.fillWithSettings()

		print("Iniciar Actualizar")
		self.dataThread = DataListenerMemory(self.testsCallback)
		self.dataThread.start()

	def closeEvent(self, event):
		print("close")

		print("Detener Actualizar")
		self.dataThread.stop()

	def on_cmdSeleccionar_clicked(self):
		self.initializeCheckbox()

	def on_cmdIniciar_clicked(self):
		print("Iniciar")

		for i in range(1,3):
			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel1_"+str(i))

			if myCheck.isChecked() == True:
				BCmb.runClient(useHostname, i)


	def on_cmdPausar_clicked(self):
		print("Pausar")

		for i in range(1,3):
			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel1_"+str(i))

			if myCheck.isChecked() == True:
				BCmb.pauseClient(useHostname, i)


	def on_cmdDetener_clicked(self):
		print("Detener")

		for i in range(1,3):
			myCheck = self.MainWindow.findChild(QtWidgets.QCheckBox, "chkSel1_"+str(i))

			if myCheck.isChecked() == True:
				BCmb.stopClient(useHostname, i)

	def on_cmdCargarP_clicked(self):
		print("CargarPr")
		self.ProgramWindow = QtWidgets.QDialog()
		self.ProgramWindow.setModal(True)
		self.ui = Ui_WindowCh()
		self.ui.setupUi(self.ProgramWindow)
		self.ProgramWindow.show()

	WAIT_SECONDS = 1
	count = 0
	count1 = 0
	count2 = 0

	def display(self):
		print("C:")
		print(self.count)
		if self.count > 2:
			memoryData = BCmb.memoryDataClient(useHostname)
			
			for i in range (shared.devStart, shared.devStop+1):
				address = i
			
				if memoryData!= None:

					print("ValueM:")
					print(memoryData)

					TempData = memoryData[address-1].split(',')
					print(TempData)

					dat1 = str(TempData[0]).replace('{','')
					print(dat1)

					if dat1 == 'True':
						TempData[8] = str(TempData[8]).replace('}','')
						TempData[0] = True

						shared.DEV[address][0] = TempData[0]
						#we store current
						shared.DEV[address][1] = str(TempData[1].replace('I',''))
						#we store voltage
						shared.DEV[address][2] = str(TempData[2].replace('V',''))
						#we store temperature
						shared.DEV[address][3] = str(TempData[3].replace('T',''))
						#we store step number and type
						shared.DEV[address][4] = str(TempData[4].replace('P',''))
						#we store time of current step
						shared.DEV[address][5] = str(TempData[5].replace('t',''))
						#we store current time program
						shared.DEV[address][6] = str(TempData[6].replace('Tt',''))
						#we store the total time program
						shared.DEV[address][7] = str(TempData[7].replace('TT',''))
						#we store the total time program
						shared.DEV[address][8] = str(TempData[8].replace('',''))

						if shared.DEV[address][8] == '':
							print("Dato3")

					if dat1 == 'False}':
						TempData[0] = str(TempData[0]).replace('}','')
						shared.DEV[address][0] = False
						print("FalsePing")
					
					print(TempData)
				

		self.count = self.count + 1
		print(time.ctime())
		if shared.DEV[1][0] == True:
			self.count1 = 0
			newstr1 = ""
			self.currentProgressB()
			if self.stateDisplay1 == 1:
				#current
				newstr1 = str(shared.DEV[1][1])+" A"
			if self.stateDisplay1 == 2:
				#voltage
				newstr1 = str(shared.DEV[1][2]) + " V"
			if self.stateDisplay1 == 3:
				#temperature
				newstr1 = str(shared.DEV[1][3]) + " °C"
			self.cmdDisplay1_1.setText(str(newstr1))
		else:
			self.count1 = self.count1 + 1
			if self.count1 > 5:
				print("FAILCOMM1")
				newstr1 = ""
				newstr1 = "FailComm"
				self.cmdDisplay1_1.setText(str(newstr1))


		if shared.DEV[2][0] == True:
			self.count2 = 0
			newstr2 = ""
			if self.stateDisplay2 == 1:
				#current
				newstr2 = str(shared.DEV[2][1])+" A"
			if self.stateDisplay2 == 2:
				#voltage
				newstr2 = str(shared.DEV[2][2]) + " V"
			if self.stateDisplay2 == 3:
				#temperature
				newstr2 = str(shared.DEV[2][3])+ " °C"
			self.cmdDisplay1_2.setText(str(newstr2))
		else:
			self.count2 = self.count2 + 1
			if self.count2 > 5:
				print("FAILCOMM2")
				newstr2 = ""
				newstr2 = "FailComm"
				self.cmdDisplay1_2.setText(str(newstr2))

		threading.Timer(self.WAIT_SECONDS, self.display).start()


	stateDisplay1 = 1
	def on_cmdDisplay1_clicked(self):
		print("Display 1")
		self.stateDisplay1 = self.stateDisplay1 + 1
		if self.stateDisplay1==4 :
			self.stateDisplay1 = 1
		print(self.stateDisplay1)


	stateDisplay2 = 1
	def on_cmdDisplay2_clicked(self):
		print("Display 2")
		self.stateDisplay2 = self.stateDisplay2 + 1
		if self.stateDisplay2==4 :
			self.stateDisplay2 = 1
		print(self.stateDisplay2)


	def currentProgressB(self):
		val = float(shared.DEV[1][6]) * 100 / float(shared.DEV[1][7])
		#val = float(shared.DEV[1][6])
		print("VAL")
		print(val)
		val2 = float(format(val,'.1f'))
		print(val2)
		#time.sleep(.1)
		self.pbProgram1_1.setValue(val2)

	def testsCallback(self, msg):
		#for i in range(1,3):
		#address = 1
		if "DL[X]" in msg:
			msg = msg.replace("DL[PASS]:","")

			#myDisplay1 = self.MainWindow.findChild(QtWidgets.QPushButton, "cmdDisplay1_"+str(i))
			print("ENT")
			self.cmdDisplay1_1.repaint()
			self.cmdDisplay1_1.update()
			self.cmdDisplay1_1.setUpdatesEnabled(True)

			self.cmdDisplay1_2.repaint()
			self.cmdDisplay1_2.update()
			self.cmdDisplay1_2.setUpdatesEnabled(True)

			#self.currentProgressB()
			#self.pbProgram1_1.repaint()

			#myDisplay2.repaint()
			#myDisplay2.update()
			#myDisplay2.setUpdatesEnabled(True)
			'''
			#self.cmdDisplay1.setText(str(newstr1))
			self.cmdDisplay1_1.repaint()
			self.cmdDisplay1_1.update()
			self.cmdDisplay1_1.setUpdatesEnabled(True)

			#self.cmdDisplay2.setText(str(newstr2))
			self.cmdDisplay1_2.repaint()
			self.cmdDisplay1_2.update()
			self.cmdDisplay1_2.setUpdatesEnabled(True)
			'''
		'''

			newstr = msg
			print (newstr)


			self.cmdDisplay1.setText(str(newstr))
			self.cmdDisplay1.repaint()
			self.cmdDisplay1.update()
			self.cmdDisplay1.setUpdatesEnabled(True)
		'''

	def fillWithSettings(self):
		print("fillWithSettingsOfEditor")
		settings = QtCore.QSettings('Settings/archivo.ini', QtCore.QSettings.NativeFormat)
		if settings.value('Settings/archivo.ini')!='':
			self.settingsList = settings.value("mylist")
			self.settingsLabel = settings.value("mylabel")
			self.settingsRowCol = settings.value("rowcol")
			print("SettingsList:",self.settingsList)
			print("SettingsLable:",self.settingsLabel)
			print("SettingsRowCol:",self.settingsRowCol)
		#print(shared.DEV[0][8])
		#for i in range(1, 9):

		#	print(shared.DEV[0][8])

			#myName = self.MainWindow.findChild(QtWidgets.QLabel, "lblPage1")
			#myName.setText("Mesa 1")
			#myName2 = self.lblPage1.text()
			#print(myName2)

			#myName = self.MainWindow.findChild(QtWidgets.QLabel, "lblPage8")
			#myName.setText("Viri")

			#myDisplay = self.MainWindow.findChild(QtWidgets.QPushButton, "cmdDisplay1")
			#myDisplay.setText("Page 34")

			#myProgress = self.MainWindow.findChild(QtWidgets.QProgressBar, "pbProgram1")
			#myProgress.setValue(10)

		#	myTab = self.MainWindow.findChild(QtWidgets.QWidget, "tab_2")
		#	self.tabWidget.setTabText(self.tabWidget.indexOf(myTab), "Mesa 2")

			#self.set

		#	print("Page "+str(i))
		#for i in range(1,28):
		#	print("Name "+str(i))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	#MainWindow.setWindowTitle('Ditsa Net 4.0')
	#MainWindow.setWindowIcon(QtGui.QIcon('imagen'))
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)

	MainWindow.show()
	sys.exit(app.exec_())

