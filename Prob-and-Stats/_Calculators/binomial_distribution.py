from scipy.stats import binom
import numpy as np


# Binomal Distribution
n = 8
k = 4
p = 0.5
q = 1 - p

expect = binom.expect(args=(n, p))
mean = binom.mean(n, p)
var = binom.var(n, p)
sigma = binom.std(n, p)
mode = np.floor((n + 1) * p)
pmf = binom.pmf(k, n, p)
cdf = binom.cdf(k, n, p)
ppf = binom.ppf(q, n, p)

print('expected value = ', expect)
print('mean = ', mean)
print('variance = ', var)
print('std. dev. = ', sigma)
print('mode = ', mode)
print('pmf = ', pmf)
print('cdf = ', cdf)
print('ppf = ', ppf)
