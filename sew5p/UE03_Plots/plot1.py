import math
import matplotlib.pyplot as plt

cnt = 1024
x = [a * (2*math.pi/cnt) - math.pi for a in range(cnt)]
c = [math.cos(a) for a in x]
s = [math.sin(a) for a in x]

plt.plot(x, c, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(x, s, color="red", linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left', frameon=False)
plt.xlim(min(x)*1.1, max(x)*1.1)
plt.ylim(min(c)*1.1, max(c)*1.1)
plt.xticks([-math.pi, -math.pi/2, 0, math.pi/2, math.pi],
[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
[r'$-1$', r'$0$', r'$+1$'])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
t = 2*math.pi/3
plt.plot([t,t],[0,math.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
plt.scatter([t,],[math.cos(t),], 50, color ='blue')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
xy=(t, math.sin(t)), xycoords='data',
xytext=(+10, +30), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot([t,t],[0,math.sin(t)], color ='red', linewidth=2.5, linestyle="--")
plt.scatter([t,],[math.sin(t),], 50, color ='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
xy=(t, math.cos(t)), xycoords='data',
xytext=(-90, -50), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
plt.savefig("plot1_smyrnov.png", dpi=72)
plt.show()