from itertools import product


def complement_of_union(A, B, U):
    # inputs: A, B and U are of type 'set'
    # output: a tuple of the type (set, set)
    unionAB = A | B
    comp_unionAB = U - unionAB

    return (unionAB, comp_unionAB)


def intersection_of_complements(A, B, U):
    # inputs: A, B and U are of type 'set'
    # output: a tuple of the form (set, set)
    compA = (B | U) - A
    compB = (A | U) - B

    isecAB = compA & compB

    return (compA, isecAB)


def product_of_unions(A, B, S, T):
    # inputs: A, B, S and T are sets
    # output: a tuple of the type (set, set)

    final_set = set()

    AunionB = A | B
    SunionT = S | T

    for i in product(AunionB, SunionT):
        final_set.add(i)

    final_tuple = (AunionB, final_set)

    return final_tuple


def union_of_products(A, B, S, T):
    # inputs: A, B, S and T are sets
    # output: a tuple of the type (set, set)

    AxS = set()
    AxT = set()
    BxS = set()
    BxT = set()
    final_set = set()
    final_tuple = ()

    for i in product(A, S):
        AxS.add(i)

    for i in product(A, T):
        AxT.add(i)

    for i in product(B, S):
        BxS.add(i)

    for i in product(B, T):
        BxT.add(i)

    # Final AxS | AxT | BxS | BxT
    final_set = AxS
    final_set = final_set.union(AxT)
    final_set = final_set.union(BxS)
    final_set = final_set.union(BxT)

    final_tuple = (AxS, final_set)

    return final_tuple


A = {-6, 3, 4, 5}
B = {-6, 5, 13}
U = A | B | {12, -2, -4}

# print('Compliment of Products = ', complement_of_union(A, B, U))

# print('Intersection of Compliments = ', intersection_of_complements(A, B, U))

# print('\n##########\n')

A = {5}
B = {5}
S = {-1, 0}
T = {0}

# print('Product of Unions = ', product_of_unions(A, B, S, T))


print('Union of Products', union_of_products(A, B, S, T))