import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from sklearn.cluster import KMeans # sklearn pacote com algoritmos de aprendizado de maquinas
from sklearn import metrics
from scipy.spatial.distance import euclidean, cdist


def optimal_number_of_clusters(wcss):
    x1, y1 = 2, wcss[0]
    x2, y2 = len(wcss), wcss[-1]
    distances = []

    for i in range(len(wcss)):
        x0 = i + 2
        y0 = wcss[i]
        numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
        denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        distances.append(numerator/denominator)

    return distances.index(max(distances)) + 2


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

fig, ax = plt.subplots()
# agrupar os objs em uma lista
X = np.array(list(zip(x0, x1, x2, x3, x4, x5, x6, x7, x8))).reshape((len(x0), 9))

distorcoes = []
cluster = KMeans(n_clusters=3).fit(X)

K = range(1, 101)
for k in K:
    kmeansModel = KMeans(n_clusters=k).fit(X)
    value = cdist(X, kmeansModel.cluster_centers_, 'euclidean')
    value = np.min(value, axis=1)
    value = sum(value)
    value = value / X.shape[0]
    distorcoes.append(value)

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

ki = optimal_number_of_clusters(inercias)
kd = optimal_number_of_clusters(distorcoes)

print('numero de cluster baseado na inercia:', ki)
print('numero de cluster baseado na distorcao:', kd)

