#Symulacja fali harmonicznej

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plt.style.use('seaborn-pastel')

A = float(input("Podaj amplitude fali w [m]: "))
k = float(input("Podaj liczbe falowa w [rad/m]: "))
w = float(input("Podaj czestosc fali w [rad/s]: "))

fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(-A-5, A+5))
line, = ax.plot([], [], linewidth=3)

def animate(i):
    x = np.linspace(0, 100,1000)
    y = A*np.sin(k*x-w*i)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, frames=500, interval=20, blit=True)
plt.title("Symulacja fali harmonicznej")
plt.xlabel("x")
plt.ylabel("y")
plt.show()



