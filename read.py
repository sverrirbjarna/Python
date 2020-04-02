import re
import matplotlib.pyplot as plt
import numpy as np

first = []
avg = []
rate = []
outF = open("Out.txt", "w")
with open("train.log") as f:
    for line in f:
        if re.match(r"\s\d",line):
            txt = line.lstrip()
            #print (txt)
            outF.write(txt)
            x = txt.split(" ")

            first.append(float(x[1][:-1]))
            avg.append(float(x[2]))
            rate.append(float(x[5]))
            #print(x)

outF.close()


y = np.linspace(0, len(avg), len(avg))
plt.plot(y, avg, label='linear')
plt.show()
plt.plot(y, rate, label='linear')
plt.show()
plt.plot(y, first, label='linear')
plt.show()
print(y)
