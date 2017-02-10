import pandas as pd
import matplotlib.pyplot as plt

X = pd.read_csv("Datasets/parkinsons.data")
X = X.drop(['name'], axis = 1)
y = X['status']
X = X.drop(['status'], axis = 1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)


# Q1
from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train, y_train)
score = svc.score(X_test, y_test)
print ("====== Q1 results ======")
print ("Score: ", score)


# Q2
import numpy as np
best_score = 0.0
best_C = 0
best_gamma = 0
for C in np.arange(0.05, 2, 0.05):
  for gamma in np.arange(0.001, 0.1, 0.001):
    svc = SVC(kernel = 'rbf', C = C, gamma = gamma)
    svc.fit(X_train, y_train)
    score = svc.score(X_test, y_test)
    if (best_score < score):
      best_score = score
      best_C = C
      best_gamma = gamma

print ("====== Q2 results ======")
print ("Best Score: ", best_score)
print ("Best C: ", best_C)
print ("Best Gamma: ", best_gamma)


# Q3
best_score = 0.0
preprocessors = []
X_trains = []
X_tests = []
from sklearn import preprocessing
preprocessors.append(preprocessing.Normalizer())
preprocessors.append(preprocessing.MaxAbsScaler())
preprocessors.append(preprocessing.MinMaxScaler())
preprocessors.append(preprocessing.KernelCenterer())
preprocessors.append(preprocessing.StandardScaler())
for i in range(0, 5):
  # Preprocessing fit and transform
  preprocessors[i].fit(X_train)
  X_trains.append(preprocessors[i].transform(X_train))
  X_tests.append(preprocessors[i].transform(X_test))
  # SVC fit and score
  for C in np.arange(0.05, 2, 0.05):
    for gamma in np.arange(0.001, 0.1, 0.001):
      svc = SVC(kernel = 'rbf', C = C, gamma = gamma)
      svc.fit(X_trains[i], y_train)
      score = svc.score(X_tests[i], y_test)
      if (best_score < score):
        best_score = score
        best_C = C
        best_gamma = gamma
        best_func = i

print ("====== Q3 results ======")
print ("Best Score: ", best_score)
print ("Best C: ", best_C)
print ("Best Gamma: ", best_gamma)   
print ("Best Func: ", preprocessors[best_func])


# Q4
from sklearn.decomposition import PCA

best_score = 0.0

for i in range(0, 5):
  # Preprocessing fit and transform (No Need Transform Again)
  # preprocessors[i].fit(X_train)
  # X_trains.append(preprocessors[i].transform(X_train))
  # X_tests.append(preprocessors[i].transform(X_test))
  
  # PCA fit and score
  for n_components in range(4, 15): # 4 to 14
    pca = PCA(n_components = n_components)
    pca.fit(X_trains[i])
    X_trains_pca = pca.transform(X_trains[i])
    X_tests_pca = pca.transform(X_tests[i])

    # SVC fit and score
    for C in np.arange(0.05, 2, 0.05):
      for gamma in np.arange(0.001, 0.1, 0.001):
        svc = SVC(kernel = 'rbf', C = C, gamma = gamma)
        svc.fit(X_trains_pca, y_train)
        score = svc.score(X_tests_pca, y_test)
        if (best_score < score):
          best_score = score
          best_C = C
          best_gamma = gamma
          best_func = i
          best_pca = n_components

print ("====== Q4 PCA results ======")
print ("Best Score: ", best_score)
print ("Best C: ", best_C)
print ("Best Gamma: ", best_gamma)   
print ("Best Func: ", preprocessors[best_func])
print ("Best n_components: ", best_pca)       



from sklearn.manifold import Isomap

best_score = 0.0

for i in range(0, 5):
  # Preprocessing fit and transform (No Need Transform Again)
  # preprocessors[i].fit(X_train)
  # X_trains.append(preprocessors[i].transform(X_train))
  # X_tests.append(preprocessors[i].transform(X_test))
  
  # Isomap fit and score
  for n_neighbors in range(2, 6): #2 to 5
    for n_components in range(4, 7): # 4 to 6
      iso = Isomap(n_neighbors = n_neighbors, n_components = n_components)
      iso.fit(X_trains[i])
      X_trains_iso = iso.transform(X_trains[i])
      X_tests_iso = iso.transform(X_tests[i])

      # SVC fit and score
      for C in np.arange(0.05, 2, 0.05):
        for gamma in np.arange(0.001, 0.1, 0.001):
          svc = SVC(kernel = 'rbf', C = C, gamma = gamma)
          svc.fit(X_trains_iso, y_train)
          score = svc.score(X_tests_iso, y_test)
          if (best_score < score):
            best_score = score
            best_C = C
            best_gamma = gamma
            best_func = i
            best_iso = [n_neighbors, n_components]

print ("====== Q4 ISO results ======")
print ("Best Score: ", best_score)
print ("Best C: ", best_C)
print ("Best Gamma: ", best_gamma)   
print ("Best Func: ", preprocessors[best_func])
print ("Best [n_components, n_components]: ", best_iso)       