# https://book.pythontips.com/en/latest/map_filter.html

from functools import reduce

# Most of the times we want to pass all the list elements to a function
# one-by-one and then collect the output. For instance:

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)

# Map allows us to implement this in a much simpler and nicer way. Here you go:

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))

print('Lambda ', squared)


# Most of the times we use lambdas with map so I did the same. Instead of a list of
# inputs we can even have a list of functions!

def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# As the name suggests, filter creates a list of elements for which a function returns true.
# Here is a short and concise example:

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# The filter resembles a for loop but it is a builtin function and faster.

# Note: If map & filter do not appear beautiful to you then you can
# read about list/dict/tuple comprehensions.

# Reduce is a really useful function for performing some computation on a list and returning the result.
# It applies a rolling computation to sequential pairs of values in a list. For example,
# if you wanted to compute the product of a list of integers.

# So the normal way you might go about doing this task in python is using a basic for loop:

product = 1
a_list = [1, 2, 3, 4]
for num in a_list:
    product = product * num

# Now let’s try it with reduce:

prod = reduce((lambda x, y: x * y), a_list)

print('Reduce by Product ', prod)

a_sum = reduce((lambda x, y: x + y), a_list)

print('Reduce by Sum ', a_sum)
