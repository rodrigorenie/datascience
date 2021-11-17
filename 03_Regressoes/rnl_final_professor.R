dados <- read.csv("servico-atividade-final-2.csv", header = TRUE, sep = ";", encoding = "UTF-8", stringsAsFactors = FALSE)
dados

head(dados)
tail(dados)

data <- as.Date(dados$data, origin = "1970-01-01")
dados$data <- data
dados$dia <- as.numeric(dados$data)
dados$dia <- dados$dia-min(dados$dia)
head(dados)

acumulado <- cumsum(dados$uso)
dados <- cbind(dados, acumulado)
dados

library("tidyverse")

options(scipen = 999)
plot(dados$acumulado ~ dados$dia, xlab = "dia", ylab = "uso")

hist(dados$uso, main="Histograma", xlab = "Uso Diario")

dados$ac_reduzido <- dados$acumulado/1000
dados

x1 <- min(dados$dia)
xf <- max(dados$dia)+1500
dia2 <- x1:xf

curva1 <- NULL
curva1$formula <- y ~ (b0) / (1 + exp(-b1 * (x - b2)))

b0 <- max(dados$ac_reduzido) * 10
b1 <- 0.001
b2 <- max(dados$dia)

curva1$parametros <- list(b0=b0, b1=b1, b2=b2)

modelo <- nls(formula = y ~ b0 / (1 + exp(-b1 * (x - b2))),
              start = list(b0=b0, b1=b1, b2=b2),
              data = data.frame(y = dados$ac_reduzido, x = dados$dia))
summary(modelo)

cbind(AIC_nla = AIC(modelo), AIC_In = AIC(glm(uso ~ dia, data = dados)), AIC_glm = AIC(glm(uso ~ dia, data = dados, family = Gamma())))
plot(dados$ac_reduzido ~ dados$dia, xlab = "dia", ylab = "uso/1000")
points(dados$dia, predict(modelo), type = "l", col = "red", lwd = 3)

hoje <- max(dados$dia)
consumido <- max(dados$acumulado)

dia3anos <- hoje + 3*365
previsao <- data.frame(dia = hoje:dia3anos)
previsao$consumo <- predict(modelo, newdata = data.frame(x = previsao$dia))
tail(previsao)

plot(dados$ac_reduzido ~ dados$dia,
     xlab = "dia",
     ylab = "uso/1000",
     xlim = c(min(dados$dia), dia3anos),
     ylim = c(0, max(previsao)))
lines(x = previsao$dia, y = previsao$consumo, lwd=3, col = "green")
points(dados$dia, predict(modelo), type="l", lwd=3, col="red")

coefficients(modelo)

planoA <- function(x){
  x * 0.35
}

planoB <- function(x, meses){
  x * 0.3 + 10000 * meses
}

planoC <- function(x){
  x * 0.17 + 1000000
}

consumido <- max(dados$acumulado)
consumo3anos <- max(previsao$consumo) * 1000 - consumido
consumo3anos

custos <- cbind(
  custoA = planoA(consumo3anos),
  custoB = planoB(consumo3anos, 36),
  custoC = planoC(consumo3anos)
)

custos

confint(modelo)

intervalo <- confint(modelo)[1,]*1000

CustosAssintotica <- cbind(
  custoA = planoA(intervalo - consumido),
  custoB = planoB(intervalo - consumido, 36),
  custoC = planoC(intervalo - consumido)
)

CustosAssintotica


#mandar para professor com titulo UP2020-PTI-REGNL