#exercício prático de R

## Liste o direório corrente

## Liste os arquivos do diretorio

## Pesquise uma função para criar um diretório

## pesquise o manual para essa funçao

## Crie um diretório com o nome "exercicioR"

## Entre no diretório criado

## crie uma função que multiplique dois valores

## crie uma funcçao que subtraia dois valores

## crie uma funcao que eleve um valor ao quadrado

## pesquise uma função que copie os arquivos e consulte a sua utilização

## copie o arquivo carros.csv da area de trabalho para a pasta.

#Objetivo: fazer a regressão linear de mpg em relaçao a hp
#Há relaçao entre as variáveis?
## qual o sentido?

## carregue o arquivo para um data frame

## veja o resumo do data frame

## os dados OK?

#por que?

#se não estiver ok, remova os dados inconsistentes do data frame

#plote os gráficos de dispersão e os histogramas das variáveis hp e mpg

#calcule a media da coluna mpg e atribua a uma variável mean_y

#calcule a media da coluna hp e atribua a uma variável mean_x

#crie um vetor com a diferenca entre o valor e sua média (xi - mean_x) utilizando a funcao de diferenca criada

#crie um vetor com a diferenca entre o valor e sua média (yi - mean_y) utilizando a funcao de diferenca criada

#crie um vetor com o quadrado da diferenca de x criado utilizando a funcao de quadrado criada

#crie um vetor com o produto das diferenca de x e y criado utilizando a funcao de subtração criada

#concatene os vetores criados com o data frame

## agora calcule os coeficientes b e a para a reta de regressão com os vetores calculados
#b <- sum_prod_dif_xy/sum_dif_x2
#a <- y_bar- b*x_bar

## Com os coeficientes criados crie uma função que estime o valor de mpg dado um valor de hp
## y = a + bx

## crie um vetor com os valores preditos f(x) os valores de hp

## concatene os valores preditos no data frame

## calcule os as variaçoes explicada, nao explicada e total

## Calcule o coeficiente de Determinação

## Calcule a Covariancia

## Calcule a Correlação

## Plote a curva no gráfico de dispersao. Dica: utilize a funcao curve( add = TRUE)

## Plote um histograma com os RESÍDUOS não explicados

## Escreva sobre o que encontrou e seus resultados obtidos

## salve o data frame como csv com o nome resultado_carros.csv

## salve a funcao de regressao para o arquivo linear_carros.R

## salve o script dentro da pasta.
