import numpy as np
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt

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

print('\n', 'iterating lists method')
print(confusion)

# here is how you can accomplish the same thing as above with np.add.at
c = np.zeros((3, 3), dtype=int)
np.add.at(c, (x, y), 1)

print('\n', 'using the np.add.at method')
print(c)


d = confusion_matrix(x, y)

print('\n', 'using the confusion matrix from scikit-learn')
print(d)


y_actu = pd.Series(x, name='Actual')
y_pred = pd.Series(y, name='Predicted')
df_confusion = pd.crosstab(y_actu, y_pred)

print('\n', 'using pandas crostab')
print(df_confusion)


def plot_confusion_matrix(df_confusion, title='Confusion matrix', cmap=plt.cm.gray_r):
    plt.matshow(df_confusion, cmap=cmap) # imshow
    #plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(df_confusion.columns))
    plt.xticks(tick_marks, df_confusion.columns, rotation=45)
    plt.yticks(tick_marks, df_confusion.index)
    #plt.tight_layout()
    plt.ylabel(df_confusion.index.name)
    plt.xlabel(df_confusion.columns.name)

plot_confusion_matrix(df_confusion)
plt.show()
