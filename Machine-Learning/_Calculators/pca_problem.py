import numpy as np
from math import sqrt
from numpy import linalg as LA
from scipy.spatial import distance

# covariance matrix (suplied)
sigma = np.array([[5, -3, 0], [-3, 5, 0], [0, 0, 4]])

a = sqrt(2)
b = 3 * sqrt(2)
c = 2
x = np.array([a, b, c])

# a) Consider the direction  𝑢=(1,1,1)/3‾√ .
# What is variance of the projection of the data onto direction  𝑢 ?
u = np.array([[1], [1], [1]])
u = u / sqrt(3)
u_hat = u / (u**2).sum()**0.5
u_var = np.transpose(u_hat) * sigma * u_hat
print('Variance (u) =', u_var.sum())

# b) Which of the following are eigenvectors of the
# covariance matrix? Select all that apply.
eig = LA.eig(sigma)
U = eig[1]
# Note: This returns the equiv of U^T - Tranposed. Don't need to Transpose
print('Eigenvectors:\n', U)

# c) Find the eigenvalues of the covariance matrix.
# List them in decreasing order.
print('Eigenvalues:\n', eig[0])

# d) Suppose we used principal component analysis (PCA)
# to project points into two dimensions. What would be the
# resulting two-dimensional projection of the point  𝑥=(2‾√,−32‾√,2) ?
project_x = U.dot(x)
print('Projected first two values of x onto U =', project_x[:2])

# e) Now suppose we use the projection in (d) to reconstruct a point  𝑥ˆ
# in the original three-dimensional space. What is the Euclidean
# distance between  𝑥  and  𝑥ˆ , that is,  ‖𝑥−𝑥ˆ‖ ?
# accomplished by UU^Tx
# 𝑥  is  (𝑥⋅𝑢1)𝑢1+(𝑥⋅𝑢2)𝑢2 .

u1 = x.dot(U[0]) * U[0]
u2 = x.dot(U[1]) * U[1]

reconstructed = u1 + u2

dist = distance.euclidean(x, reconstructed)

print('The euclidian distance is =', dist)
