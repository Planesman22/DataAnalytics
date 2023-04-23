import RPi.GPIO as GPIO
from time import sleep

PWMPin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWMPin, GPIO.OUT)
pi_pwm = GPIO.PWM(PWMPin, 1000)
pi_pwm.start(0)

while True:
    for duty in range(0, 101, 1):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)

    for duty in range(100, -1, -1):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)