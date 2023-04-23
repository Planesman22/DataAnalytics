import os
import time
import board
import adafruit_lsm6ds

submodules = dir(adafruit_lsm6ds)
print(submodules)

I2C = board.I2C()  # uses board.SCL and board.SDA
Sensor = adafruit_lsm6ds.lsm6dsox(I2C)

while True:
    os.system('clear')
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % Sensor.acceleration)
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % Sensor.gyro)
    time.sleep(0.5)
