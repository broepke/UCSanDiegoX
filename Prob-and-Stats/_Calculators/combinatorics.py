import itertools
from math import factorial

def combinations(A,k):
    if k==1:
        return [{x} for x in A]
    sets = []
    for x in A:
        for y in combinations(A-{x},k=k-1):
            if {x}|y not in sets:
                sets.append({x}|y)
    return sets


print('\n#### FACTORIAL ####\n')

N = 5

# Find the factorial of a number
print(factorial(N))

print('\n#### PERMUTATIONS ####\n')

A = {1, 2, 3}

# Find all permutations of A and |A!|
permute_all = set(itertools.permutations(A))
print("Permutations of {}: {}".format(A,permute_all))
print("Number of permutations: ", len(permute_all))

print('\n#### PARTIAL PERMUTATIONS ####\n')

A = {1, 2, 3, 4}
k = 3
n = len(A)

# Print all the k-permutations of A
permute_k = list(itertools.permutations(A, k))
print("{}-permutations of {}: {}".format(k,A,permute_k))
print("Size =  = {}".format(len(permute_k)))

print('\n#### COMBINATIONS ####\n')

A = {3, 4, 5}
k = 3

# Print all the k-combinations of A
choose_k = list(itertools.combinations(A,k))
print("{}-combinations of {}: {}".format(k,A,choose_k))
print("Number of combinations = {}".format(len(choose_k)  ))

# Print |A|!/(k!(|A|-k)!) directly
print("Size = %{}!/(%{}!(%{}-%{})!)={}".format(n,k,n,k,int(factorial(len(A))/(factorial(k)*factorial(len(A)-k)))))

print('\n#### TWO COMBINATIONS ####\n')

A = {'a', 'b', 'c', 'd'}
k = 2

# Print all the k-combinations of A
choose_k = list(combinations(A,k))
print("%i-combinations of %s:\n" %(k,A))
for i in range(0, len(choose_k)):
    print(''.join(choose_k[i]) )
print("Size = %i!/(%i!(%i-%i)!) = " %(n,k,n,k), len(choose_k))