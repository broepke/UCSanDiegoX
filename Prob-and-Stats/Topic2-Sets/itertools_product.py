from itertools import product

Faces = set({'J', 'Q', 'K'})
Suits = {'D', "S", "H", "C"}

for i in product(Faces,Suits):
    print(i)
