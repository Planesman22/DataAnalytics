import os
import time
import board
import busio
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

I2C = busio.I2C(board.SCL, board.SDA)
Sensor = LSM6DSOX(I2C)

while True:
    os.system('clear')
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % Sensor.acceleration)
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % Sensor.gyro)
    time.sleep(0.5)
