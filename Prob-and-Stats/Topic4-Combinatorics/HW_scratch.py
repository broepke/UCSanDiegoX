import sys
import numpy as np
import scipy as sp
import itertools
from scipy.special import *


def compositions(k, n):
    assert n > k > 1
    to_process = [[i] for i in range(1, n + 1)]
    while to_process:
        l = to_process.pop()
        s = sum(l)
        le = len(l)
        for i in range(1, n - s + 1):
            news = s + i
            if news <= n:
                newl = list(l)
                newl.append(i)
                if le == k - 1 and news == n:
                    yield tuple(newl)
                elif le < k - 1 and news < n:
                    to_process.append(newl)


# print(set(compositions(2, 5)))

# func_out = set(compositions(2, 5))
# assert type(func_out).__name__ == "set"
# assert func_out == {(1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1)}


def composition_formula(k, n):
    # inputs: k and n are of type 'int'
    # output: a set of tuples, (int, int)

    a = len(set(compositions(k, n)))
    b = int(binom(n - 1, k - 1))
    output = (a, b)

    return output


# assert composition_formula(4, 12) == (165,165)

# print(composition_formula(9, 16))


def constrained_compositions(n, m):
    constrained_set = set(compositions(3, n))
    new_set = set()
    for i in constrained_set:
        if i[0] <= m[0]:
            if i[1] <= m[1]:
                if i[2] <= m[2]:
                    new_set.add(i)

    return new_set

print(len(constrained_compositions(20,[12, 15, 5])))


# func_out = constrained_compositions(7, [1, 4, 4])
# assert type(func_out).__name__ == "set"
# assert constrained_compositions(7, [1, 4, 4]) == {(1, 2, 4), (1, 3, 3), (1, 4, 2)}
