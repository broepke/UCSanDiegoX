import numpy as np
from scipy.spatial import distance

a = np.array([1,1])
b = np.array([1,3])

c = np.array([4,4])

print(type(a), type(b))
print(a, b)

# calculate the euclidean distance between two matricies
dist1 = distance.euclidean(a,b)
dist2 = distance.euclidean(a,c)
dist3 = distance.euclidean(b,c)

print(dist1)
print(dist2)
print(dist3)
