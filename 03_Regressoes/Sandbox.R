#
# Exemplo 3 dos slides da apresentação
#

x = c(1, 2, 3, 4)
y = c(5.943180, 7.733549, 10.739441, 13.255065)

x.avg = mean(x)
y.avg = mean(y)

alpha1 <- sum((x - x.avg) * (y - y.avg)) / sum((x-x.avg)^2)
alpha0 <- y.avg - alpha1 * x.avg


y.est = alpha0 + alpha1*x

erro = y.est - y

SQtot <- sum((y - y.avg)^2)
SQres <- sum((y - y.est)^2)
SQexp <- sum((y.est -y.avg)^2)

r.2 <- SQexp / SQtot 

cov.xy <- sum((x - x.avg) * (y - y.avg)) / length(y)
r.simples <- cov.xy / (sd(x) * sd(y))

plot(x, y, main = paste("Determinação: ", round(r.2, 6)*100, "%", sep=''))
lines(y.est, col='red')
?lines()



# Calcula da covariância e a correlação das duas variáveis indicando se a 
# relação linear entre elas é negativa ou positiva
covaricanca <- cov(mtcars$mpg, mtcars$hp)
correlacao <- cor(mtcars$mpg, mtcars$hp)
sprintf("Cov:%f Cor:%f", covaricanca, correlacao)

plot(mtcars$hp, mtcars$mpg)
hist(mtcars$mpg)

pvtest <- function(pvalue, significancia=0.05) {
  if (pvalue > significancia) {
    print('Aceita-se a Hipósete Nula (H0)')
  } else {
    print('Rejeita-se a Hipósete Nula (H0)')
  }
}

# Shapiro Test
# H0: mpg  = normal (há normalidade)
# H1: mpg != normal (não há normalidade)
pvtest(shapiro.test(mtcars$mpg)$p.value)

# Fligner Test
# H0: existe igualdade nas variâncias
# H1: não existe igualdade nas variâncias
pvtest(fligner.test(mtcars$mpg, mtcars$hp)$p.value)

modelo.linear <- lm(mtcars$mpg ~ mtcars$hp, data=mtcars)
str(modelo.linear)
coefficients(modelo.linear)
summary(modelo.linear)

plot(mtcars$mpg ~ mtcars$hp)
abline(modelo.linear, col='red')
points(mtcars$hp, modelo.linear$fitted.values, col='red')

fitted.values(modelo.linear)

summary(modelo.linear)$adj.r.squared

pvtest(shapiro.test(modelo.linear$residuals)$p.value)
hist(modelo.linear$residuals, freq=F)

n.hp <- 1:1000
predict.linear <- predict(modelo.linear, newdata=data.frame(hp=n.hp), type='response')

plot(mtcars$mpg ~ mtcars$hp, ylim=c(-5, 30), xlim=c(0,1000))
lines(seq(1, 1000, 1), predict.linear)

