import numpy as np
from scipy.stats import norm, t, sem, bayes_mvs
# instead of using a z-table you can use scipy to calcualte Theta
#
# a = theta^-1 (1+p/2)
#
# below is the 68-95-99.7 rule of 1,2,3 standard deviations
# e.g. if you go out +/- three standard deviations
# you will have 99.7% of the total set of outcomes
dev_1 = 2 * norm.cdf(1) - 1
dev_2 = 2 * norm.cdf(2) - 1
dev_3 = 2 * norm.cdf(3) - 1

print('1-2-3 standard deviations')
print(dev_1)
print(dev_2)
print(dev_3)

# use the ppf fucntion to calcualte the inverse of Theta
inv_1 = norm.ppf(.90)
inv_2 = norm.ppf(.95)
inv_3 = norm.ppf(.99)

print('inverse calcualtions = the number of standard deviations you need from mean')
print(inv_1)
print(inv_2)
print(inv_3)
