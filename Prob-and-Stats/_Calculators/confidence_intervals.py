import numpy as np
from scipy.stats import norm, t, sem
from math import sqrt

# list = [60, 56, 61, 68, 51, 53, 69, 54, 80, 90, 55, 35, 45]
list = np.random.randint(low=35,high=71, size=20)
print(list)

n = len(list)
mu = np.mean(list)
sigma = np.std(list)
var = np.var(list)
bounds = t.interval(0.90, len(list)-1, loc=np.mean(list), scale=sem(list))

print('The Mean Is =', mu)
print('The Raw Variance ("S^2") Is =', var)
print('The Standard Deviation Is =', sigma)
print('Lower Bounds =', bounds[0])
print('Upper Bounds =', bounds[1])

# the number of tweets a random user is a random variable with sigma=2
# in a sample of 121 users, the sample mean was 3.7
# find the 95% confidence interval for the distribtuion mean.
ci = 0.95
sig = 2
mean = 3.7
users = 121
inv_theta = norm.ppf((1+ci)/2)
std_error = sig/sqrt(users)

tweets_lower = mean - (inv_theta*std_error)
tweets_upper = mean + (inv_theta*std_error)

print('the bounds of number of tweets is =', tweets_lower, tweets_upper)

# tweets =
