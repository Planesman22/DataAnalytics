import smbus
import os
import time

StartTime = time.monotonic()
Bus = smbus.SMBus(1)
Address = 0x6a


while True:
    os.system('clear')

    Data = Bus.read_byte(Address)

    print("At time "+time.monotonic()-StartTime+":")
    print(Data)

    time.sleep(0.5)

