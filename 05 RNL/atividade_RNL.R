require(rstudioapi)

#
# Aluno: Rodrigo Renie de Braga Pinto
#

#
# Define a diretório corrente para o mesmo ao da localização do arquivo 
# atualmente aberto no RStudio
#
setwd_curfile <- function() {
  path <- getActiveDocumentContext()$path
  dir <- dirname(path)
  message(paste("Setting CWD to '", dir, "'", sep=''))
  setwd(dir)
}

setwd_curfile()
options(scipen=999)

#
# Lê os dados coletados e faz as conversões necessárias
#
dados.csv <- read.csv2('servico-atividade-final-2.csv')
dados.csv$data <- as.Date(dados.csv$data)

#
# Data frame gerado para preencher os dias faltantes dos dados coletados
#
# filler <- data.frame(
#   data=seq.Date(min(dados.csv$data), max(dados.csv$data), by='day')
# )
# filler$ano <- as.numeric(format(filler$data, '%Y'))
# filler$mes <- as.numeric(format(filler$data, '%m'))

#
# Faz o merge dos dados originais com o filler, mantando os dados originais e
# definindo para 0 (zero) os dados de consumo faltantes
#
# dados.csv <- merge(dados.csv, filler, all.y=T)
# dados.csv[is.na(dados.csv)] <- 0

#
# Cria dois novos campos no CSV original, um contendo o uso acumulado e outro
# convertendo o tipo Data em dias corridos (començando de 0)
#
dados.csv$dia <- as.numeric(dados.csv$data) - as.numeric(min(dados.csv$data))
dados.csv$uso_acumulado <- cumsum(dados.csv$uso)/1000
hist(dados.csv$uso_acumulado)
plot(uso_acumulado ~ dia, data=dados.csv)

# Considerando o gráfico dos dados coletados:
#   - b0: O maior ponto máximo da curva (com alguma extrapolação)
#   - b1: O grau da curva
#   - b2: O ponto em X (dia) onde estarão 50% dos dados (média da área da curva)
# Crie o modelo baseado nesses valores
dados.b0 <- max(dados.csv$uso_acumulado) * 10
dados.b1 <- 0.001
dados.b2 <- max(dados.csv$dia)

dados.formula <- uso_acumulado ~ (b0)/(1 + exp(-b1*(dia-b2)))
dados.start  <- list(b0=dados.b0, b1=dados.b1, b2=dados.b2)

dados.modelo <- nls(formula=dados.formula, data=dados.csv, start=dados.start)
summary(dados.modelo)
confint(dados.modelo)

plot(dados.csv$uso_acumulado ~ dados.csv$dia, 
     xlab='Dia', ylab='Uso / 1000')
points(dados.csv$dia, predict(dados.modelo),
       col='red', type='l', lwd=3)

#
# A previsão deverá ser a partir do dia seguinte ao último dia coletado até
# três anos após esta data, portanto calcule qual o valor de X (dia) desse 
# período:
#
previsao.dia_ini <- max(dados.csv$dia) +1
previsao.dia_fim <- previsao.dia_ini + 365*3
  
previsao.data <- data.frame(dia=previsao.dia_ini:previsao.dia_fim)
previsao.data$uso_acumulado <- predict(
  dados.modelo, newdata=data.frame(dia=previsao.data$dia))

plot(dados.csv$uso_acumulado ~ dados.csv$dia, 
     xlab='Dia', ylab='Uso / 1000',
     xlim=c(min(dados.csv$dia), previsao.dia_fim),
     ylim=c(min(dados.csv$uso_acumulado), max(previsao.data$uso_acumulado)))
points(dados.csv$dia, predict(dados.modelo), 
       col='red', type='l', lwd=3)
points(previsao.data$dia, previsao.data$uso_acumulado, 
       col='green', type='l', lwd=3)

planoA <- function(uso) {
  0.35*uso
}

planoB <- function(uso, meses) {
  10000*meses + 0.30*uso
}

planoC <- function(uso) {
  1000000 + 0.17*uso
}

print.currency <- function(x) {
  paste0('R$ ', formatC(as.numeric(x), 
                        format='f', digits=2,
                        decimal.mark=',', big.mark='.'))
}

#
# Para calcular apenas o custo gerado pela previsão, deve-se remover o uso
# acumulado dos dados coletados dos dados de previsão, já que a previsão inicia
# onde dados coletados termina. Além disso, multiplica-se por 1000 pois os dados 
# foram dividos por 1000 anteriormente para ajustar as escalas entre o uso 
# acumulado e os dias corridos.
#
# Porém, como a primeira previsão de uso acumulado do nosso modelo é menor que o
# último valor de uso acumulado coletado, se fazer a abordagem descrita antes, o
# primeiro uso acumulado é um valor negativo, o que não faz sentido.
#
# Portanto, eu preferi apenas diminuir os dados de uso acumulado da minha 
# previsão com seu valor máximo, trazendo assim o primeiro valor acumulado da 
# minha previsão para zero
#

previsao.data$uso_acumulado_ajustado <- previsao.data$uso_acumulado*1000
previsao.data$uso_acumulado_ajustado <- 
  previsao.data$uso_acumulado_ajustado - 
  min(previsao.data$uso_acumulado_ajustado)

tail(dados.csv)
head(previsao.data)
  
previsao.meses <- as.integer(length(previsao.data$dia)/30)
previsao.uso_total <- max(previsao.data$uso_acumulado_ajustado)

a <- planoA(previsao.uso_total)
b <- planoB(previsao.uso_total, previsao.meses)
c <- planoC(previsao.uso_total)

resultado <- data.frame(
  plano=c('Plano A', 'Plano B', 'Plano C'),
  total=c(a, b, c),
  valor=print.currency(c(a, b, c))
)
resultado

sprintf('A melhor estratégia é o %s com custo total de %s',
       resultado$plano[resultado$total == min(resultado$total)],
       resultado$valor[resultado$total == min(resultado$total)])


#
# Extra: plote as curvas de custos dos planos acima ao longo dos dias de 
# previsão
#
custo.planoa <- planoA(previsao.data$uso_acumulado_ajustado)
custo.planob <- planoB(previsao.data$uso_acumulado_ajustado, previsao.meses)
custo.planoc <- planoC(previsao.data$uso_acumulado_ajustado)

plot(custo.planoa ~ previsao.data$dia,
     xlab='Dia', ylab='Custo', type='l', lwd=2, col='red',
     xlim=c(min(previsao.data$dia), max(previsao.data$dia)+480),
     ylim=c(min(custo.planoa, custo.planob, custo.planoc), 
            max(custo.planoa, custo.planob, custo.planoc)))

points(previsao.data$dia, custo.planob, col='darkorange', type='l', lwd=2)
points(previsao.data$dia, custo.planoc, col='darkgreen', type='l', lwd=2)

texto <- sprintf('%s: %s', resultado$plano[1], resultado$valor[1])
text(max(previsao.data$dia)+240, max(custo.planoa), texto, col='darkred')
texto <- sprintf('%s: %s', resultado$plano[2], resultado$valor[2])
text(max(previsao.data$dia)+240, max(custo.planob), texto, col='darkorange')
texto <- sprintf('%s: %s', resultado$plano[3], resultado$valor[3])
text(max(previsao.data$dia)+240, max(custo.planoc), texto, col='darkgreen')
