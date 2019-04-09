import numpy as np
import pandas as pd

def metric_hp(x):
    y = x * 0.7457
    y = round(y)

    return y

def euro(x):
    y = x * 0.89
    y = round(y)

    return y

# Create the list
makes = ['ford', 'chevy', 'bmw', 'mercedes','jaguar','toyota']
model = ['mustang', 'corvette', 'm4', 'gt','f-type','supra']
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
