from scipy.stats import poisson
import numpy as np


# Assume the number of typo errors on a single page of a book follows
# Poisson distribution with parameter 1/3. Calculate the probability
# that on one page there are
# no typos (pmf(0,1/3) = 0.7165313105737893)
# exactly two typos = (pmf(0,1/3) = 0.03980729503187717)

k = 1
mu = 2.5

expect = poisson.expect(args=(mu,), loc=0)
mean = poisson.mean(mu)
var = poisson.var(mu)
sigma = poisson.std(mu)
pmf = poisson.pmf(k, mu, loc=0)
cdf = poisson.cdf(k, mu, loc=0)
e_x_squared = mu**2 + mu

print('expected = ', expect)
print('mean = ', mean)
print('variance = ', var)
print('std. dev. = ',sigma)
print('pmf = ', pmf)
print('cdf = ', cdf)
print('E[X]^2 = ', e_x_squared)
