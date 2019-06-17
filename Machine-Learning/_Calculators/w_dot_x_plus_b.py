import numpy as np

'''
A linear classifier on  ℝ2  is specified by  𝑤=(−1,3)  and  𝑏=−6 .
What label,  1  or  −1 , is assigned to the point  (1,1) ?
'''

w = np.array([-3,1])
x = np.array([1,1])
b = -6

print(x.dot(x)+b)
