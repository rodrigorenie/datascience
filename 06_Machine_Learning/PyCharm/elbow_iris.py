import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # sklearn pacote com algoritmos de aprendizado de maquinas
from sklearn import metrics
from scipy.spatial.distance import euclidean, cdist

# carrega dados para objeto
iris = pd.read_csv('dados/iris.csv')

# dados para plotagem
x0 = iris.iloc[:,0]
x1 = iris.iloc[:,1]
x2 = iris.iloc[:,2]
x3 = iris.iloc[:,3]
x4 = iris.iloc[:,4]

# isola classe
iris.y = iris.iloc[:,4]

# isola colunas independentes
iris.x = iris.drop(columns=['class'], axis=1)


fig, ax = plt.subplots()
# agrupar os objs em uma lista
X = np.array(list(zip(x0, x1, x2, x3))).reshape((len(x0), 4))


distorcoes = []
cluster = KMeans(n_clusters=3).fit(X)

K = range(1, 11)
for k in K:
    kmeansModel = KMeans(n_clusters=k).fit(X)
    value = cdist(X, kmeansModel.cluster_centers_, 'euclidean')
    value = np.min(value, axis=1)
    value = sum(value)
    value = value / X.shape[0]
    distorcoes.append(value)

ax.plot(K, distorcoes)
ax.set(xlabel='clusters', ylabel='distorcao', title='metodo elbow')
plt.savefig('plot_distorcao')

inercias = []
for k in K:
    kmeansModel = KMeans(n_clusters=k).fit(X)
    inercias.append(kmeansModel.inertia_)

fig, ax = plt.subplots()

ax.plot(K, inercias)
ax.set(xlabel='clusters', ylabel='inercia', title='metodo elbow')
plt.savefig('plot_inercia')


labels = KMeans(n_clusters=4).fit_predict(X)
cluster_labels_df = pd.DataFrame(labels, columns=['Cluster_Label'])
dados = pd.DataFrame(X, columns=['x1', 'x2', 'x3', 'x4'])

print(pd.merge(cluster_labels_df, dados, left_on=['Cluster_Label'], right_on=['x1', 'x2', 'x3', 'x4']))