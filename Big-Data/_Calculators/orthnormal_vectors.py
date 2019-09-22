import numpy as np
from math import sqrt

u1 = np.array([1/sqrt(2), 0, -(1/sqrt(2))])
u2 = np.array([1/2, 1/sqrt(2), 1 / 2])
u3 = np.array([1/2, -(1/sqrt(2)), 1/2])

print('two norm magnitude of u1 =', round(np.linalg.norm(u1, ord=2)))
print('two norm magnitude of u2 =', round(np.linalg.norm(u2, ord=2)))
print('two norm magnitude of u3 =', round(np.linalg.norm(u3, ord=2)))

print('u1 dot u2 =', u1.dot(u2))
print('u2 dot u3 =', (round(u2.dot(u3),3)))
print('u1 dot u3 =', u1.dot(u3))

print('u1 Dot product with itself =', round(u1.dot(u1)))
