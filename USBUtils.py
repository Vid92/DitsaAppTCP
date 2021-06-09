from time import sleep, time

import usb.core
import usb.util

import StringUtils
import appsettings
    
def labjackIsPresent():
    isPresent = usb.core.find(idVendor=appsettings.LabJack_idVendor, idProduct=appsettings.LabJack_idProduct)
    if not isPresent:
        raise Exception("LabJackError", "No LabJack is hooked on!")
        #return False
    else:
        return True

def barcodescannerIsPresent():
    isPresent = usb.core.find(idVendor=appsettings.BarcodeScanner_idVendor, idProduct=appsettings.BarcodeScanner_idProduct)
    if not isPresent:
        return False
    else:
        return True

def getvidpidString(vid, pid):
    idVendorStr = ''.join('{:04X}'.format(vid).lower())
    idProductStr = ''.join('{:04X}'.format(pid).lower())
    vidpidStr = idVendorStr+':'+idProductStr
    return vidpidStr

if __name__ == '__main__':
    print("demo")
    #print(scanif.labjackIsPresent())
    #print(scanif.barcodescannerIsPresent())
    #print(ftdiIsPresent("4"))
    #print(scanif.cp2104IsPresent())
