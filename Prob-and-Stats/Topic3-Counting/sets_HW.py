def union(A, B):
    my_union = A | B
    my_output = (my_union, len(my_union))

    return my_output


def inclusion_exclusion(A, B):
    inter_ab = A & B
    union_ab = A | B

    my_output = (len(A), len(B), len(inter_ab), len(union_ab))

    return my_output


A = {1, 4, -3, "bob"}
B = {2, 1, -3, "jill"}
print("union = ", union(A, B))

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
print("inclusion exclusion = ", inclusion_exclusion(A, B))
