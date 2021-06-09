import os
from datetime import time, date, datetime, timedelta
from enum import Enum
from time import sleep, time
from pathlib import Path

import appsettings
import StringUtils


class IndividualReport():
    home = str(Path.home())
    #if appsettings.useDesktopToSaveReports:
    file_path = '/home/pi/DitsaNetServer/FormationDataFiles/'
    #else:
    #file_path = os.getcwd() + '/TestLogs/'

    file_name = None
    address_number = None
    date_created = None
    date_modified = None
    text_to_print = ""
    
    def __init__(self):
        try:
            os.makedirs(self.file_path)
        except OSError:
            print ("Creation of the directory %s failed" % self.file_path)
        else:
            print ("Successfully created the directory %s" % self.file_path)


    def begin(self):
        temp = ""
        self.text_to_print = ""
        #st = self.create_timestamp()
        st = ""
        temp += self.append(str(st)+"Date"+","+"Current"+","+"Voltage"+","+"Temperature"+","+"Amper/Hour"+","+"Amper Acu."+","+"Step"+","+"Step State"+","+"Time"+","+"Current Time"+","+"Total Time"+","+"Status\r\n")
        #temp += self.append(str(st)+" **************************************************************************\r\n")
        #st = self.create_timestamp()
        #temp += self.append(str(st)+" ****************************** REPORT BEGIN ******************************\r\n")
        #st = self.create_timestamp()
        ltext = 74
        lsn = len(self.address_number)+6
        spaces = (ltext-lsn)/2
        remBanner = (ltext-lsn)%2
        strBanner = ""
        strFillBanner = ""
        #for n in range(0,int(spaces)):
        #   strBanner+="*"
        #for n in range(0,int(remBanner)):
        #   strFillBanner+="*"
        #temp += self.append(str(st)+" "+strBanner+" SN: ")
        #temp += self.append(self.address_number + " ")
        #temp += self.append(strBanner+strFillBanner+"\r\n")
        #st = self.create_timestamp()
        #temp += self.append(str(st)+" **************************************************************************\r\n")
        self.text_to_print += temp
        return temp
    
    def end(self):
        temp = ""
        st = self.create_timestamp()
        temp += self.append(str(st)+" **************************************************************************\r\n")
        st = self.create_timestamp()
        temp += self.append(str(st)+" ******************************* REPORT END *******************************\r\n")
        st = self.create_timestamp()
        temp += self.append(str(st)+" **************************************************************************\r\n\r\n")
        self.text_to_print += temp
        return temp
    
    def append(self, text):
        if self.address_number == None:
            raise Exception("IndividualReportError", "No Serial Number as FileName was Assigned!")
        if os.path.isfile(self.file_name): # if file exists
            file = open(self.file_name, "a+")  # we append
            file.write(text)
            file.close()
        else:
            file = open(self.file_name, "w+") # we create a new file
            file.write(text)
            file.close()
        return text
    
    def appendWithTimeStamp(self, text):
        if self.address_number == None:
            raise Exception("IndividualReportError", "No Serial Number as FileName was Assigned!")
        st = self.create_timestamp()
        temp = str(st)+" "+ text +  "\r\n"
        self.append(temp)
        self.text_to_print += temp
        return temp
    
    def appendWithTimeStampUsingFile(self, text, file):
        if not StringUtils.isNoneOrEmpty(file):
            self.address_number = file
            self.file_name = self.file_path + self.address_number + '.xls'   #'.txt'

        if not os.path.exists(self.file_name):
            self.begin()

        st = self.create_timestamp()
        temp = str(st)+" "+ text +  "\r\n"
        self.append(temp)
        self.text_to_print += temp
        return temp

    def create_timestamp(self):
        now = datetime.now()
        st = now.strftime('%Y-%m-%d %H:%M:%S') #+ ('.%04d' % (now.microsecond / 100))
        #print(st)
        return st

    def print(self):
        return self.text_to_print

class MainReport:
    home = str(Path.home())
    #if appsettings.useDesktopToSaveReports:
    file_path = home +'/TestLogs/'
    #else:
    #file_path = os.getcwd() + '/TestLogs/'
    file_name = None
    address_number = None
    date_created = None
    date_modified = None
    text_to_print = ""

    def __init__(self):
        try:
            os.makedirs(self.file_path)
        except OSError:
            print ("Creation of the directory %s failed" % self.file_path)
        else:
            print ("Successfully created the directory %s" % self.file_path)

        self.file_name = self.file_path+'mainlog.txt'
        self.text_to_print = ""

    def begin(self):
        temp = ""
        self.text_to_print = ""
        st = self.create_timestamp()
        temp += self.append(str(st)+" **************************************************************************\r\n")
        st = self.create_timestamp()
        temp += self.append(str(st)+" **************************** MAIN REPORT BEGIN ***************************\r\n")
        st = self.create_timestamp()
        temp += self.append(str(st)+" **************************************************************************\r\n")
        self.text_to_print += temp
        return temp

    def end(self):
        temp = ""
        st = self.create_timestamp()
        temp += self.append(str(st)+" **************************************************************************\r\n")
        st = self.create_timestamp()
        temp += self.append(str(st)+" ***************************** MAIN REPORT END ****************************\r\n")
        st = self.create_timestamp()
        temp += self.append(str(st)+" **************************************************************************\r\n\r\n")
        self.text_to_print += temp
        return temp

    def append(self, text):

        if os.path.isfile(self.file_name): # if file exists
            file = open(self.file_name, "a+")  # we append
            file.write(text)
            file.close()
        else:
            file = open(self.file_name, "w+") # we create a new file
            file.write(text)
            file.close()
        return text

    def appendWithTimeStamp(self, text):

        st = self.create_timestamp()
        temp = str(st)+" "+text + "\r\n"
        self.append(temp)
        self.text_to_print += temp
        return temp

    def create_timestamp(self):
        now = datetime.now()
        st = now.strftime('%Y-%m-%d %H:%M:%S') + ('.%04d' % (now.microsecond / 100))
        #print(st)
        return st

    def print(self):
        return self.text_to_print

if __name__ == '__main__':
    print("report demo")

    #mreport = MainReport()
    #mreport.begin()
    #mreport.end()
    #ireport = [None, None, None]
    
    ireport = IndividualReport()
    #ireport.begin()

    #print(ireport.appendWithTimeStamp("data1\r\n"), end='')
    #print(ireport.appendWithTimeStamp("data2\r\n"), end='')
    #print(ireport.appendWithTimeStamp("data3\r\n"), end='')
    #for i in range (0,20): 
    ireport.appendWithTimeStampUsingFile("," + "data1" + "," + "data2" + "," + "data3","Modulo" + "1 " + "2019-11-23")
    #ireport.appendWithTimeStamp("data2")
    #ireport.appendWithTimeStamp("data3")
    #print(ireport.print(), end='')

    #ireport.end()
