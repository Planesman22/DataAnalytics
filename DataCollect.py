import RPi.GPIO as GPIO
from time import sleep


def PWToDC(PW):
    Frequency = 400
    Period = 1 / Frequency
    return (PW / Period) * 0.0001


def PowerToDC(Power):
    return PWToDC(1000 + 1000 * Power)


# GPIO Init
PWMPin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWMPin, GPIO.OUT)
ESC = GPIO.PWM(PWMPin, 400)
ESC.start(0)

# Change power to 0 so we don't kill ourselves
ESC.ChangeDutyCycle(PowerToDC(0.0))

# Literally wait a second, for vibe check
sleep(1)

ESC.ChangeDutyCycle(PowerToDC(0.3))
sleep(10)
