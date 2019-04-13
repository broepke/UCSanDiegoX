import numpy as np
import matplotlib.pyplot as plt

tries = []
np.random.seed(123)

for x in range(10000):
    flips = [0]
    for i in range(10):
        coin = np.random.randint(0, 2)
        flips.append(flips[i] + coin)
    tries.append(flips[-1])

plt.hist(tries, bins=10, histtype='bar', rwidth=.95, align='mid', density=True)
plt.show()
