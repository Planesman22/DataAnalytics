import matplotlib.pyplot as plt
import numpy
import csv


with open('nominal180.csv', 'r') as File:
    Data = list(csv.reader(File))

DataNP = numpy.array(Data, dtype=float)

DataX = DataNP[:, 0]
DataY = DataNP[:, 1]
DataZ = DataNP[:, 2]

TimeInt = numpy.arange(len(DataNP)) * 0.01

plt.plot(TimeInt, DataX, label='X-axis')
plt.plot(TimeInt, DataY, label='Y-axis')
plt.plot(TimeInt, DataZ, label='Z-axis')

plt.ylim(-40, 40)

plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.legend()

plt.show()