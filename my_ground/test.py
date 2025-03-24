import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np
import random

plt.style.use("cyberpunk")
ax = plt.subplot()

while True:
    point_list = []
    for x in range(random.randint(1,10)):
        point_list.append(random.randint(0, 15))

    ax.set(xlim = point_list)
plt.show()