import numpy as np
from math import sqrt

x = np.array([1, 3])
y = np.array([1, 0])


# Calculate the magnitude manually
def magnitude(array):

    mag = sqrt(np.sum([array ** 2]))

    return mag


print('manual calc x =', magnitude(x))
print('manual calc y =', magnitude(y))

# Use numpy to Calculate the same
print('numpy calc y =', np.linalg.norm(x))
print('numpy calc y =', np.linalg.norm(y))


# Get the unit vector to compare
x_hat = x / (x**2).sum()**0.5
print('Unit Vector for x', x_hat)

print('Lenth of of Unit Vector =', np.linalg.norm(x_hat))
