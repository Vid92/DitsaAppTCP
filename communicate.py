import sys
import os
import time
from datetime import datetime
import threading

from PyQt5 import QtCore, QtGui, QtWidgets

#Frank

# Create the class 'Communicate'. The instance
# from this class shall be used later on for the
# signal/slot mechanism.
class Communicate(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal(str)
    myGUI_signal_list = QtCore.pyqtSignal(list)
    #myGUI_slot = QtCore.pyqtSlot(str)
''' End class '''
