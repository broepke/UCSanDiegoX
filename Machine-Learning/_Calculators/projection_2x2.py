import numpy as np

# ut * SIGMA * u


sigma = np.array([[1, 0.85], [0.85, 1]])
x1 = np.array([[1], [0]])
x2 = np.array([[0], [1]])
x3 = np.array([1, 1])

x3_hat = x3 / (x3**2).sum()**0.5


x1_var = np.transpose(x1) * sigma * x1
x2_var = np.transpose(x2) * sigma * x2
x3_var = np.transpose(x3_hat) * sigma * x3_hat



print('Upper Left Number (x1 direction) = \n', x1_var)
print(x2_var)
print(x3_var)
print(x3_var.sum())
