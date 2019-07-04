import numpy as np
from numpy import linalg as LA

sigma = np.array([[1, 0.85], [0.85, 1]])
x1 = np.array([[1], [0]])
x2 = np.array([[0], [1]])
x3 = np.array([1, 1])

# Get the unit vector for the [1,1]
x3_hat = x3 / (x3**2).sum()**0.5
print(x3_hat)

# Run all three different vectors, to see which one has the
# Largest Variance
x1_var = np.transpose(x1) * sigma * x1
x2_var = np.transpose(x2) * sigma * x2
x3_var = np.transpose(x3_hat) *sigma * x3_hat

print('x1 direction =', x1_var[0][0])
print('x2 direction =', x2_var[1][1])
print('x1x2 Variance =', x3_var.sum())

# The optimal direction is simply the first eivenvector of sigmal
# corresponding to the related eigenvalue
# notice how the first Eigenvalue is the same as the [1,1] vectors
# however, this method below tells you how to get the biggest automatically
eig = LA.eig(sigma)
print('Eigenvalues:\n', eig[0])
print('Eigenvectors:\n', eig[1])
