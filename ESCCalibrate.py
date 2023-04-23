import RPi.GPIO as GPIO
from time import sleep

def PWToDC(PW):
    Frequency = 400
    Period = 1/Frequency
    return (PW/Period) * 0.0001

def PowerToDC(Power):
    # We use PW range from 1000-2000
    return PWToDC(1000+1000*Power)

#GPIO Setup
PWMPin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWMPin, GPIO.OUT)

ESC = GPIO.PWM(PWMPin, 400)
ESC.start(0)

# ESC Calibration
ESC.ChangeDutyCycle(PowerToDC(1.00))
while True:
    UserInput = input("Please Connect Battery! (Enter Y to continue)")
    if UserInput.lower() == 'y':
        break
sleep(3)
ESC.ChangeDutyCycle(PowerToDC(0.00))
sleep(15)
print("ESC should be calibrated, please check tones!")