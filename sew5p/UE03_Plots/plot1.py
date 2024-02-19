import math
import matplotlib.pyplot as plt

cnt = 1024
x = [a * (2*math.pi/cnt) - math.pi for a in range(cnt)]
c = [math.cos(a) for a in x]
s = [math.sin(a) for a in x]

plt.plot(x, c)
plt.plot(x, s)
plt.savefig("plot1_smyrnov.png", dpi=72)
plt.show()