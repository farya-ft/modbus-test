from pymodbus.client.serial import ModbusSerialClient as ModbusSerialClient
import time

client = ModbusSerialClient(method='rtu', port='/dev/ttyACM0', baudrate=9600, timeout=0.5)

client.connect()


d = client.write_coil(address=0x0,value=True,slave=1)

while True:
    d = client.write_coil(address=0x0, value=True, slave=1)
    time.sleep(1)
    d = client.write_coil(address=0x0, value=False, slave=1)
    time.sleep(1)