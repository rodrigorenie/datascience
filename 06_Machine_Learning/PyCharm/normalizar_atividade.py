import sklearn
import pandas as pd
import numpy as np
import sklearn.preprocessing

housing = pd.read_csv('dados/housing.data.csv', sep=',')
vote = pd.read_csv('dados/vote.csv')

normalizer = sklearn.preprocessing.MinMaxScaler()
housing_normal = normalizer.fit_transform(housing)
housing_normal = pd.DataFrame(housing_normal, columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
                                                       'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'])

vote_normal = pd.get_dummies(vote)
print(vote)
print(vote_normal)

housing_normal.to_csv('dados/housing.data.normal.csv', index=False)
