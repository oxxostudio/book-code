# Copyright © https://steam.oxxostudio.tw

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(3,2), dpi=150)
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [])
line.set_data([], [])
x = np.linspace(0, 2, 100)
y = np.sin(5 * np.pi * x)
line.set_data(x, y)

plt.show()

