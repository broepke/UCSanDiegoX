import numpy as np
import matplotlib.pyplot as plt
M = np.array([[1,1],[-2,2],[4,-7]])


rows,cols = M.T.shape

#Get absolute maxes for axis ranges to center origin
#This is optional
maxes = 1.1*np.amax(abs(M), axis = 0)
colors = ['b','r','k']


for i,l in enumerate(range(0,cols)):
    plt.axes().arrow(0,0,M[i,0],M[i,1],head_width=0.2,head_length=0.2,color = colors[i])

plt.plot(0,0,'ok') #<-- plot a black point at the origin
# plt.axis('equal')  #<-- set the axes to the same scale
plt.xlim([-maxes[0],maxes[0]]) #<-- set the x axis limits
plt.ylim([-maxes[1],maxes[1]]) #<-- set the y axis limits
plt.grid(b=True, which='major') #<-- plot grid lines
plt.show()
