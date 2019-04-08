import scipy.stats as sp
import numpy as np
from math import sqrt

list = [60, 56, 61, 68, 51, 53, 69, 54]
total = 0

n = len(list) # total number of samples
mu = np.mean(list) # calculate the mean
sigma = np.std(list)
var = np.var(list)
var_u = np.var(list, ddof=1) #add ddof=1 for unbiased (Bessle Corrected)
sem = sp.sem(list)

print("mean = ", mu)
print("std. dev. = ", sigma)
print("raw variance ('S^2') = ", var)
print("unbiased sample variace = ", var_u)
print('standard error of the mean = ', sem)
print("standard error = ", sigma/sqrt(n))
