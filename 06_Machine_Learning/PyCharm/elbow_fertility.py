import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # sklearn pacote com algoritmos de aprendizado de maquinas
from sklearn import metrics
from scipy.spatial.distance import euclidean, cdist

fertility = pd.read_csv('dados/fertility_diagnosis.txt')

# dados para plotagem
x0 = fertility.iloc[:,0]
x1 = fertility.iloc[:,1]
x2 = fertility.iloc[:,2]
x3 = fertility.iloc[:,3]
x4 = fertility.iloc[:,4]
x5 = fertility.iloc[:,5]
x6 = fertility.iloc[:,6]
x7 = fertility.iloc[:,7]
x8 = fertility.iloc[:,8]
x9 = fertility.iloc[:,9]


# isola classe
fertility.y = fertility.iloc[:,9]

# isola colunas independentes
fertility.x = fertility.drop(columns=['Output'], axis=1)

fig, ax = plt.subplots()
# agrupar os objs em uma lista
X = np.array(list(zip(x0, x1, x2, x3, x4, x5, x6, x7, x8))).reshape((len(x0), 9))
print(X)


distorcoes = []
cluster = KMeans(n_clusters=3).fit(X)
print(cluster.cluster_centers_)

K = range(1, 101)
for k in K:
    kmeansModel = KMeans(n_clusters=k).fit(X)
    value = cdist(X, kmeansModel.cluster_centers_, 'euclidean')
    value = np.min(value, axis=1)
    value = sum(value)
    value = value / X.shape[0]
    distorcoes.append(value)

print(distorcoes)

ax.plot(K, distorcoes)
ax.set(xlabel='clusters', ylabel='distorcao', title='metodo elbow')
plt.savefig('plot_fertility_distorcao')

inercias = []
for k in K:
    kmeansModel = KMeans(n_clusters=k).fit(X)
    inercias.append(kmeansModel.inertia_)

fig, ax = plt.subplots()

ax.plot(K, inercias)
ax.set(xlabel='clusters', ylabel='inercia', title='metodo elbow')
plt.savefig('plot_fertility_inercia')