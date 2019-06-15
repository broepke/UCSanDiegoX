
'''
The second derivatives are given by the Hessian matrix.
Here is a Python implementation for ND arrays,
that consists in applying the np.gradient twice and
storing the output appropriately,
'''
import numpy as np


def hessian(x):
    """
    Calculate the hessian matrix with finite differences
    Parameters:
       - x : ndarray
    Returns:
       an array of shape (x.dim, x.ndim) + x.shape
       where the array[i, j, ...] corresponds to the second derivative x_ij
    """
    x_grad = np.gradient(x)
    hessian = np.empty((x.ndim, x.ndim) + x.shape, dtype=x.dtype)
    for k, grad_k in enumerate(x_grad):
        # iterate over dimensions
        # apply gradient again to every component of the first derivative.
        tmp_grad = np.gradient(grad_k)
        for l, grad_kl in enumerate(tmp_grad):
            hessian[k, l, :, :] = grad_kl
    return hessian



# x = np.random.randn(100, 100, 100)
x = np.array([[-1,1],[1,-1]])
print(hessian(x))
