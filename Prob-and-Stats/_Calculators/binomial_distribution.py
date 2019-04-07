from scipy.stats import binom
import numpy as np


# Binomal Distribution
n = 10
p = 0.7

expect = binom.expect(args=(n, p))
mean = binom.mean(n,p)
var = binom.var(n, p)
sigma = binom.std(n, p)
mode = np.floor((n+1)*p)

print('expected value = ',expect)
print('mean = ', mean)
print('variance = ', var)
print('std. dev. = ',sigma)
print('mode = ', mode)
