import numpy as np


def constrained_compositions(n, m):
    k = len(m)
    parts = set()
    if k == n:
        if 1 <= min(m):
            parts.add((1,) * n)
    if k == 1:
        if n <= m[0]:
            parts.add((n,))
    else:
        for x in range(1, min(n - k + 2, m[0] + 1)):
            for y in constrained_compositions(n - x, m[1:]):
                parts.add((x,) + y)
    return parts


def largest_face(f, x_max):
    for i in f:
        if i < x_max:
            f.remove(i)

    print(f)

    total_prob = 0

    for j in f:
        if j != x_max:
            total_prob = total_prob
        else:
            if total_prob == 0:
                total_prob = (f[0] - x_max) / f[0]
            else:
                total_prob = total_prob * ((j - x_max) / j)

    return total_prob


def face_sum(m, s):
    total_sum = 0
    total_comps = set(constrained_compositions(s, m))

    for i in m:
        if total_sum == 0:
            total_sum = m[0]
        else:
            total_sum *= i

    return len(total_comps) / total_sum


print(largest_face([2, 5, 7, 3], 3))

# assert abs(largest_face([5], 3) - 0.19999999999999996) < 10 ** -5
# assert abs(largest_face([11, 5, 4], 5) - 0.16363636363636364) < 10 ** -5
# assert abs(largest_face(range(1, 10), 3) - 0.011348104056437391) < 10 ** -5

assert abs(face_sum([2, 2], 2) - 0.25) < 10 ** -5
assert abs(face_sum([2, 2], 10) - 0.0) < 10 ** -5
assert abs(face_sum(range(1, 10), 20) - 0.03037092151675485) < 10 ** -5
