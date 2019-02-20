from math import factorial
import itertools

target = 25
k = 19
A = set()

for i in range(1,target+1):
    A.add(i)

n = len(A)

# Print all the k-combinations of A
choose_k = list(itertools.combinations(A,k))
print("{}-combinations of {}: {}".format(k,A,choose_k))
print("Number of combinations = {}".format(len(choose_k)  ))

# Print |A|!/(k!(|A|-k)!) directly
print("Size = %{}!/(%{}!(%{}-%{})!)={}".format(n,k,n,k,int(factorial(len(A))/(factorial(k)*factorial(len(A)-k)))))
