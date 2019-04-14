import numpy as np
from scipy.stats import norm, t, sem, moment
from math import sqrt

# from the SAT Score Question
list = [560, 610, 500, 470, 660, 640]
p = 0.90

# Elephan Trunk
# List = [5.62, 6.07, 6.64, 5.91, 6.30, 6.55, 6.19, 5.48]
# p = 0.95

total = 0
n = len(list)
mu = np.mean(list)
var = np.var(list, ddof=1)  # add ddof=1 for unbiased (Bessle Corrected)
bounds = t.interval(p, len(list)-1, loc=np.mean(list), scale=sem(list))
critical_t = t.ppf(((1+p)/2),n-1)

sigma_est = sqrt(var)
std_error = critical_t * sigma_est / sqrt(n)

print('Mean =', mu)
print('Critical T =', critical_t)
print('Unbiased Sample Variace (Bessel Corrected) = ', var)
print('Standard Deviation (Estimation) =', sigma_est)
print('Standard Error =', std_error)
print('Lower Bounds =', bounds[0])
print('Upper Bounds =', bounds[1])
