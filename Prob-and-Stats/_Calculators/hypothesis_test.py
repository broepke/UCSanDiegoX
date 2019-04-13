from scipy.stats import t, ttest_ind, ttest_1samp
import numpy as np
from math import sqrt

# T-Test - Tesla Example from Class

mean_assumption = 4.0
sample = [3.74, 4.73, 3.85, 3.96, 4.11, 4.30, 4.28, 4.02]
mu = np.mean(sample)
sigma = np.std(sample)
var = np.var(sample, ddof=1)
n = len(sample)
t_stat = (mu - mean_assumption) / sqrt(var / n)
p_value = 1 - t.cdf(t_stat, n - 1)

print('mean =', mu)
print('variation (bessel corrected) =', var)
print('t statistic =', t_stat)
print('p value =', p_value)
