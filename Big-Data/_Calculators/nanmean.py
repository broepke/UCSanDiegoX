import numpy as np

a = np.mean([1,2,np.nan]) # = 1.5
b = np.nanmean([1,2,np.nan]) # = 1.5
c = np.nanmean([1,2,np.nan]) # = 1


print(a,b,c)
