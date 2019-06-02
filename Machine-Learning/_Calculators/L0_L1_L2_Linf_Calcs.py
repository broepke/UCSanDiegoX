import numpy as np

# x = np.array([1, 2, -1, 3])

# Calculate the varius distances between two arrays (euclidian = L2)
x = np.array([63.03, 22.55, 39.61, 40.48, 98.67, -0.25])
y = np.array([43.92, 14.18, 37.83, 29.74, 134.46, 6.45])

if x.ndim < 2:
    print("L0 length of the vector:")
    print(np.linalg.norm(x-y, ord=0),'\n')

print("L1 length of the vector:")
print(np.linalg.norm(x-y, ord=1),'\n')

print("L2 length of the vector:")
print(np.linalg.norm(x-y, ord=2),'\n')

print("Infinity (max) length of the vector:")
print(np.linalg.norm(x-y, np.inf))

# A spherical Gaussian has mean  𝜇=(1,0,0) .
# At which of the following points will the density be
# the same as at (1,1,0)? Select all that apply.

print('')
mu = np.array([1,0,0])
a = np.array([1,1,0])
b = np.array([0,0,0])
c = np.array([1,1,1])
d = np.array([2,0,0])
e = np.array([1,0,1])

print('base', np.linalg.norm(mu-a, ord=2))
print('1', np.linalg.norm(mu-b, ord=2))
print('2', np.linalg.norm(mu-c, ord=2))
print('3', np.linalg.norm(mu-d, ord=2))
print('4', np.linalg.norm(mu-e, ord=2))
