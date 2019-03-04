from math import factorial

target = 7
k = 5
A = set()

for i in range(1,target+1):
    A.add(i)

print("n =",A)
print("k =",k)

n = len(A)

# Print |A|!/(k!(|A|-k)!) directly
print("Size = {}!/({}!({}-{})!)={}".format(n,k,n,k,int(factorial(len(A))/(factorial(k)*factorial(len(A)-k)))))
