import numpy as np
from sklearn.decomposition import PCA


X = np.array([[5, 3, 0], [-3, 5, 0], [0, 0, 4]])


pca = PCA(n_components=2)
pca.fit(X)

print(pca.explained_variance_ratio_)
print(pca.singular_values_)
print(pca.components_)
