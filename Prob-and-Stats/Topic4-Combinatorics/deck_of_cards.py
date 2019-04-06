import itertools
from math import factorial


vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['S', 'C', 'H', 'D']

A = set(itertools.product(vals, suits))
k = 5
n = len(A)

# Print all the k-combinations of A
# choose_k = list(itertools.combinations(A,k))
# print("{}-combinations of {}: {}".format(k,A,choose_k))
# print("Number of combinations = {}".format(len(choose_k)  ))

# Print |A|!/(k!(|A|-k)!) directly
print(int(factorial(len(A))/(factorial(k)*factorial(len(A)-k))))
