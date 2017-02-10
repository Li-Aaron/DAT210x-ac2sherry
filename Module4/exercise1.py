import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv("Datasets/wheat.data", index_col=0)

pca = PCA(n_components=2)

df1 = df.drop(['wheat_type'],axis = 1)
df2 = df1.dropna()
pca.fit(df2)
PCA(copy=True, n_components=2, whiten=False)

T = pca.transform(df2)

print(df2.shape) # 430 Student survey responses, 6 questions..

print(T.shape) # 430 Student survey responses, 2 principal components..