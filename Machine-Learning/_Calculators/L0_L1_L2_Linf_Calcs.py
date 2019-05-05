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
