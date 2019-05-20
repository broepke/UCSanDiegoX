import numpy as np
from math import sqrt

# Basic Vectors
x = np.array([1,1])
y = np.array([3,9])

print('Dot Product =', np.dot(x,y))

# Vectors are right angles when their dot product == 0
x = np.array([-4,3])
y = np.array([3,4])

print('Vectors at right angles =', np.dot(x,y))

# Transpose, Add, and Subract two arrays
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[-1,0,1],[1,-1,0]])

print('Transpose =\n', np.transpose(a))
print('Add Matrix =\n',a+b)
print('Subract Matrix =\n', a-b)

# Two arrays - Dot Product and Angle
x = np.array([1,0,-1])
y = np.array([0,1,-1])

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2':: """

    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


print('Dot Product =', np.dot(x,y))
print('Angle in Degrees =', np.rad2deg(angle_between(x,y)))

# In general, to get a unit vector in the same direction as x
# we simply divide by the L2 norm of x
l = np.array([1,2,3])

print('L2 norm =', np.linalg.norm(l, ord=2))
print('For validation the above number is SqRt of 14 =', sqrt(14))

# Identity Matrix
print('Identity Matrix = \n',np.identity(5))

# Inverse of a Matrix
a = np.array([[1,5],[1,4]])
print(np.linalg.inv(a))

# A singular matrix does not have an inverst - like this
a = np.array([[3,1],[3,1]])
try:
    inv = np.linalg.inv(a)
except:
    print('there is no inverse')

# The following demonstrates "x^Tx" (first one) and xx^T
# for the first, it's the length of the vector squared
# for the second, a full NxN matrix is created
x = np.array([[1],[3],[5]])
xt = np.transpose(x)

print(np.dot(xt,x))
print(np.dot(x,xt))
