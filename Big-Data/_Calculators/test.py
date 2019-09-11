def find_slope(x):
    x1 = x[0][0]
    y1 = x[0][1]
    x2 = x[1][0]
    y2 = x[1][1]

    if x1 == x2:
        return (((x[0]), "inf"), (x[1]))
    else:
        slope = (y2 - y1) / (x2 - x1)
        return (((x[0]), slope), (x[1]))


a = [((4, 2), (2, 1)), ((4, 2), (-3, 4)), ((4, 2), (6, 3)), ((2, 1), (4, 2)), ((2, 1), (-3, 4)), ((2, 1), (6, 3)),
     ((-3, 4), (4, 2)), ((-3, 4), (2, 1)), ((-3, 4), (6, 3)), ((6, 3), (4, 2)), ((6, 3), (2, 1)), ((6, 3), (-3, 4))]

# new list of slopes
b = []
found = False

for i in a:
    # check to see if that slop already is in there, if so just append the points
    found = False
    s = find_slope(i)

    for j in b:
        if j[0][1] == s[0][1]:
            found = True
            j[1].add(s[1])

    if not found:
        x = (s[0], {tuple(s[1])})
        b.append(x)

c = []
for y in b:
    d = (y[0], list(y[1]))
    c.append(d)

print(c)
