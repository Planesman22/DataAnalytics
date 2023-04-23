import os
import time
import board
import adafruit_lsm6ds

i2c = board.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA
sox = LSM6DSOX(i2c)

while True:
    os.system('clear')
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(sox.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s"%(sox.gyro))
    print("")
    time.sleep(0.5)
