import numpy as np
from scipy.stats import hypergeom

# Suppose you have a jar containing 10 red marbles and 90 black marbles.
# You collect 10 marbles from the jar.
# What is the probability you collect k red marbles?

# The population size, usually denoted N.
# In this case, the total number of marbles in the jar: 100.
# The number of “successes” in the population, usually denoted K.
# In this case, the number of red marbles in the jar: 10.
# The sample size, usually denoted n.
# In this case, the number of draws from the jar: 10.

# M is the population size (previously N)
# n is the number of successes in the population (previously K)
# N is the sample size (previously n)
# X is still the number of drawn “successes”.

M = 10
n = 3
N = 3
x = 3

pval = hypergeom.sf(x-1, M, n, N)

print(pval)
