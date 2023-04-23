import smbus
import os
import time

bus = smbus.SMBus(1)

Address = 0x6a

while True:
    os.system('clear')

    Data = bus.read_byte(Address)

    print(Data)

    time.sleep(0.5)

