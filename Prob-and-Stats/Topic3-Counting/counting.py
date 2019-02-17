# target = 2016
# counter = 0
#
# for i in range(1,target+1):
#     if target % i == 0:
#         counter += 1
#         print(i)
#
# print('Total numbers divible by ' + str(target) + ' = ' + str(counter))


A = {'00000', '10000', '20000', '00001', '00002'}
B = {'01111', '11111', '21111', '11112', '11110'}
C = {'02222', '12222', '22222', '22221', '22220'}

union_of = A | B | C
print(3 ** 5 - len(union_of))

print(10**7)

X = {'01234',
'12345',
'23456',
'34567',
'45678',
'56789',
'67890'}

print(len(X))
