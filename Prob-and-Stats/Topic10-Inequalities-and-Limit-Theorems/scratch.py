import math
import itertools
import collections
import numpy as np
import pandas as import pd

a = [1,2]
b = [3,4]

product = set(itertools.product(a,b))

print(product)
print(math.e)

print(math.sqrt(144))

set_1 = {'A', 'B','C','D'}
set_2 = {'C','D','E','F'}

print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.symmetric_difference(set_2))
print(len(set_1.union(set_2)))
