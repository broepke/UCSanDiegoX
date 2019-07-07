import numpy as np
from sklearn.metrics import mean_squared_error

# Consider the following simple data set of four points  (𝑥,𝑦) :
x = np.array([1, 1, 4, 4])
y = np.array([1, 3, 4, 6])


# a) Suppose you had to predict  𝑦  without knowledge of  𝑥 .
# What value would you predict?
print('a)', np.mean(y))

# b) Continuing from part (a), what is the  𝐦𝐞𝐚𝐧 𝐬𝐪𝐮𝐚𝐫𝐞𝐝 𝐞𝐫𝐫𝐨𝐫  (MSE)
# of your prediction, on the given four points?
# (This is the variance of the four observed values of  𝑦 .)
print('b)', np.var(y))

# c) Now let's say you want to predict  𝑦  based on  𝑥 .
# Your initial choice of prediction rule is  𝑦=𝑥 .
# What is the MSE of the linear function  𝑦=𝑥  on the four given points?
# (The MSE is obtained by computing the (squared) error on each
# of the four points and averaging them.)
mse = mean_squared_error(x, y)
print('c)', mse)

# d) Finally, you want to find the  𝐛𝐞𝐬𝐭  prediction rule of the
# form  𝑦=𝑎𝑥+𝑏 . That is, you want to find the parameters  𝑎,𝑏∈ℝ
# such that this rule has the smallest possible mean squared error
# on the four training points. What are  𝑎  and  𝑏 ?

best_a = np.cov(x, y, ddof=0)[1][0] / np.var(x)
print('best fit a', best_a)

best_b = np.mean(y) - (best_a * np.mean(x))
print('best fit b', best_b)


# e) Continuing from part (d), what is the MSE of this
# optimal linear predictor?
