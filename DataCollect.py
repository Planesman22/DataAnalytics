import RPi.GPIO as GPIO
from time import sleep

def PWToDC(PW):
    Frequency = 400
    Period = 1/Frequency
    return (PW/Period) * 0.0001

def PowerToDC(Power):
    return PWToDC(1000+1000*Power)

#GPIO Setup
PWMPin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWMPin, GPIO.OUT)

ESC = GPIO.PWM(PWMPin, 400)
ESC.start(0)

#First Calibrate ESC
ESC.ChangeDutyCycle(PowerToDC(1.00))
sleep(5)
ESC.ChangeDutyCycle(PowerToDC(0.00))
sleep(10)
