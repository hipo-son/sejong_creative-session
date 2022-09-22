import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.animation import FuncAnimation_

def Energy(h, v):
  E = g * h + (1/2) * (v**2)
  return E

g = 9.8; v0 = 10.; theta = 45 * (np.pi/180.); dt = 0.01;
vx = v0 * np.cos(theta); vy= v0 * np.sin(theta)
x, y = 0., 0.
px, py = [], []

while Energy(y, vy) > 0.1:
  if y < 0 and vy < 0:
    vy = 0.8 * abs(vy)
  x += vx * dt
  y += vy * dt
  vy -= g * dt
  px.append(x)
  py.append(y)

plt.plot(px, py)

rc('animation', html='jshtml')

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(min(px), max(px))
    ax.set_ylim(min(py), max(py))
    return ln,
def update(frame):
    xdata.append(px[frame])
    ydata.append(py[frame])
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=range(0, len(px), 5), init_func = init, blit = False)
ani

def Energy(h, v):
  E = g * h + (1/2) * (v**2)
  return E

g = 9.8; v0 = 10.; theta = 60 * (np.pi/180.); dt = 0.01;
vx = v0 * np.cos(theta); vy= v0 * np.sin(theta)
x, y = 0., 0.
px, py = [], []

while Energy(y, vy) > 0.1:
  if y < 0 and vy < 0:
    vy = 0.8 * abs(vy)
  x += vx * dt
  y += vy * dt
  vy -= g * dt
  px.append(x)
  py.append(y)

plt.plot(px, py)
