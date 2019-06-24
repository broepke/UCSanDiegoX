from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
import numpy as np

X, Y = load_digits(return_X_y=True)
clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(X, Y)

print(clf.score(X, Y))

print(X.shape)
print(X.ndim)
