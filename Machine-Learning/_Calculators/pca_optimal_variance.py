import numpy as np
from statsmodels.stats import moment_helpers as mh
from math import sqrt


sigma = np.array([[5, -3, 0], [-3, 5, 0], [0, 0, 4]])
x1 = np.array([[1], [0], [0]])
x2 = np.array([[0], [-1], [0]])
x3 = np.array([[1], [1], [1]])
x3_hat = x3 / (x3**2).sum()**0.5

print('Original Matrix')
print(sigma)


x1_var = np.transpose(x1) * sigma * x1
x2_var = np.transpose(x2) * sigma * x2
x3_var = np.transpose(x3_hat) * sigma * x3_hat

print('Variance (x1) = \n', x1_var)
print('Variance (x2) = \n', x2_var)
print('Variance (x3) =', x3_var.sum())

print()
print('Cov 2 Corr')
print(mh.cov2corr(sigma))
