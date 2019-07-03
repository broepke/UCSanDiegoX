import numpy as np
from statsmodels.stats import moment_helpers as mh
from numpy import linalg as LA

# ut * SIGMA * u

sigma = np.array([[5, 3, 0], [-3, 5, 0], [0, 0, 4]])


eig = LA.eig(sigma)
print('Eigenvalues:\n', eig[0])
print('Eigenvectors:\n', eig[1])
