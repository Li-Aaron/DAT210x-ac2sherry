import pandas as pd
import numpy as np

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

import pylab as pl

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = np.linspace(0,355,72)


#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
for sam in samples:
    img = misc.imread('Datasets/ALOI/32/32_r'+str(int(sam))+'.png')
    img = img[::2, ::2]
    X = (img / 255.0).reshape(-1)
    X.shape = (len(X),1)
    Y = np.transpose(X)
    if sam == 0: 
        A = Y
    else:
        A = np.append(A, Y, axis = 0)

pl.imshow(img, cmap=plt.cm.gray)
#pl.imshow(X, cmap=plt.cm.gray)
df = pd.DataFrame(A)

from sklearn import manifold
iso = manifold.Isomap(n_neighbors=2, n_components=3)
iso.fit(df)
T_ISO = iso.transform(df)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('ISO 2D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.scatter(T_ISO[:,0],T_ISO[:,1], c='blue', marker='.', alpha=0.75)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('ISO 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(T_ISO[:,0],T_ISO[:,1],T_ISO[:,2], c='blue', marker='.', alpha=0.75)

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
samples2 = np.linspace(110,220,12)
for sam in samples2:
    img = misc.imread('Datasets/ALOI/32i/32_i'+str(int(sam))+'.png')
    img = img[::2, ::2]
    X = (img / 255.0).reshape(-1)
    X.shape = (len(X),1)
    Y = np.transpose(X)
    if sam == 110: 
        B = Y
    else:
        B = np.append(B, Y, axis = 0)

#
# TODO: Convert the list to a dataframe
#
# .. your code here ..
C = np.append(A, B, axis = 0) 
df2 = pd.DataFrame(C)

colors = ['b']*72 +['r']*12


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 

iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df2)
T_ISO = iso.transform(df2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('ISO 2D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.scatter(T_ISO[:,0],T_ISO[:,1], c=colors, marker='.', alpha=0.75)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('ISO 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(T_ISO[:,0],T_ISO[:,1],T_ISO[:,2], c=colors, marker='.', alpha=0.75)


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 




#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()

