import numpy as np
from statsmodels.stats import moment_helpers as mh
from numpy import linalg as LA



M = np.array([[1, -2], [-2, 1]])
eig = LA.eig(M)

U = eig[1]
UT = np.transpose(eig[1])
Lambda = np.array([[eig[0][0],0],[0,eig[0][1]]])


spec_decomp = U.dot(Lambda.dot(UT))

print(U)
print(Lambda)
print(UT)

print(M)
print(spec_decomp)
