import numpy as np
import numpy_sugar as sug

a = np.array([[1, -1], [-1, 1]])
a = a.astype(float)
print(a)
print('Positive Semidefinite via Sugar =',
      sug.linalg.check_semidefinite_positiveness(a))

'''
The heierarchy of square matricies:
Square
Symmetric
Positive Semidefinite
'''

# First check if the matrix is sqare
def check_square(a):
    '''checks to see if the matrix is square'''
    return all(len(row) == len(a) for row in a)

# Next check if the matrix = transpose of matrix
def check_symmetric(a, rtol=1e-05, atol=1e-08):
    '''returns a bool on whether or not the matrix is symmetric'''
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


print('Matrix is Square =', check_square(a))
print('Matrix is Symmetric =', check_symmetric(a))

b = np.transpose(a)
c = a * b
print(c)
if c.all() > 0:
    print('Positive = True')
else:
    print('Positive = False')
