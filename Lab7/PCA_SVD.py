"""PCA and SVD dimensionality reduction."""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X=load_iris().data
X=StandardScaler().fit_transform(X)
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X)
print("Original shape:",X.shape)
print("PCA shape:",X_pca.shape)
print("Explained variance ratio:",pca.explained_variance_ratio_)

U,S,Vt=np.linalg.svd(X,full_matrices=False)
X_svd=U[:,:2] @ np.diag(S[:2])
print("SVD reduced shape:",X_svd.shape)
