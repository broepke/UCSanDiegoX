import math
import itertools
import collections
import numpy as np
import pandas as pd

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

makes = ['ford', 'chevy', 'bmw', 'mercedes']
model = ['mustang', 'corvette', 'm4', 'gt']
hp = [500,350,425,550]
cars_dict = {}
cars_dict['makes'] = makes
cars_dict['model'] = model
cars_dict['hp'] = hp

cars = pd.DataFrame(cars_dict)

# Add a column to a data from using the apply method

cars['metric_hp'] = cars['hp'].apply(np.sqrt)


print(cars)
