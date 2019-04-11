from scipy.stats import geom
import numpy as np


k = 1
p = 0.3

expect = geom.expect(args=(p,), loc=0)
mean = geom.mean(p)
var = geom.var(p)
sigma = geom.std(p)
pmf = geom.pmf(k, p, loc=0)
cdf = geom.cdf(k, p, loc=0)
ex2 = var + expect**2

print('expected = ', expect)
print('mean = ', mean)
print('variance = ', var)
print('std. dev. = ',sigma)
print('pmf = ', pmf)
print('cdf = ', cdf)
print("E[X]^2 = ",ex2)
