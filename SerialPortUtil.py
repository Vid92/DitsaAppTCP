import logging

from time import sleep, time

import usb.core
import usb.util

import serial
import serial.tools.list_ports

import os
import appsettings

import StringUtils

def portIsOpen(name):
    try: 
        ser = serial.Serial(name, 9600, timeout=1)
        if ser.isOpen():
            return True
        else:
            return False
    except:
        return True
    # test

def getPortNames():
    print("list")
    ports = list(serial.tools.list_ports.comports())
    result = []
    for port in ports:
        s = port.device
        result.append(s)
    return result

def getPortNamesBy_VID_PID(vid, pid):
    vid_pid = "{:04x}:{:04x}".format(vid, pid)
    mylist = serial.tools.list_ports.grep(vid_pid)
    ports = list(mylist)
    result = []
    for port in ports:
        s = port.device
        result.append(s)
    return result

def getPortByName(name):
    try:
        ser = serial.Serial(name, 9600, timeout=1)
        print(ser)
        if not ser.isOpen():
            return None
        else:
            return ser
    except:
        return None

def getFirstPortByVID_PID(vid, pid):
    vid_pid = "{:04x}:{:04x}".format(vid, pid)
    mylist = serial.tools.list_ports.grep(vid_pid)
    ports = list(mylist)
    name = None
    result = []
    for port in ports:
        name = port.device
        #print(port.serial_number)
        s = port.device
        result.append(s)
        break
    
    try:
        ser = serial.Serial(name, 9600, timeout=1)
        if not ser.isOpen():
            return None
        else:
            return ser
    except:
        return None

def getFirstSerialNumberByVID_PID(vid, pid):
    vid_pid = "{:04x}:{:04x}".format(vid, pid)
    mylist = serial.tools.list_ports.grep(vid_pid)
    ports = list(mylist)
    sn = None
    result = []
    for port in ports:
        sn = port.serial_number
        result.append(sn)
        break
    
    try:
        
        if len(result)==0:
            return None
        else:
            return sn
    except:
        return None


def getPortBySerialNumber(serialnumber):
    try:
        ports = list(serial.tools.list_ports.comports())
        device_name = None
        serial_number = None
        for port in ports:
            device_name = port.device
            serial_number = port.serial_number
            
            if not StringUtils.isNoneOrEmpty(serialnumber):
                if serial_number == serialnumber:
                    ser = serial.Serial(device_name, 9600, timeout=1)
                    break

        if not ser.isOpen():
            return None
        else:
            return ser
    except:
        return None

def doesPortExistsBySerialNumber(serialnumber):
    result = False
    try:
        ports = list(serial.tools.list_ports.comports())
        #device_name = None
        serial_number = None
        for port in ports:
            serial_number = port.serial_number
            
            if not StringUtils.isNoneOrEmpty(serialnumber):
                if serial_number == serialnumber:
                    result = True
                    break
        return result
    except:
        return result

if __name__ == "__main__":
    #print(getPortNames())
    #print(portIsOpen('/dev/cu.usbserial-AH05R7EJ'))
    idVendor=0x0403
    idProduct=0x6001
    
    #print(getPortNamesBy_VID_PID(idVendor, idProduct))
    #print(getPortByName('/dev/cu.usbserial-AH05R7EJ'))
    #AH05R7EJ
    #AH05R7EK
    #print(getPortBySerialNumber('AH05R7EJ'))
    #print(getFirstPortByVID_PID(idVendor, idProduct))
    #idVendor_idProduct='0cd5:0003'
    
    print(getPortBySerialNumber(appsettings.FTDIpic32_serialNumber))
