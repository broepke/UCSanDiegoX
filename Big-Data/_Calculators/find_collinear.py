
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


def to_tuple(x):
    y = x.split()
    z = tuple(map(lambda x: int(x), y))

    return z

def format_result(x):
    x[1].append(x[0][0])
    return tuple(x[1])


def to_sorted_points(x):
    """
    Sorts and returns a tuple of points for further processing.
    """
    return tuple(sorted(x))


# List all pairs of points. You can do that efficiently in spark by computing cartesian product of
# the list of points with itself. For example, given three points  [(1,0),(2,0),(3,0)]
# Remove the pairs in which the same point appears twice
# This is the output of the function already written

'''
a = [((4, 2), (2, 1)), ((4, 2), (-3, 4)), ((4, 2), (6, 3)), ((2, 1), (4, 2)), ((2, 1), (-3, 4)), ((2, 1), (6, 3)),
     ((-3, 4), (4, 2)), ((-3, 4), (2, 1)), ((-3, 4), (6, 3)), ((6, 3), (4, 2)), ((6, 3), (2, 1)), ((6, 3), (-3, 4))]

a = [((4, -2), (2, -1)),
     ((2, -1), (4, -2)),
     ((4, -2), (-3, 4)),
     ((4, -2), (6, 3)),
     ((2, -1), (-3, 4)),
     ((2, -1), (6, 3)),
     ((4, -2), (-9, 4)),
     ((4, -2), (6, -3)),
     ((2, -1), (-9, 4)),
     ((2, -1), (6, -3)),
     ((4, -2), (8, -4)),
     ((4, -2), (6, 9)),
     ((2, -1), (8, -4)),
     ((2, -1), (6, 9)),
     ((-3, 4), (4, -2)),
     ((-3, 4), (2, -1)),
     ((6, 3), (4, -2)),
     ((6, 3), (2, -1)),
     ((-3, 4), (6, 3)),
     ((6, 3), (-3, 4)),
     ((-3, 4), (-9, 4)),
     ((-3, 4), (6, -3)),
     ((6, 3), (-9, 4)),
     ((6, 3), (6, -3)),
     ((-3, 4), (8, -4)),
     ((-3, 4), (6, 9)),
     ((6, 3), (8, -4)),
     ((6, 3), (6, 9)),
     ((-9, 4), (4, -2)),
     ((-9, 4), (2, -1)),
     ((6, -3), (4, -2)),
     ((6, -3), (2, -1)),
     ((-9, 4), (-3, 4)),
     ((-9, 4), (6, 3)),
     ((6, -3), (-3, 4)),
     ((6, -3), (6, 3)),
     ((-9, 4), (6, -3)),
     ((6, -3), (-9, 4)),
     ((-9, 4), (8, -4)),
     ((-9, 4), (6, 9)),
     ((6, -3), (8, -4)),
     ((6, -3), (6, 9)),
     ((8, -4), (4, -2)),
     ((8, -4), (2, -1)),
     ((6, 9), (4, -2)),
     ((6, 9), (2, -1)),
     ((8, -4), (-3, 4)),
     ((8, -4), (6, 3)),
     ((6, 9), (-3, 4)),
     ((6, 9), (6, 3)),
     ((8, -4), (-9, 4)),
     ((8, -4), (6, -3)),
     ((6, 9), (-9, 4)),
     ((6, 9), (6, -3)),
     ((8, -4), (6, 9)),
     ((6, 9), (8, -4))]


'''
a = [((1, 1), (0, 1)),
     ((0, 1), (1, 1)),
     ((1, 1), (2, 2)),
     ((1, 1), (3, 3)),
     ((0, 1), (2, 2)),
     ((0, 1), (3, 3)),
     ((1, 1), (0, 5)),
     ((1, 1), (3, 4)),
     ((0, 1), (0, 5)),
     ((0, 1), (3, 4)),
     ((1, 1), (5, 6)),
     ((1, 1), (0, -3)),
     ((0, 1), (5, 6)),
     ((0, 1), (0, -3)),
     ((1, 1), (-2, -2)),
     ((0, 1), (-2, -2)),
     ((2, 2), (1, 1)),
     ((2, 2), (0, 1)),
     ((3, 3), (1, 1)),
     ((3, 3), (0, 1)),
     ((2, 2), (3, 3)),
     ((3, 3), (2, 2)),
     ((2, 2), (0, 5)),
     ((2, 2), (3, 4)),
     ((3, 3), (0, 5)),
     ((3, 3), (3, 4)),
     ((2, 2), (5, 6)),
     ((2, 2), (0, -3)),
     ((3, 3), (5, 6)),
     ((3, 3), (0, -3)),
     ((2, 2), (-2, -2)),
     ((3, 3), (-2, -2)),
     ((0, 5), (1, 1)),
     ((0, 5), (0, 1)),
     ((3, 4), (1, 1)),
     ((3, 4), (0, 1)),
     ((0, 5), (2, 2)),
     ((0, 5), (3, 3)),
     ((3, 4), (2, 2)),
     ((3, 4), (3, 3)),
     ((0, 5), (3, 4)),
     ((3, 4), (0, 5)),
     ((0, 5), (5, 6)),
     ((0, 5), (0, -3)),
     ((3, 4), (5, 6)),
     ((3, 4), (0, -3)),
     ((0, 5), (-2, -2)),
     ((3, 4), (-2, -2)),
     ((5, 6), (1, 1)),
     ((5, 6), (0, 1)),
     ((0, -3), (1, 1)),
     ((0, -3), (0, 1)),
     ((-2, -2), (1, 1)),
     ((-2, -2), (0, 1)),
     ((5, 6), (2, 2)),
     ((5, 6), (3, 3)),
     ((0, -3), (2, 2)),
     ((0, -3), (3, 3)),
     ((-2, -2), (2, 2)),
     ((-2, -2), (3, 3)),
     ((5, 6), (0, 5)),
     ((5, 6), (3, 4)),
     ((0, -3), (0, 5)),
     ((0, -3), (3, 4)),
     ((-2, -2), (0, 5)),
     ((-2, -2), (3, 4)),
     ((5, 6), (0, -3)),
     ((0, -3), (5, 6)),
     ((5, 6), (-2, -2)),
     ((0, -3), (-2, -2)),
     ((-2, -2), (5, 6)),
     ((-2, -2), (0, -3))]


# For each pair of points, find the parametrization (slope)
# Group the pairs according to their parameters. Clearly, if two pairs have the same a,b values same line


pairs_dict = {}
for i in a:
    # find the parametrization of a line
    axb = 0
    q = find_slope(i)
    y = float(i[0][1])
    x = float(i[0][0])
    m = q[0][1]
    if m == -0.0:
        axb = round(y - (0 * x), 5)
        axb = str(axb) + '&' + str(0.0)
    elif m != "inf":
        axb = round(y - (m * x),5)
        m = round(m,5)
        axb = str(axb) + '&' + str(m)
    else:
        axb = 'inf'

    try:
        if pairs_dict[axb]:
            pairs_dict[axb].append(q[0][0])
    except:
        pairs_dict[axb] = []
        pairs_dict[axb].append(q[1])

# Eliminate the groups that contain only one pair
final_list = []

for key, value in pairs_dict.items():
    if len([item for item in value if item]) > 2 and key != 'inf':
        final_list.append(value)

# Finally check for an vertical lines with 3 or more from the "inf"
vert_set = set()
vert_dict = {}
try:
    if pairs_dict['inf']:

        for value in pairs_dict['inf']:
            vert_set.add(value)

        for vert in vert_set:
            try:
                if vert_dict[vert[0]]:
                    vert_dict[vert[0]].append(vert)
            except:
                vert_dict[vert[0]] = []
                vert_dict[vert[0]].append(vert)

        for key, value in vert_dict.items():
            if len([item for item in value if item]) > 2:
                final_list.append(value)
except:
    pass

dedupe = []
for x in final_list:
    x_set = set(x)
    x_set = tuple(x_set)
    x_set = to_sorted_points(x_set)
    dedupe.append(x_set)

dedupe = sorted(dedupe)
print(set(dedupe))
