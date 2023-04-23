import matplotlib.pyplot as plt
import csv


with open('nominal.csv', 'r') as File:
    Data = list(csv.reader(File))

X = [float(row[0]) for row in Data[1:]]
Y = [float(row[1]) for row in Data[1:]]
Z = [float(row[2]) for row in Data[1:]]

plt.plot(X, Y, label='Y')
plt.plot(X, Z, label='Z')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.legend()
plt.show()