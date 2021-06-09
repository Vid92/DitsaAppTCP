import sys
from enum import Enum
# [Number, Description, FailureType, Enable, Checked, Result]

import shared

useDesktopToSaveReports = True
useDongle = True
useMac = True

#para server se cambian estas dos lineas y se comentan las 3 siguientes
#useHostname = 'ditsaServer1.local' 
#usePort = 65433

useHostname = list() #lee el archivo de serverConfig
usePort = list()
usePassw = list()

measureWMVoltage = False
jlinkSNforPIC32 = 820100854
jlinkSNforNRF52 = 820100854

inAustin = False
remoteDebug = True

TEST_UNCHECKED = 0
TEST_CHECKED = 1

NON_CATASTROPHIC = 0
CATASTROPHIC = 1

BARCODE_SCANNED = False
TESTFIXTURE_CLOSED = False

EXCLUDE = 0
INCLUDE = 1

TEST_PASS = 0
TEST_FAIL = 1
TEST_NONE = 2
TEST_ABORTED = 3 # ABORTED BY OPEN LID OR DUT REMOVED
TEST_CANCEL = 4 # TEST CANCELED BY THE USER

GLOBAL_NUMBER_OF_TESTS = 0
GLOBAL_CURRENT_TEST = 0

GLOBAL_TEST_RESULT = TEST_NONE
GLOBAL_TEST_STATUS = TEST_NONE

CURRENT_SERIAL_NUMBER = None

#GLOBAL_ROOT_PASWORD = 'Paulina84'

if inAustin:
    GLOBAL_ROOT_PASWORD = 'vwtele123'
else:
    GLOBAL_ROOT_PASWORD = 'Paulina84'
'''
APP_TESTS = [
    ['ActivatingManufacturingTestingOnThePIC32AndNRF52', 'Activating Manufacturing Testing on the PIC32 and NRF52', CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52BLETest', 'nRF52 BLE Test',                                                                              NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE]
]
'''

APP_TESTS = [
    ['boardCurrentTest', 'Board Current Test',                                                                      CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['voltageTestsPart1', 'Voltage Tests Part 1',                                                                   CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52SiliconVersionandSerialNumberVerification', 'nRF52 Silicon Version and Serial Number Verification',      CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52ManufacturingFirmwareProgram', 'nRF52 Manufacturing Firmware Program',                                   CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32SiliconVersionVerification', 'PIC32 Silicon Version Verification',                                       CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32ManufacturingFirmwareProgramming', 'PIC32 Manufacturing Firmware Programming',                           CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['ActivatingManufacturingTestingOnThePIC32AndNRF52', 'Activating Manufacturing Testing on the PIC32 and NRF52', CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['voltageTestsPart2', 'Voltage Tests Part 2',                                                                   CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],

    ['hardwareIDTest', 'Hardware ID Test',                                                                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['pic32SetSerialNumber', 'PIC32 Set Serial Number',                                                             NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32ReadFirmwareVersions', 'PIC32 Read Firmware Versions',                                                   NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['NRF52ReadFirmwareVersions', 'NRF52 Read Firmware Versions',                                                   NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52BLETest', 'nRF52 BLE Test',                                                                              NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52ExpansionPortPowerTest', 'nRF52 Expansion Port Power Test',                                              NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52ExpansionPortCommunicationTest', 'nRF52 Expansion Port Communication Test',                              NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52AccelerometerTest', 'nRF52 Accelerometer Test',                                                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52SerialEEPROMTest', 'nRF52 Serial EEPROM Test',                                                           NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32SerialFlashTest', 'PIC32 Serial Flash Test',                                                             NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32EEPROMTest', 'PIC32 EEPROM Test',                                                                        NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32_to_nRF52_SPIInterfaceTest', 'PIC32-to-nRF52 SPI Interface Test',                                        NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32_to_nRF52_GPIOPinsTest', 'PIC32-to-nRF52 GPIO Pins',                                                     NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32MDBInterfaceTest', 'PIC32 MDB Interface Test',                                                           NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32DEXInterfaceTest', 'PIC32 DEX Interface Test',                                                           NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['CreditCardReaderInterfaceCommunicationTest', 'Credit Card Reader Interface Communication Test',               NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['CreditCardReaderInterfacePowerTest', 'Credit Card Reader Interface Power Test',                               NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['IDSNormallyClosedSwitchTest', 'IDS Normally Closed Switch Test',                                              NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['IDSNormallyOpenSwitchTest', 'IDS Normally Open Switch Test',                                                  NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['SDSSwitchTest', 'SDS Switch Test',                                                                            NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['IDSForceTest', 'IDS Force Test',                                                                              NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['USBDataTest', 'USB Data Test',                                                                                NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['USBPortChargingTest', 'USB Charging Test',                                                                    NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['WirelessModuleInterfacePIC32SPITest', 'Wireless Module Interface PIC32 SPI Test',                             NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['WirelessModuleInterfacePIC32GPIOTest', 'Wireless Module Interface PIC32 GPIO Test',                           NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['WirelessModuleInterfacePIC32UARTTest', 'Wireless Module Interface PIC32 UART Test',                           NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['WirelessModuleInterfacenRF52I2CTest', 'Wireless Module Interface nRF52 I2C Test',                             NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['WirelessModuleInterfacenRF52GPIOTest', 'Wireless Module Interface nRF52 GPIO Test',                           NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],

    ['FrontPanelPowerStatusLEDTest', 'Front Panel Power Status LED Test',                                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],

    #['FrontPanelWirelessModuleStatusLEDTest', 'Front Panel Wireless Module Status LED Test',                       NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],

    ['FrontPanelTriColorStatusBLUELEDTest', 'Front Panel Tri-Color Status BLUE LED Test',                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['FrontPanelTriColorStatusREDLEDTest', 'Front Panel Tri-Color Status RED LED Test',                            NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['FrontPanelTriColorStatusGREENLEDTest', 'Front Panel Tri-Color Status GREEN LED Test',                        NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['RefillSwitchTest', 'Refill Switch Test',                                                                      NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32ResetTest', 'PIC32 Reset Test',                                                                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['nRF52ResetTest', 'nRF52 Reset Test',                                                                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['BatteryTest', 'Battery Test',   NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['BatteryBoostCircuitandMainVoltageLossIndicatorCircuitTest', 'Battery Boost Circuit and Main Voltage Loss Indicator Circuit Test',   NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['PIC32ApplicationFirmwareProgramming', 'Set As Application Firmware',                                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],

 ]

'''
APP_TESTS = [
    ['FrontPanelPowerStatusLEDTest', 'Front Panel Power Status LED Test',                                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    #['FrontPanelWirelessModuleStatusLEDTest', 'Front Panel Wireless Module Status LED Test',                       NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['FrontPanelTriColorStatusBLUELEDTest', 'Front Panel Tri-Color Status BLUE LED Test',                          NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['FrontPanelTriColorStatusREDLEDTest', 'Front Panel Tri-Color Status RED LED Test',                            NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE],
    ['FrontPanelTriColorStatusGREENLEDTest', 'Front Panel Tri-Color Status GREEN LED Test',                        NON_CATASTROPHIC, INCLUDE, TEST_UNCHECKED, TEST_NONE]
]
'''

def getDescriptionFromNumber(number):
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][0] == number:
            return APP_TESTS[x][1]

def getNumberFromDescription(description):
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][1] == description:
            return APP_TESTS[x][0]

def getFailureTypeFromDescription(description):
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][1] == description:
            return APP_TESTS[x][2]

def getEnableStateFromDescription(description):
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][1] == description:
            return APP_TESTS[x][3]

def getCheckedStateFromDescription(description):
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][1] == description:
            return APP_TESTS[x][4]

def setCheckedStateFromDescription(description, state):
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][1] == description:
            APP_TESTS[x][4] = state

def getTestStatusFromDescription(description):
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][1] == description:
            return APP_TESTS[x][5]

def setTestStatusFromDescription(description, status):
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][1] == description:
            APP_TESTS[x][5] = status

def countEnabledTests():
    counter = 0
    for x in range(0, len(APP_TESTS)):
        if APP_TESTS[x][3] == INCLUDE:
            counter = counter + 1
    return counter

#######################################################################################################

# Future Technology Devices International Limited FT232R USB UART
FTDI_idVendor=0x0403
FTDI_idProduct=0x6001
FTDI_baudRate=115200
if inAustin == True:
    FTDI_serialNumber='AH05R7EI' # Austin
else:
    FTDI_serialNumber='AH05R7EG' # Monterrey

if inAustin == True:
    lj_sn1 =  320074622
    lj_sn2 =  320084481
else:
    lj_sn1 = 320080921
    lj_sn2 = 320080921

# Honeywell BarcodeScanner 0c2e
BarcodeScanner_idVendor=0x0c2e
BarcodeScanner_idProduct=0x0b6a
BarcodeScanner_baudRate=115200
BarcodeScanner_endChar='\r'

# LabJack U3 LV 0cd5 LabJack U3
LabJack_idVendor=0x0cd5
LabJack_idProduct=0x0003

# Winbond Electronics Corp. USB Virtual COM
KORAD_idVendor=0x0416
KORAD_idProduct=0x5011
KORAD_baudRate=9600

# PIC32 ICSP SPEED
PIC32_SEGGER_SPEED = 20000
# NRF52 SWD SPEED
NRF52_SEGGER_SPEED = 4000

#######################################################################################################

LED_THRESHOLD = 80

# MDB Voltage and Current Test
MDB_VOLTAGE_HIGH_VALUE = 30
MDB_VOLTAGE_LOW_VALUE = 20
MDB_CURRENT_HIGH_VALUE = 200 # mA
MDB_CURRENT_LOW_VALUE = 25 # mA

# Voltage Tests [A2, A1, A0]
# VCC_MDB_FLTR, Filtered MDB input voltage (VCC_MDB_FLTR), TP38, [0, 0, 0]
VCC_MDB_FLTR_ACCEPTABLE_HIGH_VALUE = 25.2
VCC_MDB_FLTR_ACCEPTABLE_LOW_VALUE = 19.0

# VCC_5V0, Main 5.0 VDC supply output from SIC462ED (U11), TP15, [0, 0, 1]
VCC_5V0_HIGH_VALUE = 5.1
VCC_5V0_LOW_VALUE = 4.2

# VCC_5V0F, 5.0 VDC to PAM2310 (U8) TP14, [0, 1, 0]
VCC_5V0F_HIGH_VALUE = 5.1
VCC_5V0F_LOW_VALUE = 4.2

# VCC5V0F, 5.0 VDC at Wireless Module, TP16, [0, 1, 1]
VCC5V0F_HIGH_VALUE = 5.1
VCC5V0F_LOW_VALUE = 4.2

# VCC_3V3, Main 3.3 VDC supply output from PAM2310 (U8), TP13, [1, 0, 0]
VCC_3V3_HIGH_VALUE = 5.1
VCC_3V3_LOW_VALUE = 3.0

# VBUS, USB Charger 5.0 VDC, J8.1, [1, 0, 1]
VBUS_HIGH_VALUE = 5.1
VBUS_LOW_VALUE = 4.5

# VCC_5V0GPIO, Expansion Port 5.0 VDC, P1.1, [1, 1, 0]
VCC_5V0GPIO_HIGH_VALUE = 5.1
VCC_5V0GPIO_LOW_VALUE = 4.1

# VCC_FLT_MDB, Power Supply (U16) Card Reader 24.0 VDC, TP42, [1, 1, 1]
VCC_FLT_MDB_HIGH_VALUE = 25.2
VCC_FLT_MDB_LOW_VALUE = 17.5

# VCC3V3_WM, 3.3V VDC at Wireless Module, TP18,
VCC3V3_WM_HIGH_VALUE = 5.1
VCC3V3_WM_LOW_VALUE = 3.0

if __name__ == "__main__":
    print("code something else in here!")
