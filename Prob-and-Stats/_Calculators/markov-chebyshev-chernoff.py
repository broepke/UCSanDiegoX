import math
from scipy.stats import binom

def Markov(n, p, c):
  return 1.0/c

def Chernoff(n, p, c):
  d = c-1
  m = n*p
  return math.exp(-d**2/(2+d)*m)

def Chebyshev(n, p, c):
  m = n*p
  s = math.sqrt(n*p*(1-p))
  k = m*(c-1)/s
  return 1/k**2

# n = number of occourances
# p = probability of occurance
# c =

# For the binomial distribution X∼Bp,n with mean μ=np and variance σ**2=np(1−p),
# we would like to upper bound the probability  P(X≥c⋅μ) for  c≥1.
# Three bounds introduced:

print('Markov: ',Markov(100,0.2,1.5))
print('Chebyshev: ',Chebyshev(100,0.2,1.5))
print('Chernoff: ',Chernoff(100,0.2,1.5))
