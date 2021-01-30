## exercíio prático de R
## Aluno: Rodrigo Renie de Braga Pinto

require(rstudioapi)

#
# Define a diretório corrente para o mesmo ao da localização do arquivo 
# atualmente aberto no RStudio
#
setwd_curfile <- function() {
  installed_packages <- rownames(installed.packages())
  
  if (!is.element('rstudioapi', installed_packages)) {
    install.packages('rstudioapi')
  }
  
  library('rstudioapi')
  path <- getActiveDocumentContext()$path
  dir <- dirname(path)
  message(paste("Setting CWD to '", dir, "'", sep=''))
  setwd(dir)
}


## Liste o diretório corrente
setwd_curfile()
getwd()


## Liste os arquivos do diretório
dir()


## Pesquise uma função para criar um diretório
apropos('dir')


## pesquise o manual para essa função
help('dir.create')
help(dir.create)


## Crie um diretório com o nome "exercicioR"
if (!dir.exists('exercicioR')) {
  dir.create('exercicioR', mode='0755')
}


## Entre no diretório criado
exercicio_path <- paste(getwd(), .Platform$file.sep, 'exercicioR', sep='')
setwd(exercicio_path)
dir()


## crie uma função que multiplique dois valores
multiply <- function(x, y) {
  tryCatch(
    {
      return(x*y)
    },
    error = function(cond) {
      return(NA)
    }
  )
}

multiply(8.1)
multiply(8.1, '3')
multiply(8.1, 3)


## crie uma função que subtraia dois valores
subtract <- function(x, y) {
  tryCatch(
    {
      return(x-y)
    },
    error = function(cond) {
      return(NA)
    }
  )
}

subtract(-9.1)
subtract(-9.1, '-9.1')
subtract(c(-9.1, 1), c(-9.1, -2, 3))
subtract(c(-9.1, 1), c(-9.1, -2))


## crie uma função que eleve um valor ao quadrado
powerof2 <- function(x) {
  tryCatch(
    {
      return(x^2)
    },
    error = function(cond) {
      return(NA)
    }
  )
}

powerof2()
powerof2('-7.333')
powerof2(-7.333)
powerof2(c(-7.333, 1, 0, 1))


## pesquise uma função que copie os arquivos e consulte a sua utilização
apropos('file')
help(file.copy)


## copie o arquivo carros.csv da area de trabalho para a pasta
getwd()
file.copy("~/Desktop/carros.csv", getwd(), overwrite = T)
file.remove("~/Desktop/carros.csv")


## Objetivo: fazer a regress?o linear de mpg em rela??o a hp
## Há relação entre as variáveis?
## qual o sentido?


## carregue o arquivo para um data frame
cars <- read.csv2(file="carros.csv")


## veja o resumo do data frame
summary(cars)


## os dados estão OK?
# Não


## Por que?
# Existem 3 carros que não possuem o valor de MPG


## Se não estiver ok, remova os dados inconsistentes do data frame
cars <- cars[!is.na(cars$mpg),]
# cars <- na.omit(cars)
summary(cars)


## Plote os gráficos de dispersão e os histogramas das variáeis hp e mpg
plot(x = cars$hp, y = cars$mpg, type = 'p', 
     main = "Horse Power influence on car consumption",
     xlab = "Horse Power",
     ylab = "Miles per Gallon")


## Calcule a media da coluna mpg e atribua a uma variável mean_y
y_bar <- mean(cars$mpg)
y_bar


## calcule a media da coluna hp e atribua a uma variável mean_x
x_bar = mean(cars$hp)
x_bar


## crie um vetor com a diferença entre o valor e sua média (xi - mean_x) 
## utilizando a função de diferença criada
x_sub_x_bar <- c(subtract(cars$hp, x_bar))
x_sub_x_bar


## crie um vetor com a diferença entre o valor e sua média (yi - mean_y) 
## utilizando a funcao de diferença criada
y_sub_y_bar <- c(subtract(cars$mpg, y_bar))
y_sub_y_bar


## crie um vetor com o quadrado da diferença de x criado 
## utilizando a função de quadrado criada
pow_x_sub_x_bar <- c(powerof2(x_sub_x_bar))
pow_x_sub_x_bar


## crie um vetor com o produto das diferença de x e y criado
## utilizando a função de subtração criada
v_mul_xy <- c(multiply(x_sub_x_bar, y_sub_y_bar))
v_mul_xy


## concatene os vetores criados com o data frame
cars <- cbind(cars, x_sub_x_bar, y_sub_y_bar, pow_x_sub_x_bar, v_mul_xy)
cars
summary(cars)
str(cars)


## agora calcule os coeficientes b e a para a reta de regressão
## com os vetores calculados
## b <- sum_prod_dif_xy/sum_dif_x2
## a <- y_bar- b*x_bar
b <- sum(cars$v_mul_xy) / sum(cars$pow_x_sub_x_bar)
b

a <- y_bar - (b * x_bar)
a


## Com os coeficientes criados crie uma função que estime o valor de mpg
## dado um valor de hp
## y = a + bx
getmpg <- function(hp) {
  return(a + b*hp)
}


## crie um vetor com os valores preditos f(x) os valores de hp


## concatene os valores preditos no data frame


## calcule os as variaçoes explicada, nao explicada e total


## Calcule o coeficiente de Determinação


## Calcule a Covariancia


## Calcule a Correlação


## Plote a curva no gráfico de dispersão. Dica: utilize a 
## função curve(add = TRUE)
plot(x = cars$hp, y = cars$mpg, type = 'p', 
     main = "Horse Power influence on car consumption",
     xlab = "Horse Power",
     ylab = "Miles per Gallon")

curve(getmpg(x), from = 40, to = 400, add = T, col = "red")


## Plote um histograma com os RESÍDUOS não explicados


## Escreva sobre o que encontrou e seus resultados obtidos


## salve o data frame como csv com o nome resultado_carros.csv
write.csv2(cars, file = "resultado_carros.csv")


## salve a funcao de regressao para o arquivo linear_carros.R


## salve o script dentro da pasta


mydnorm <- function(x, mean, sd) {
  a = sd * sqrt(2*pi)
  b = -(1/2) * ((x-mean)/sd)^2
  return ((1/a)*exp(b))
}

# Create a sequence of numbers between -10 and 10 incrementing by 0.1.
x <- seq(-5, 5, by = .1)
x

# Choose the mean as 2.5 and standard deviation as 0.5.
y <- mydnorm(x, mean = 0, sd = 1)
y

plot(x,y, xlim=c(-5, 5), ylim=c(0,1))


