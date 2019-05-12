from scipy.stats import bernoulli
import numpy as np


k = 3
p = 0.4

expect = bernoulli.expect(args=(p,), loc=0)
mean = bernoulli.mean(p)
var = bernoulli.var(p)
sigma = bernoulli.std(p)
pmf = bernoulli.pmf(k, p, loc=0)
cdf = bernoulli.cdf(k, p, loc=0)


print('expected = ', expect)
print('mean = ', mean)
print('variance = ', var)
print('std. dev. = ',sigma)
print('pmf = ', pmf)
print('cdf = ', cdf)
