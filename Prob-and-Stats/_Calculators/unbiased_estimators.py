import scipy.stats as sp
import numpy as np
from math import sqrt

list = [60, 56, 61, 68, 51, 53, 69, 54]
total = 0

n = len(list) # total number of samples
mu = np.mean(list) # calculate the mean
sigma = np.std(list)
var = np.var(list)
sem = sp.sem(list)

print("mean = ", mu)
print("std. dev. = ", sigma)
print("raw variance ('S^2') = ", var)
print('standard error of the mean = ', sem)

# Calculate the "Unbiased Sample Variance"
for i in list:
    total += (i-mu)**2

print("unbiased sample variace = ",total/(n-1))

# Calculate it another way
#print(var * (n/(n-1)))

# Raw variance is also Std.Dev Squared
# print(sigma**2)
