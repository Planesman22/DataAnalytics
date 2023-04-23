import board
import pwmio
import shawnc
from time import sleep

# PWM ESC Init
ESC = pwmio.PWMOut(board.D18, frequency=400)

# ESC Calibration
ESC.duty_cycle = shawnc.PWToDC(2000)
while True:
    UserInput = input("Please Connect Battery! (Enter Y to continue)")
    if UserInput.lower() == 'y':
        break
sleep(3)
ESC.duty_cycle = shawnc.PWToDC(1000)
sleep(15)
print("ESC should be calibrated, please check tones!")
