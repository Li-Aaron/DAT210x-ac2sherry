import pandas as pd
import matplotlib.pyplot as plt

from sklearn import manifold
df = pd.read_csv("Datasets/wheat.data", index_col=0)
df = df.drop(['wheat_type'],axis = 1)
df = df.dropna(axis = 0, how = "any")
iso = manifold.Isomap(n_neighbors=4, n_components=2)
print(iso.fit(df))
manifold_iso = iso.transform(df)
print(df.shape)
print(manifold_iso.shape)

T = pd.DataFrame(manifold_iso)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', alpha=0.75)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(T.component1, T.component2, c='black', marker='o', alpha=0.75)

plt.show()