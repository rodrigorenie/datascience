

#
# Regressão Linear
#

# 1. Definir uma variável alvo: mpg (Y)

# 2. Definir uma variável independente: hp (X)

# Fazer o gŕafico de dispersão para tentar identificar uma relação
plot(mtcars$hp, mtcars$mpg)
# relação inversa, alpha1 é negativo

cor(mtcars$hp, mtcars$mpg)

# observar a distribuição (sqrt melhora a normalidade)
hist(mtcars$mpg)
hist(sqrt(mtcars$mpg))

# verificar a normalidade (sqrt melhora a normalidade)
# p-value deve server maior que 0.05 para aceitar
shapiro.test(mtcars$mpg)
shapiro.test(sqrt(mtcars$mpg))

modelo.linear <- lm(mtcars$mpg ~ mtcars$hp)
modelo.linear$fitted.values

plot(mtcars$hp, mtcars$mpg)
abline(modelo.linear, col = 'red')
points(modelo.linear$fitted.values ~ mtcars$hp, col = 'blue')

summary(modelo.linear)
str(summary(modelo.linear))
summary(modelo.linear)$r.squared

# retorna o alpha0 e alpha1 podendo ser usados para criar as predições de Y
coefficients(modelo.linear)

# ou usar o predict
predicao <- predict(modelo.linear, newdata = data.frame(hp=150:175))

# Verificar se os resíduos seguem a distribuição normal
hist(residuals(modelo.linear))
hist(modelo.linear$residuals)

shapiro.test(modelo.linear$residuals)
# como p-value é menor que 0.05 (5%), este modelo não se adequa

summary(modelo.linear)$r.squared
# o valor da determinação acima também indica isso, dizendo que este modelo
# explica apenas 60% dos valores da variável alvo (Y = mpg)