import numpy as np

x = [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0]
y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

testy = np.array(x)
testy_fit = np.array(y)

row_no = [0, 0, 0]
row_dh = [0, 0, 0]
row_sl = [0, 0, 0]

# Code for the first row - NO
for i in range(len(testy)):
    if testy.item(i) == 0 and testy_fit.item(i) == 0:
        row_no[0] += 1
    elif testy.item(i) == 0 and testy_fit.item(i) == 1:
        row_no[1] += 1
    elif testy.item(i) == 0 and testy_fit.item(i) == 2:
        row_no[2] += 1

# Code for the second row - DH
for i in range(len(testy)):
    if testy.item(i) == 1 and testy_fit.item(i) == 0:
        row_dh[0] += 1
    elif testy.item(i) == 1 and testy_fit.item(i) == 1:
        row_dh[1] += 1
    elif testy.item(i) == 1 and testy_fit.item(i) == 2:
        row_dh[2] += 1

# Code for the third row - SL
for i in range(len(testy)):
    if testy.item(i) == 2 and testy_fit.item(i) == 0:
        row_sl[0] += 1
    elif testy.item(i) == 2 and testy_fit.item(i) == 1:
        row_sl[1] += 1
    elif testy.item(i) == 2 and testy_fit.item(i) == 2:
        row_sl[2] += 1

confusion = np.array([row_no, row_dh, row_sl])

# print(confusion)

# here is how you can accomplish the same thing as above with np.add.at
c = np.zeros((3, 3), dtype=int)

np.add.at(c, (x, y), 1)

print(c)
