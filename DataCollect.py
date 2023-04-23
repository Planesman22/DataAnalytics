import RPi.GPIO as GPIO
from time import sleep

def PWToDC(PW):
    Frequency = 400
    Period = 1/Frequency
    return (PW/Period) * 0.0001

#GPIO Setup
PWMPin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWMPin, GPIO.OUT)

ESC = GPIO.PWM(PWMPin, 400)
ESC.start(0)

#First Calibrate ESC
ESC.ChangeDutyCycle(PWToDC(2000))
sleep(5)
ESC.ChangeDutyCycle(PWToDC(1000))
sleep(10)
