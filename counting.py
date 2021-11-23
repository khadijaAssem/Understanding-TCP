import numpy as np
import matplotlib.pyplot as plt
import os

timestamp, scwnd, fcwnd= np.loadtxt("test/tcp-example.cwnd", unpack=True)
plt.plot(timestamp, scwnd)
plt.title("cwnd vs time")
plt.xlabel("time")
plt.ylabel("cwnd")
plt.show()

count = 0
print(os.getcwd())
with open("test/tcp-example.cwnd") as f:
    w, h, m = [float(x) for x in next(f).split()] # read first line
    for line in f: # read rest of lines
        w, h, m = ([float(x) for x in line.split()])
        if h > m:
            count += 1
print (count)
