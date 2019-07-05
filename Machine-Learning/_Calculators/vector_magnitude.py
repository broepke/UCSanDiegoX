import numpy as np
from math import sqrt

x = np.array([1, 3])
y = np.array([1, 0])


# Calculate the magnitude manually
def magnitude(array):

    mag = 0
    # Sum the Squares of Each Value
    for i in array:
        mag += i**2

    # Take the SqRt of those sums
    mag = sqrt(mag)

    return mag


print(magnitude(x))
print(magnitude(y))

# Use numpy to Calculate the same
print(np.linalg.norm(x))
print(np.linalg.norm(y))


# Get the unit vector to compare
x_hat = x / (x**2).sum()**0.5
print(x_hat)
