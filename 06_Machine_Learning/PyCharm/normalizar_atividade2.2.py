
import pandas as pd
import sklearn.preprocessing
import pickle

housing_novos = pd.read_csv('dados/housing.data.novos.csv')

with open('dados/minmax_normalizer.pkl', 'rb') as f:
    normalizer = pickle.load(f)

housing_novos_normal = normalizer.transform(housing_novos)
housing_novos_normal = pd.DataFrame(housing_novos_normal, columns=housing_novos.columns)
print(housing_novos_normal)
