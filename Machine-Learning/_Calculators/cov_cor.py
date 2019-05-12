import numpy as np

x = np.array([[0, 0, 1/3], [0, 1/3, 0], [1/3, 0, 0]]).T

x = np.array([-1,0,1])
y = np.array([-1,0,1])


print(x)

print(np.cov(x+y))
print(np.corrcoef(x))
