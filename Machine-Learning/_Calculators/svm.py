import numpy as np

# A linear classifier on  ℝ2  is specified by  𝑤=(−1,3)  and  𝑏=−6 .
# What label,  1  or  −1 , is assigned to the point  (1,1) ?

w = np.array([.5,.5])
x = np.array([4,5])
b = -3.5

y  = w.dot(x) + b
print('w.x + b =', y)

# Test the classifier quickyly
if y > 0:
    print('Classify', x , 'as 1')
elif y < 0:
    print('Classify', x , 'as -1')
else:
    print('Classify as "Correct" or 0')


# Calculate 1/||w|| or the margin for the support vector
print('Margin for Support vector =', 1/np.linalg.norm(w, ord=2),'\n')
