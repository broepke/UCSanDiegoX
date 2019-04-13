from scipy import stats
import numpy as np

# The location (loc) keyword specifies the mean.
# The scale (scale) keyword specifies the standard deviation.

np.random.seed(12345678)
mu = 68
sigma = 4
n = 10

rvs1 = stats.norm.rvs(loc=mu, scale=sigma, size=n)
rvs2 = stats.norm.rvs(loc=mu, scale=sigma, size=n)

a = stats.ttest_ind(rvs1, rvs2)
print(a)

rvs = stats.norm.rvs(loc=mu, scale=sigma, size=n)

print(rvs)
print('check the actual mean of the array = ', np.mean(rvs))
print('check the actual std. dev. of array', np.std(rvs))

b = stats.ttest_1samp(rvs, mu)
c = stats.ttest_1samp(rvs, 0.0)

print(b)
print(c)
