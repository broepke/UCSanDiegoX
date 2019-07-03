import numpy as np

v = np.array([4,1,1,9,1])

v_hat = v / (v**2).sum()**0.5

print('The Unit Vector Is =', v_hat)

# What is the projection of the
# vector  (3,5,−9)  onto the direction  (0.6,−0.8,0) ?
# HINT:  If  𝑢  is a unit vector, then the projection
# of  𝑥  onto direction  𝑢  is simply  𝑢⋅𝑥 .
x = np.array([3, 5, -9])
y = np.array([0.6, -0.8, 0])

print('The Projection Is =', np.dot(x, y))
