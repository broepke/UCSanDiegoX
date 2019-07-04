import numpy as np
from numpy import linalg as LA

# When you calcualte Eigenvalues and Eigenvectors on a diagnal matrix

# [ 2  0  0]
# [ 0 -1  0]
# [ 0  0 10]

sigma = np.array([[2, 0, 0], [0, -1, 0], [0, 0, 10]])
print(sigma)

eig = LA.eig(sigma)
print('Eigenvalues:\n', eig[0])
print('Eigenvectors:\n', eig[1])

'''
Eigenvalues:
 [ 2. -1. 10.]
Eigenvectors:
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
 '''
