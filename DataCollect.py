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

# Change power to 0 so we don't kill ourselves
ESC.duty_cycle = shawnc.PWToDC(1000)

# Literally wait a second, for vibe check
sleep(1)

ESC.duty_cycle = shawnc.PWToDC(1000)
sleep(0.5)
ESC.duty_cycle = shawnc.PWToDC(1000)
sleep(0.5)
ESC.duty_cycle = shawnc.PWToDC(1000)
sleep(0.5)
ESC.duty_cycle = shawnc.PWToDC(1000)
sleep(0.5)
