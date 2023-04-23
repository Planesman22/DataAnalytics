import RPi.GPIO as GPIO
import shawncommon
from time import sleep

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