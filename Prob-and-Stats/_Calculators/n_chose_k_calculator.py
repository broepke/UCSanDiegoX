from math import factorial
from scipy import special as sp

target = 10
k = 2
A = set()

for i in range(1, target + 1):
    A.add(i)

print("n =", A)
print("k =", k)

n = len(A)

# Print |A|!/(k!(|A|-k)!) directly
print("Size = {}!/({}!({}-{})!)={}".format(n, k, n, k,
                                           int(factorial(len(A)) / (factorial(k) * factorial(len(A) - k)))))


# Alternatively you can calculate this with scipy.special.binom
# this takes two simple parameters, n, and k.
n_k = sp.binom(n,k)
print(n_k)
