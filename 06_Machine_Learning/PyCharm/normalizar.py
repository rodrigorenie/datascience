import sklearn
import pandas as pd
import numpy as np
import sklearn.preprocessing

# import time
# initial_time = time.time()
# i = [i for i in range(100000000)]
# for value in i:
#     print(value)
#     if value >= 10:
#         break
# print('took:', initial_time - time.time())
# exit()

dados = pd.read_csv('dados/dados_normalizar.csv', sep=';')

# Carregar dados puramente numéricos
dados_num = dados.drop(columns=['sexo'])
dados_categorias = dados['sexo']

# Normalizar usando min/max
# z = (x - min(dados))/(max(dados) - min(dados))
# dados_normalizados = (dados_num - dados_num.min())/(dados_num.max() - dados_num.min())

# Normalizar usando média
# dados_normalizados = (dados_num - dados_num.mean())/dados_num.std()

# Normalizar usando MinMaxScaler
normalizador = sklearn.preprocessing.MinMaxScaler()
dados_normalizados = normalizador.fit_transform(dados_num)

# Normalizar dados categóricos
categorias_normalizados = pd.get_dummies(dados_categorias, prefix='Sexo')

dados_finais = pd.DataFrame(dados_normalizados, columns=['Idade', 'Altura', 'Peso'])
dados_finais = dados_finais.join(categorias_normalizados)
dados_finais.to_csv('dados/dados_normalizados.csv', index=False, sep=';')
print(dados_finais)

