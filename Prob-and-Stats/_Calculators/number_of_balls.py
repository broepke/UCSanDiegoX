# Used to calculate this problem

# Six balls are numbered 1, 2, 3, 4, 5, and 6. What is the chance that the numbers
# on three balls, picked simultaneously and randomly, will sum to a multiple of 3?

# the easier math on this is nCk or n! / k! * (n-k)! -
# then you need the number of those that are divisibile by 3.  I don't know this other
# than by the code - lol ;)

import itertools
from scipy.special import *

A = {1, 2, 3, 4, 5, 6}
k = 3
n = len(A)

# Print all the k-combinations of A
choose_k = list(itertools.combinations(A, k))
print("{}-combinations of {}: {}".format(k, A, choose_k))
print("Number of combinations = {}".format(len(choose_k)))

# Print |A|!/(k!(|A|-k)!) directly
print("Size = %{}!/(%{}!(%{}-%{})!)={}".format(n, k, n, k,
                                               int(factorial(len(A)) / (factorial(k) * factorial(len(A) - k)))))

counter = 0

for i in choose_k:
    if sum(i) % 3 == 0:
        counter += 1

print('Probability of chosing a sum of a multiple of 3 from 6 balls is =',
      counter / len(choose_k))
