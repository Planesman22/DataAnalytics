import os
# import board
import time
import shawnc
import RPi.GPIO as GPIO
# from adafruit_lsm6ds.ism330dhcx import ISM330DHCX
from time import sleep

# GPIO Init
PWMPin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWMPin, GPIO.OUT)
ESC = GPIO.PWM(PWMPin, 400)
ESC.start(0)

ESC.ChangeDutyCycle(shawnc.PowerToDC(0.0))

'''
# Sensor Init
I2C = board.I2C()  # uses board.SCL and board.SDA
Sensor = ISM330DHCX(I2C)

# Change power to 0 so we don't kill ourselves
ESC.ChangeDutyCycle(shawnc.PowerToDC(0.0))

# Literally wait a second, for vibe check
sleep(1)

ESC.ChangeDutyCycle(shawnc.PowerToDC(0.3))
sleep(10)
'''