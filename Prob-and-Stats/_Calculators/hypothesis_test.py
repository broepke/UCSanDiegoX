from scipy.stats import t, ttest_ind, ttest_1samp, ttest_rel
import numpy as np
from math import sqrt

# T-Test - Tesla Example from Class
mean_assumption = .5
sample = [1,1,1,0]


# using manual calulations for most of the t-test.  From class
mu = np.mean(sample)
sigma = np.std(sample)
var = np.var(sample, ddof=1)
n = len(sample)
t_stat = (mu - mean_assumption) / sqrt(var / n)
p_value = 1 - t.cdf(t_stat, n - 1)
print('t statistic =', t_stat)
print('p value =', p_value)

print()

## using the built in method for the t-test from scipy
tt = ttest_1samp(sample, mean_assumption)
print('t statistic =', tt[0])
print('two sided test =', tt[1])
print('one sided test =', tt[1]/2)
