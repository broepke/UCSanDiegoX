import numpy as np

x = np.array([1, 2, -1, 3])

# for a 2D array use this - you can use a 1D or 2D with this
x = np.array([[1, 2], [-1, 3]])

print(x)

if x.ndim < 2:
    print("L0 length of the vector:")
    print(np.linalg.norm(x, ord=0))

print("L1 length of the vector:")
print(np.linalg.norm(x, ord=1))

print("L2 length of the vector:")
print(np.linalg.norm(x, ord=2))

print("Infinity (max) length of the vector:")
print(np.linalg.norm(x, np.inf))
