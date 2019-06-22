import numpy as np
from scipy.misc import derivative


def f(x):
    return x**3 + x**2


y = derivative(f, 1.0, dx=1e-6)

print(y)
