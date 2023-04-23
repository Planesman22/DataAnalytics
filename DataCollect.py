import os
import time
import board
import busio
import pwmio
import shawnc
from adafruit_lsm6ds.ism330dhcx import ISM330DHCX
from time import sleep

# I2C Acc Init
I2C = busio.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA
Sensor = ISM330DHCX(I2C)

# PWM ESC Init
ESC = pwmio.PWMOut(board.D18, frequency=400)

# Change power to 0 and wait for battery connect so we don't kill ourselves
ESC.duty_cycle = shawnc.PWToDC(1000)

while True:
    UserInput = input("Please Connect Battery! (Enter Y to continue)")
    if UserInput.lower() == 'y':
        break

# Literally wait a second, for vibe check
sleep(1)

ESC.duty_cycle = shawnc.PWToDC(1200)
sleep(3)
ESC.duty_cycle = shawnc.PWToDC(1000)
sleep(3)
ESC.duty_cycle = shawnc.PWToDC(1300)
sleep(3)
ESC.duty_cycle = shawnc.PWToDC(1000)
sleep(3)
