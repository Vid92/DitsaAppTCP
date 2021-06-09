import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QScrollBar, QApplication, QWidget, QMainWindow
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QDesktopServices
from PyQt5.QtCore import QEventLoop, QByteArray, Qt, QUrl, pyqtSignal, pyqtSlot, QObject, QTimer, QElapsedTimer, QTime

serial_number = None

# constants that will indicate a pin state
LOW = 0
HIGH = 1

lock_uart = threading.Lock() # lock will be used as a lock for the UART
lock_memory = threading.Lock() # lock will be used as a lock for the memory

lock_client = threading.Lock()	#lock will be used as a lock for the client

#numero de modulos que tendra el gabinete
devStart = 1
devStop = 16


DA_PI = [] #todos los modulos
ON_PI = [] #solo los que dieron TRUE
RE_PI = [] #modulos reales en interfaz

#la cantidad de DEV_ADDR dependera de cuantos dip. sean por raspb(15aprx)
DEV_ADDR = [
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

#solo en shared de ubuntu tendra nameProgram
#ping #I #V #T #AH #AC #P #SOFF #t #Tt #TT #nameProgram #S #auxsavedatas #Name #Show #Address
DEV = [
    #[False, '', '', '', '', '', '', '', ''],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 1],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 2],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 3],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 4], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 5], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 6], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 7], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 8], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 9], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 10], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 11], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 12], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 13], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 14], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 15], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 16], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 17], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 18], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 19], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 20], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 21],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 22],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 23],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 24],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 25],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 26],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 27],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 28],

    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 29],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 30],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 31],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 32], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 33], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 34], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 35], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 36], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 37], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 38], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 39], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 40], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 41], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 42], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 43], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 44], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 45], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 46], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 47], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 48], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 49],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 50],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 51],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 52],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 53],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 54],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 55],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 56], 

    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 57],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 58],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 59],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 60], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 61], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 62], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 63], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 64], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 65], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 66], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 67], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 68], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 69], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 70], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 71], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 72], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 73], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 74], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 75], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 76], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 77],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 78],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 79],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 80],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 81],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 82],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 83],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 84],

    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 85],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 86],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 87],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 88], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 89], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 90], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 91], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 92], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 93], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 94], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 95], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 96], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 97], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 98], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 99], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 100], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 101], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 102], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 103], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 104], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 105],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 106],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 107],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 108],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 109],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 110],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 111],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 112], 
   
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 113],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 114],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 115],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 116], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 117], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 118], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 119], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 120], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 121], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 122], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 123], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 124], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 125], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 126], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 127], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 128], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 129], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 130], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 131], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 132], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 133],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 134],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 135],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 136],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 137],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 138],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 139],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 140],  

	[False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 141],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 142],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 143],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 144], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 145], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 146], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 147], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 148], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 149], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 150], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 151], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 152], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 153], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 154], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 155], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 156], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 157], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 158], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 159], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 160], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 161],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 162],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 163],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 164],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 165],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 166],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 167],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 168],

    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 169],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 170],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 171],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 172], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 173], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 174], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 175], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 176], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 177], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 178], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 179], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 180], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 181], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 182], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 183], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 184], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 185], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 186], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 187], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 188], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 189],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 190],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 191],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 192],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 193],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 194],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 195],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 196], 
   
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 197],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 198],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 199],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 200], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 201], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 202], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 203], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 204], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 205], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 206], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 207], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 208], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 209], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 210], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 211], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 212], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 213], 
	[False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 214], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 215], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 216], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 217],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 218],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 219],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 220],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 221],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 222],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 223],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 224],

	[False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 225],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 226],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 227],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 228], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 229], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 230], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 231], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 232], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 233], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 234], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 235], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 236], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 237], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 238], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 239], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 240], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 241], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 242], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 243], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 244], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 245],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 246],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 247],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 248],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 249],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 250],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 251],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 252], 
   
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 253],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 254],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 255],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 256], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 257], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 258], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 259], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 260], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 261], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 262], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 263], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 264], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 265], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 266], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 267], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 268], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 269], 
	[False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 270], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 271], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 272], 
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 273],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 274],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 275],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 276],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 277],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 278],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 279],
    [False, '', '', '', '', '', '', '', '', '', '', 'S', True,'', 280],
]


'''
[1-28]
[29-56]
[59-84]
[85-112]
[113-140]
[141-168]
[169-196]
[197-224]
'''


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def dec2str(number, places):
    return '{:.2f}'.format(number)

def CenterWidgets(widget:QWidget):
    screenGeometry =  QApplication.desktop().screenGeometry()
    x = (screenGeometry.width() - widget.width())/ 2
    y = (screenGeometry.height()- widget.height())/ 2
    widget.move(x, y)
