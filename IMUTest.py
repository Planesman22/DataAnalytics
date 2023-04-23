import os
import time
import board
from adafruit_lsm6ds.ism330dhcx import ISM330DHCX

I2C = board.I2C()  # uses board.SCL and board.SDA
Sensor = ISM330DHCX(I2C)

while True:
    os.system('clear')
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % Sensor.acceleration)
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % Sensor.gyro)
    time.sleep(0.1)
