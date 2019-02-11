target = 2016
counter = 0

for i in range(target):
    try:
        if target % i == 0:
            counter += 1
    except:
        counter =+ 1

print(counter)