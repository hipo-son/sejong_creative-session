# %% codecell
import numpy as np

def Energy(h, v):
  E = g * h + (1/2) * (v**2)
  return E

g = 9.8; v0 = 10.; theta = 45 * (np.pi/180.); dt = 0.01; #alpha = 0.01;
vx = v0 * np.cos(theta); vy= v0 * np.sin(theta)
x, y = 0., 0.
px, py = [], []

while Energy(y, vy) > 0.1:
  if y < 0 and vy < 0:
    vy = 0.8 * abs(vy) # 탄성계수
  x += vx * dt
  y += vy * dt
  # vx -= alpha * (vx ** 2)
  vy -= g * dt
  px.append(x)
  py.append(y)
import matplotlib.pyplot as plt
plt.plot(px, py)

# %% codecell
from matplotlib import rc
rc('animation', html='jshtml')
from matplotlib.animation import FuncAnimation

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
# %% codecell
import numpy as np

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
import matplotlib.pyplot as plt
plt.plot(px, py)

# def res(v):

# %% codecell
