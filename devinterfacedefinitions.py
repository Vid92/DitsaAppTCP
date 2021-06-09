from enum import Enum
#some changes
'''
DEV_OPERATION = {}
DEV_OPERATION["NRF52_ENABLE_EXPANSION_PORT_POWER"] = "exppwron"
DEV_OPERATION["NRF52_DISABLE_EXPANSION_PORT_POWER"] = "exppwroff"
DEV_OPERATION["PIC32_READ_MAIN_POWER_GOOD_PIN"] = "read_main_pwr_good_pin"
DEV_OPERATION["PIC32_DISABLE_NRF52_SPI_INTERFACE"] = "dis_nrf52_spi"
DEV_OPERATION["PIC32_ENABLE_NRF52_SPI_INTERFACE"] = "en_nrf52_spi"
DEV_OPERATION["NRF52_DISABLE_PIC32_SPI_INTERFACE"] = "dis_pic32_spi"
DEV_OPERATION["NRF52_ENABLE_PIC32_SPI_INTERFACE"] = "en_pic32_spi"
DEV_OPERATION["PIC32_SET_GPIOS_TO_NRF52_HIGH"] = "set_gpios_to_nrf52_high"
DEV_OPERATION["PIC32_SET_GPIOS_TO_NRF52_LOW"] = "set_gpios_to_nrf52_low"
DEV_OPERATION["NRF52_SET_GPIOS_TO_PIC32_HIGH"] = "set_gpios_to_pic32_high"
DEV_OPERATION["NRF52_SET_GPIOS_TO_PIC32_LOW"] = "set_gpios_to_pic32_low"
DEV_OPERATION["PIC32_READ_GPIOS_FROM_NRF52"] = "read_gpios_from_nrf52"
DEV_OPERATION["NRF52_READ_GPIOS_FROM_PIC32"] = "read_gpios_from_pic32"
DEV_OPERATION["NRF52_READ_POWER_FAULT_PIN"] = "read_pwr_fault"
DEV_OPERATION["PIC32_ENABLE_READER_POWER"] = "readerpower_on"
DEV_OPERATION["PIC32_DISABLE_READER_POWER"] = "readerpower_off"
DEV_OPERATION["PIC32_SET_IDS_OUT_TO_OFF"] = "idsforceoff"
DEV_OPERATION["PIC32_SET_IDS_OUT_TO_ON"] = "idsforceon"
DEV_OPERATION["PIC32_READ_IDS_IN"] = "ids_in_state"
DEV_OPERATION["PIC32_TURN_USB_CHARGER_ON"] = "usbchargeon"
DEV_OPERATION["PIC32_TURN_USB_CHARGER_OFF"] = "usbchargeoff"
DEV_OPERATION["PIC32_TURN_LED_RED"] = "redled"
DEV_OPERATION["PIC32_TURN_LED_GREEN"] = "greenled"
DEV_OPERATION["PIC32_TURN_LED_BLUE"] = "blueled"
DEV_OPERATION["PIC32_READ_REFILL_SWITCH_INPUT"] = "refill_state"
DEV_OPERATION["NRF52_RESET_PIC"] = "resetpic"
DEV_OPERATION["PIC32_RESET_NRF52"] = "resetnrf"
DEV_OPERATION["PIC32_GET_RESET_SOURCE"] = "reset_source"
DEV_OPERATION["NRF52_GET_RESET_SOURCE"] = "nrf52_reset_source"
DEV_OPERATION["PIC32_DISABLE_BOOST_PWR_SUPPLY"] = "boost_disable"
DEV_OPERATION["PIC32_DISABLE_BATTERY_CHARGER"] = "batt_charger_disable"
DEV_OPERATION["PIC32_READ_BATTERY_VOLTAGE"] = "batvolt"
DEV_OPERATION["PIC32_ENABLE_BOOST_PWR_SUPPLY"] = "boost_enable"
DEV_OPERATION["PIC32_READ_INPUT_POWER_LOSS_PIN"] = "pwr_loss_state"
DEV_OPERATION["PIC32_READ_WIRELESS_MODULE_SIMID"] = "readsimid"
DEV_OPERATION["PIC32_WIRELESS_MODULE_COMMUNICATIONS_TEST"] = "wm_comm_test"
DEV_OPERATION["PIC32_WIRELESS_MODULE_GET_TYPE"] = "get_wm_type"
DEV_OPERATION["PIC32_WIRELESS_MODULE_SERIAL_NUM"] = "get_wm_sn"
DEV_OPERATION["PIC32_WIRELESS_MODULE_IMEI_SV_NUM"] = "get_wm_imei"
DEV_OPERATION["PIC32_WIRELESS_MODULE_FIRMWARE_VER"] = "get_wm_fv"
DEV_OPERATION["PIC32_WIRELESS_MODULE_ENABLE_TEST_MODE"] = "enable_wm_test_mode"
DEV_OPERATION["PIC32_WIRELESS_MODULE_DISABLE_TEST_MODE"] = "disable_wm_test_mode"
DEV_OPERATION["NRF52_ACTIVATE_BLE_TEST"] = "bletest"
DEV_OPERATION["NRF52_ACTIVATE_BLE_LOOPBACK"] = "activate_ble_loopback"
DEV_OPERATION["PIC32_CLEAR_AUTO_MANUFACTURE_TEST_ACTIVATION"] = "clear_auto_mt_activate"
DEV_OPERATION["NRF52_READ_3_7_VOLT_SUPPLY"] = "read3_7volt_supply"
DEV_OPERATION["NRF52_READ_1_8_VOLT_SUPPLY"] = "read1_8volt_supply"
DEV_OPERATION["NRF52_READ_WIRELESS_MODULE_CURRENT"] = "read_wm_current"
DEV_OPERATION["PIC32_WIRELESS_MODULE_SPI_TEST"] = "pic32_wm_spi_test"
DEV_OPERATION["PIC32_READ_USB_OC_PIN"] = "read_usb_oc_pin"
DEV_OPERATION["START_MANUFACTURING_TEST_ON_NRF52"] = "activate_manufacturing_testing"

TESTS_TO_DO = [
"MEASURE_VOLTAGES",
"PROGRAMMING_MCUS",
"NRF52_BLE_TEST",
"NRF52_EXPANSION_PORT_POWER_TEST",
"NRF52_EXPANSION_PORT_COMM_TEST",
"NRF52_ACCELEROMETER_TEST",
"NRF52_SERIAL_EEPROM_TEST",
"PIC32_SQI_FLASH_TEST",
"PIC32_EEPROM_TEST",
"PIC32_HARDWARE_ID_TEST",
"PIC32_TO_NRF52_SPI_TEST",
"PIC32_TO_NRF52_GPIO_TEST",
"PIC32_MDB_INTERFACE_TEST",
"PIC32_DEX_INTERFACE_TEST",
"PIC32_CARD_READER_INTERFACE_TEST",
"PIC32_CARD_READER_POWER_TEST",
"PIC32_IDS_NC_SWITCH_TEST",
"PIC32_IDS_NO_SWITCH_TEST",
"PIC32_IDS_SDS_SWITCH_TEST",
"PIC32_IDS_FORCE_SWITCH_TEST",
"PIC32_USB_CHARGING_TEST",
"PIC32_USB_DATA_TEST",
"PIC32_WIRELESS_MODULE_GPIO_TEST",
"PIC32_WIRELESS_MODULE_UART_TEST",
"NRF52_WIRELESS_MODULE_I2C_TEST",
"NRF52_WIRELESS_MODULE_GPIO_TEST",
"PIC32_REFILL_SWITCH_TEST",
"NRF52_PIC32_RESET_TEST",
"PIC32_NRF52_RESET_TEST",
"PIC32_BATTERY_MEASURE_TEST",
"PIC32_BATTERY_CHARGING_TEST",
"PIC32_BATTERY_BOOST_AND_MAIN_VOLTAGE_TEST"
]

class TEST_STATUS(Enum):
    TEST_NOT_SELECTED = 0
    TEST_SELECTED_OR_IN_PROGRESS = 1
    TEST_PASSED = 2
    TEST_FAILED = 3

DEV_TEST_DESC = [
"Measure Voltages",
"Programming Both MCU's",
"nRf52 BLE Test",
"nRf52 Expansion Port Power Test",
"nRf52 Expansion Port Comm Test",
"nRf52 Accelerometer Test",
"nRf52 Serial EEPROM Test",
"PIC32 SQI Flash Test",
"PIC32 EEPROM Test",
"PIC32 Hardware ID Test",
"PIC32 to nRF52 SPI Test",
"PIC32 to nRF52 GPIO Test",
"PIC32 MDB Comm Interface Test",
"PIC32 DEX Comm Interface Test",
"PIC32 READER Comm Interface Test",
"PIC32 READER PWR Interface Test",
"PIC32 IDS Normally Closed Test",
"PIC32 IDS Normally Open Test",
"PIC32 IDS Simple Door Switch Test",
"PIC32 IDS Force Switch Test",
"PIC32 USB Charging Test",
"PIC32 USB Data Test",
"PIC32 Wireless Module GPIO Test",
"PIC32 Wireless Module UART Test",
"NRF52 Wireless Module I2C Test",
"NRF52 Wireless Module GPIO Test",
"PIC32 Refill Switch Test",
"NRF52 PIC32 Reset Test",
"PIC32 NRF52 Reset Test",
"PIC32 Battery Measure Test",
"PIC32 Battery Charge Test",
"PIC32 Batt Boost and Volt Test"
]

DEV_TEST_OP = [
"measure_voltages",
"program_both_devices",
"NRF52_BLE_TEST",
"NRF52_EXPANSION_PORT_POWER_TEST",
"exp_comm_test",
"accel",
"eeprom",
"flashtest",
"eepromtest",
"hwid",
"nrf52test",
"PIC32_TO_NRF52_GPIO_TEST",
"mdbtest",
"dextest",
"readertest",
"PIC32_CARD_READER_POWER_TEST",
"PIC32_IDS_NC_SWITCH_TEST",
"PIC32_IDS_NO_SWITCH_TEST",
"PIC32_IDS_SDS_SWITCH_TEST",
"PIC32_IDS_FORCE_SWITCH_TEST",
"PIC32_USB_CHARGING_TEST",
"usbdata",
"wlmgpio",
"wlmuart",
"wm_i2c_test",
"nrf52wlmgpio",
"PIC32_REFILL_SWITCH_TEST",
"NRF52_PIC32_RESET_TEST",
"PIC32_NRF52_RESET_TEST",
"PIC32_BATTERY_MEASURE_TEST",
"PIC32_BATTERY_CHARGING_TEST",
"PIC32_BATTERY_BOOST_AND_MAIN_VOLTAGE_TEST"
]


DEV_TEST_ENABLED = {}
DEV_TEST_ENABLED[VIU_TEST_OP[0]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[1]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[2]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[3]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[4]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[5]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[6]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[7]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[8]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[9]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[10]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[11]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[12]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[13]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[14]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[15]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[16]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[17]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[18]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[19]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[20]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[21]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[22]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[23]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[24]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[25]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[26]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[27]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[28]] = False
DEV_TEST_ENABLED[VIU_TEST_OP[29]] = False

DEV_TEST_RESPONSE = {}
DEV_TEST_RESPONSE[VIU_TEST_OP[0]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[1]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[2]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[3]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[4]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[5]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[6]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[7]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[8]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[9]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[10]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[11]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[12]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[13]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[14]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[15]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[16]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[17]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[18]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[19]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[20]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[21]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[22]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[23]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[24]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[25]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[26]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[27]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[28]] = ""
DEV_TEST_RESPONSE[VIU_TEST_OP[29]] = ""

DEV_TEST_RESULT = {}
DEV_TEST_RESULT[VIU_TEST_OP[0]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[1]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[2]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[3]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[4]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[5]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[6]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[7]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[8]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[9]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[10]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[11]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[12]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[13]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[14]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[15]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[16]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[17]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[18]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[19]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[20]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[21]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[22]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[23]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[24]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[25]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[26]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[27]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[28]] = ""
DEV_TEST_RESULT[VIU_TEST_OP[29]] = ""

class TestName(Enum):
	NRF52_BLE_TEST = "nRF52 BLE Test"
	PIC32_EEPROM_TEST = "PIC32 EEPROM Test"

class TestResult(Enum):
	PASS = "PASS"
	FAIL = "FAIL"
'''
