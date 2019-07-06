from math import factorial
from scipy import special as sp


# binomial theorem.  a.k.a = N choose K.
n = 10
k = 2

n_k = sp.binom(n,k)
print(n_k)
