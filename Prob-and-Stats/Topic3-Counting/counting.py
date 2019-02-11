target = 2016
counter = 0

for i in range(1,target+1):
    if target % i == 0:
        counter += 1
        print(i)

print('Total numbers divible by ' + str(target) + ' = ' + str(counter))