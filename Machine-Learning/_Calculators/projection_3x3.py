import numpy as np
from statsmodels.stats import moment_helpers as mh
from math import sqrt

# ut * SIGMA * u

sigma = np.array([[4, 2, -3], [2, 9, 0], [-3, 0, 9]])

x1 = np.array([[1], [1], [0]])
x1_hat = x1 / (x1**2).sum()**0.5


x1_var = np.transpose(x1_hat) * sigma * x1_hat


print('Variance (x1) =', x1_var.sum())
