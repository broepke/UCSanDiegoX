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

def metric_hp(x):

    y = x * 0.7457
    y = round(y)

    return y

def euro(x):

    y = x * 0.89
    y = round(y)

    return y

makes = ['ford', 'chevy', 'bmw', 'mercedes','jaguar','toyota']
model = ['mustang', 'corvette', 'm4', 'gt','f-type','gr supra']
hp = [500,350,425,550, 425, 450]
country = ['usa', 'usa', 'germany', 'germany', 'uk', 'japan']
base_msrp = [26900, 55900, 69150, 113500, 61600, 55250]

cars_dict = {}
cars_dict['makes'] = makes
cars_dict['model'] = model
cars_dict['hp'] = hp
cars_dict['country'] = country
cars_dict['msrp'] = base_msrp

cars = pd.DataFrame(cars_dict)

# Add a column to a data from using the apply method
cars['metric_hp'] = cars['hp'].apply(metric_hp)
cars['msrp_euro'] = cars['msrp'].apply(euro)

print(cars)

# Some random nupy stuff
