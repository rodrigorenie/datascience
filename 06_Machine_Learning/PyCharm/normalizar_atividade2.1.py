
import pandas as pd
import sklearn.preprocessing
import pickle

housing = pd.read_csv('dados/housing.data.csv', sep=',')
normalizer = sklearn.preprocessing.MinMaxScaler()
housing_normal = normalizer.fit(housing)

with open('dados/minmax_normalizer.pkl', 'wb') as f:
    pickle.dump(normalizer, f)