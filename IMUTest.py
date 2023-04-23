import os
import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

submodules = dir(adafruit_lsm6ds.lsm6dsox)
print(submodules)

I2C = board.I2C()  # uses board.SCL and board.SDA
Sensor = LSM6DSOX(I2C)

while True:
    os.system('clear')
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % Sensor.acceleration)
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % Sensor.gyro)
    time.sleep(0.5)
