#
# Exercício 1
#

mec <- data.frame(
  row.names = c("RR", "AC", "PA", "TO", "MA", "SE", "BA", "AL", "SP", "ES", 
                "SC", "PR", "GO", "DF", "AP", "RO", "AM", "PB", "RN", "PI", 
                "PE","CE","RJ", "MG","RS","MT","MS"),
  escolaridade = c(5.7, 4.5, 4.7, 4.5, 3.6, 4.3, 4.1, 3.7, 6.8, 5.7, 6.3, 6.0,
                   5.5, 8.2, 6.0, 4.9, 5.5, 3.9, 4.5, 3.5, 4.6, 4.0, 7.1, 5.4, 
                   6.4, 5.4, 5.7),
  renda = c(685, 526, 536, 520, 343, 462, 460, 454, 1076, 722, 814, 782, 689,
            1499, 683, 662, 627, 423, 513, 383, 517, 448, 970, 681, 800, 775,
            731)
)

plot(mec)
cor(mec)

hist(mec$renda)
hist(mec$escolaridade)

# Shapiro Test
# H0: x  = normal (há normalidade)
# H1: x != normal (não há normalidade)

if (shapiro.test(mec$renda)$p.value > 0.05) {
  print('Aceita-se a Hipósete Nula (H0)')
} else {
  print('Rejeita-se a Hipósete Nula (H0)')
}

if (shapiro.test(mec$escolaridade)$p.value > 0.05) {
  print('Aceita-se a Hipósete Nula (H0)')
} else {
  print('Rejeita-se a Hipósete Nula (H0)')
}

modelo.linear <- lm(renda ~ escolaridade, data=mec)
hist(modelo.linear$residuals)
shapiro.test(modelo.linear$residuals)

plot(mec)
abline(modelo.linear, col='red')
points(mec$escolaridade, modelo.linear$fitted.values, col='red')

sort(influence(modelo.linear)$hat)
layout(matrix(c(1, 2, 3, 4), 2, 2))
plot(modelo.linear)

summary(modelo.linear)$r.squared


library(hnp)
hnp(modelo.linear, xlab='N(0,1)', ylab='Resíduos',
    main=modelo.linear$call$formula)


if (shapiro.test(modelo.linear$residuals)$p.value > 0.05) {
  print('Aceita-se a Hipósete Nula (H0)')
} else {
  print('Rejeita-se a Hipósete Nula (H0)')
}

modelo.gamma <- glm(renda ~ escolaridade, data=mec, family=Gamma(link='log'))
hist(modelo.gamma$residuals)
shapiro.test(modelo.gamma$residuals)

modelo.invgaus <- glm(renda ~ escolaridade, data=mec,
                      family=inverse.gaussian(link='log'))
hist(modelo.invgaus$residuals)
shapiro.test(modelo.invgaus$residuals)

predict.values <- seq(from=-6, to=12, by=0.25)
predict.dataframe <- data.frame(escolaridade=predict.values)

predict.linear <- predict(modelo.linear, predict.dataframe, type='response')
predict.gamma <- predict(modelo.gamma, predict.dataframe, type='response')
predict.invgaus <- predict(modelo.invgaus, predict.dataframe, type='response')

plot(mec, data=mec, ylim=c(-250,2000), xlim=c(-6,12), col='black', bg='grey', 
     pch=21, xaxt='n', yaxt='n')
axis(side=1, at=seq(-6, 12, by=1), labels=T)
axis(side=2, at=seq(-250, 2000, by=250), labels=T)
abline(h=0, col='grey')

points(predict.values, predict.linear, pch=21, col='white', bg='red')
points(predict.values, predict.gamma, pch=21, col='white', bg='blue')
lines(predict.values, predict.invgaus, pch=21, col='green')


AIC(modelo.linear, modelo.gamma, modelo.invgaus)


hnp(modelo.linear, xlab='N(0,1)', ylab='Resíduos',
    main=modelo.linear$call$formula)



#
# Exercício 2
#

library(TTR)
library(forecast)

setwd('Z:\\Dropbox\\Itaipu\\Pós Graduação\\Danilo Souto\\03 Regressões\\Atividade Final')

serie.dados <- read.csv('dados_tickets.csv')
hist(serie.dados$TOTAL)
shapiro.test(serie.dados$TOTAL)

serie.ts <- ts(serie.dados$TOTAL, start=c(2017, 2), end=c(2020, 11), frequency=12)
plot(serie.ts)

serie.dc <- decompose(serie.ts)
plot(serie.dc)

serie.holt <- HoltWinters(serie.ts)
plot(serie.holt)

serie.previsao1 <- forecast(serie.holt, h=13)
plot(serie.previsao1)

serie.previsao2 <- predict(serie.holt, n.ahead=13, 
                           prediction.interval=T, level=0.95)
plot(serie.holt, serie.previsao2)
