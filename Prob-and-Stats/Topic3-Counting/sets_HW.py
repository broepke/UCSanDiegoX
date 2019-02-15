def union(A, B):
    my_union = A | B
    my_output = (my_union, len(my_union))

    return my_output


def inclusion_exclusion(A, B):
    inter_ab = A & B
    union_ab = A | B

    my_output = (len(A), len(B), len(inter_ab), len(union_ab))

    return my_output


def union3(A, B, C):
    int_ab = A & B
    int_bc = B & C
    int_ca = C & A
    int_abc = A & B & C
    union_abc = A | B | C

    inc_ex = len(A) + len(B) + len(C) - len(int_ab) - len(int_bc) - len(int_ca) + len(int_abc)

    my_output = (union_abc, inc_ex)

    return my_output


def inclusion_exclusion3(A, B, C):
    # Inclusion Exclusion for Intersection
    union_ab = A | B
    union_bc = B | C
    union_ca = C | A
    union_abc = A | B | C

    inc_ex_int = len(A) + len(B) + len(C) - len(union_ab) - len(union_bc) - len(union_ca) + len(union_abc)

    # Inclusion Exclusion for Unions
    int_ab = A & B
    int_bc = B & C
    int_ca = C & A
    int_abc = A & B & C

    inc_ex_union = len(A) + len(B) + len(C) - len(int_ab) - len(int_bc) - len(int_ca) + len(int_abc)

    return (inc_ex_int, inc_ex_union)


A = {1, 4, -3, "bob"}
B = {2, 1, -3, "jill"}
print("union = ", union(A, B))

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
print("inclusion exclusion = ", inclusion_exclusion(A, B))

A = {1, 2, 4, 5, 10}
B = {5, 2, -6, 5, 8, 9}
C = {2, 10, 13}
print("union3 = ", union3(A, B, C))

A = {1, 2, 4, 5, 10}
B = {5, 2, -6, 5, 8, 9, 10}
C = {2, 10, 13}
print("union and intersection inclusion exclusion = ", inclusion_exclusion3(A, B, C))
