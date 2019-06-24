import numpy as np

# A linear classifier on  ℝ2  is specified by  𝑤=(−1,3)  and  𝑏=−6 .
# What label,  1  or  −1 , is assigned to the point  (1,1) ?

w = np.array([1, 1, -3, 0])
x = np.array([3, 1, 1, 4])
b = -2
y = 1

y  = w.dot(x) + b
print('w.x + b =', y)

# Test the classifier quickyly
if y > 0:
    print('Classify as 1')
elif y < 0:
    print('Classify as -1')
else:
    print('Classify as "Correct" or 0')

# Calculate the loss when the result is less than 0
if y <= 0:
    loss = -y
    print('The loss of the function is =', loss)
else:
    print('There was no loss')
