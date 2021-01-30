
### Regressão linear

summary(mtcars)
str(mtcars)

# 1 definir uma variavel alvo. mpg (milhas por galao) Y

# 2 definir uma varial independente X será hp

# gráfico de dispersao

plot(mtcars$hp, mtcars$mpg)
plot(mpg~hp, data=mtcars)
# inversa, negativa (a1 < 0)

attach(mtcars)
cov(mpg,hp)

cor(hp,mpg)

# observar a distribuição
hist(mpg)


# verificar a noramalidade
shapiro.test( mpg )

# verificar homogeniedade nas varianças
fligner.test(mpg ~ hp, data = mtcars)

mean(mpg)
mean(hp)

help(lm)

modelo.linear <- lm(mpg ~ hp, data=mtcars)
summary(modelo.linear)

coefficients(modelo.linear)



modelo.linear$fitted.values

plot(mpg ~ hp)
abline(modelo.linear, col ="red")
points(modelo.linear$fitted.values ~ hp, col = "green")

#coeficiente de determinacao
summary(modelo.linear)$r.squared
summary(modelo.linear)$adj.r.squared

str(summary(modelo.linear))
summary(modelo.linear)$call

hist(residuals(modelo.linear))
hist(modelo.linear$residuals)

shapiro.test(modelo.linear$residuals)


#### predicao
f_mpg <- function(hp){
  coefficients(modelo.linear)[1]+ coefficients(modelo.linear)[2]*hp
}

x <- 100:200
y <- f_mpg(x)
cbind(x,y)

points(  x,y , col="blue")

x <- data.frame(hp=125:175)
predicao <- predict(modelo.linear, newdata = x)
summary(predicao)
points(x$hp, predicao, col="yellow")



plot(mpg ~ hp, xlim=c(0,500), ylim=c(-30,30))
abline(h=0)
abline(v=0)
abline(modelo.linear, col ="red")
points(modelo.linear$fitted.values ~ hp, col = "green")

mean(mpg)

modelo.const <- lm(mpg ~ 1, data=mtcars )
modelo.const

abline(modelo.const, col="green")
abline(modelo.linear, col= "red")
summary(modelo.const)


anova(modelo.const, modelo.linear, test= "Chisq")

anova(modelo.const, modelo.linear, test= "Chisq")


str(mtcars)
dim(mtcars)

summary(modelo.linear)



colnames(mtcars)


boxplot(mpg ~ cyl, data = mtcars)

plot(mpg ~ hp, pch=cyl, col=cyl, data=mtcars)

cor(mpg,hp)
cor(mpg,cyl)
multi.cor <- cor(mtcars[,c("mpg","hp","cyl")])
multi.cor

cor(mtcars)

install.packages("corrplot")
#aqui está uma forma de exibir a correlação
library(corrplot)

corrplot.mixed(multi.cor, upper = "ellipse")
corrplot.mixed(cor(mtcars), upper = "ellipse")


modelo.multi <- lm(mpg ~ cyl + hp, data=mtcars)

summary(modelo.multi)

summary(lm(mpg ~ cyl, data=mtcars))


summary(modelo.multi)$adj.r.squared
summary(modelo.linear)$r.squared


coefficients(modelo.multi)

plot_carros <- function(){
plot(mpg ~ hp , pch =cyl, col = cyl, data = mtcars, xlim=c(0,1000), ylim=c(-10,40))
#points(modelo.multi$fitted.values ~ hp, col = "red", pch = 18, data = mtcars)
fun.reta <- function(x, cyl){
  modelo.multi$coefficients[1]+modelo.multi$coefficients["cyl"]*cyl +
    modelo.multi$coefficients["hp"]*x }
curve(expr = fun.reta(x,4) , from = 0, to = 5000, add = T, col = 4)
curve(expr = fun.reta(x,6) , from = 0, to = 5000, add = T, col = 6)
curve(expr = fun.reta(x,8) , from = 0, to = 5000, add = T, col = 8)
#legend(300,32,legend = c("4","6","8"), pch = c(4,6,8), col = c("blue","pink","grey"), title = "Cilindros")
abline(h=0)
abline(modelo.linear, col="green")
}
plot_carros()
hist(modelo.multi$residuals)
shapiro.test(modelo.multi$residuals)

anova( modelo.const, modelo.linear,modelo.multi, test= "Chisq")

str(mtcars)


install.packages("car")
library(car)

scatterplotMatrix(mtcars[,c("mpg","cyl","hp","wt","qsec")])
coefficients(modelo.multi)
confint(modelo.multi,level = 0.95)

modelo.multi2.0 <- lm( mpg ~ cyl + disp + hp + wt + qsec, data=mtcars)
summary(modelo.multi2.0)
hist(modelo.multi2.0$residuals)

modelo.multi2.0 <- lm( mpg ~ cyl + disp + hp + wt, data=mtcars)
summary(modelo.multi2.0)
hist(modelo.multi2.0$residuals)

modelo.multi2.0 <- lm( mpg ~ cyl + hp + wt, data=mtcars)
summary(modelo.multi2.0)
corrplot.mixed(cor(mtcars), upper = "ellipse")





############ funcao modelo backward
variavel_menor_backward <- function(modelo, dados, coef = 0.975){
  #modelo <- modelo.multi2
  #summary(modelo)
  #coef <- 0.975
  #dados<- mtcars

  #obtém-se os graus de liberdade
  modelo.coef <- summary(modelo)$coefficients;modelo.coef
  if(nrow(summary(modelo)$coefficients) == 2 ){
    return(sprintf("Só há uma variável, nada a remover"))
  }
  gl<-nrow(dados) - length(coefficients(modelo));gl

  #calcula o quantil
  quantile  <- qt(coef,gl);quantile

  modelo.coef <- modelo.coef[-1,];modelo.coef
  #menor_valor <- min (abs(summary(modelo)$coefficients[, "t value"])) ; menor_valor
  menor_valor <- min (abs(modelo.coef[, "t value"])); menor_valor

  #obtém os valores que são menor que o quantil
  nome <- names(which(abs(modelo.coef[,"t value"]) == menor_valor))

  if (quantile > menor_valor) {
    return(sprintf("Remova %s, t %f  < quantil: %f", nome,menor_valor,quantile))
  }
  return(sprintf("Remova %s, t %f  < quantil: %f", nome,menor_valor,quantile))
}

variavel_menor_backward(modelo.multi2.0, mtcars)
modelo.multi2.0$call

modelo.multi2.1 <- lm(mpg ~ cyl + disp + hp + wt, data = mtcars)
summary(modelo.multi2.1)
variavel_menor_backward(modelo.multi2.1, mtcars)

modelo.multi2.2 <- lm(mpg ~ cyl + hp + wt, data = mtcars)
summary(modelo.multi2.2)
variavel_menor_backward(modelo.multi2.2, mtcars)


modelo.multi2.3 <- lm(mpg ~ cyl + wt, data = mtcars)
summary(modelo.multi2.3)
variavel_menor_backward(modelo.multi2.3, mtcars)

hist(modelo.multi2.3$residuals)
shapiro.test(modelo.multi2.3$residuals)

modelo.multi2.4 <- lm(mpg ~  wt, data = mtcars)
summary(modelo.multi2.4)


anova(modelo.multi2.0,modelo.multi2.1,modelo.multi2.2,modelo.multi2.3,modelo.multi2.4,test="Chisq")


install.packages("hnp")
library(hnp)
hnp(modelo.multi2.2)

layout(matrix(c(1,2,3,4),2,2))
hnp(modelo.multi2.0, main = modelo.multi2.0$call$formula)
hnp(modelo.multi2.1, main = modelo.multi2.1$call$formula)
hnp(modelo.multi2.2, main = modelo.multi2.2$call$formula)
hnp(modelo.multi2.3, main = modelo.multi2.3$call$formula)


?AIC
logLik(modelo.multi2.0)
logLik(modelo.multi2.1)
logLik(modelo.multi2.2)
logLik(modelo.multi2.3)


AIC(modelo.multi2.0)
AIC(modelo.multi2.1)
AIC(modelo.multi2.2)
AIC(modelo.multi2.3)




data.frame(
  modelos = c('2.0', '2.1', '2.2', '2.3'),
  aic = c(AIC(modelo.multi2.0), AIC(modelo.multi2.1),
          AIC(modelo.multi2.2),AIC(modelo.multi2.3)),
  verossimilhança = c(logLik(modelo.multi2.0),
                      logLik(modelo.multi2.1),logLik(modelo.multi2.2),
                      logLik(modelo.multi2.3))
)

modelo.multi2.0$call

modelo.multi2.2$call
summary(modelo.multi2.0)
summary(modelo.multi2.2)

library(MASS)

modelo_back <- step(modelo.multi2.0, direction = "backward")
modelo_back
mt <-mtcars[,-7]
 colnames(mtcars)
modelo.todas <- lm(mpg ~ . , mt)
modelo.both <- step(modelo.todas, direction = "both")
summary(modelo.both)

corrplot.mixed(cor(mtcars), upper = "ellipse")
layout(matrix(c(1),1,1))


plot(modelo.both)

sum(sort(influence(modelo.multi2.3)$hat))
modelo.both$call
modelo.multi2.3$call

mtcars[,c("mpg","cyl", "wt")]




################################## GLM
###################### BINOMIAL
insetos <- data.frame(
        dose = c(0.0, 2.6, 3.8, 5.1, 7.7, 10.2),
        total = c(49, 50, 48, 46, 49, 50),
        mortos = c(0, 6, 16, 24, 42, 44))

insetos$proporcao <- NULL
insetos$proporcao <- insetos$mortos/insetos$total

insetos
hist(insetos$proporcao)

plot(proporcao ~ dose, data=insetos, type="l")



modelo.logit <- glm(proporcao ~ dose, data=insetos,
                    family = binomial(link = "logit") )

modelo.probit <- glm(proporcao ~ dose, data=insetos,
                    family = binomial(link = "probit") )

coef(modelo.probit)
coef(modelo.logit)

new.doses <- 1:10
preditos <- predict(modelo.logit, newdata = data.frame(dose=new.doses ))

# funcao inversa
mu <- function(t){
  exp(t)/(1+exp(t))
}

mu(preditos)
plot(new.doses, preditos)
points(new.doses, mu(preditos), type = "l", col="blue")
plot(new.doses, mu(preditos))

preditos.probit <- predict(modelo.probit,
                           newdata = data.frame(dose=new.doses),
                           type="response")

points(new.doses, preditos.probit, col="red", type = "l")
points(proporcao~dose, data= insetos, col="green")


anova(modelo.logit, modelo.probit, test="Chisq")

exp(coef(modelo.probit))
exp(confint(modelo.probit))


############################################################
###### POISSON #############################################
############################################################

bacterias <- c(175, 108,95,82,71,50,49,31,28,17,16,11)
tempo <- c(1:12)

bacterias <- data.frame(bacterias=bacterias, tempo=tempo)
bacterias
plot(bacterias ~tempo, data=bacterias , type="h", xlim=c(0,24),ylim=c(0,180))

modelo.poisson <- glm(bacterias ~ tempo , data=bacterias,
    family = poisson())
summary(modelo.poisson)

preditos.poisson <- predict(modelo.poisson,
                            newdata = data.frame(tempo=1:24))
exp(preditos.poisson)
points(1:24,exp(preditos.poisson), col="red")


int.confianca <- exp(confint.default(modelo.poisson))
int.confianca



####################### GAMA e Gaussiana inversa
attach(mtcars)
hist(mpg)
modelo.ig <- glm(mpg ~ hp, data=mtcars, family = inverse.gaussian())
modelo.gamma <- glm(mpg ~ hp, data=mtcars, family = Gamma())

summary(modelo.ig)
summary(modelo.gamma)
new.hp <- data.frame(hp=1:1000)

predito.gamma <- predict(modelo.gamma, newdata = new.hp,
                         type="response")

predito.ig <- predict(modelo.ig, newdata = new.hp,
                     type="response")
plot_carros()
points(new.hp$hp, predito.ig, col="red", type="l")
points(new.hp$hp, predito.gamma, col="orange", type="l")

modelo.gamma.multi <- glm(mpg ~ hp+ cyl, data=mtcars, family = Gamma())
AIC(modelo.ig, modelo.gamma, modelo.linear, modelo.multi, modelo.gamma.multi)

predito <- predict(modelo.gamma.multi,
                      newdata = data.frame(hp=1:1000, cyl=rep(4,1000)),
                      type="response")
points(1:1000,predito, col="orange", type = "l")
predito <- predict(modelo.gamma.multi,
                   newdata = data.frame(hp=1:1000, cyl=rep(8,1000)),
                   type="response")
points(1:1000,predito, col="orange", type = "l")


hnp(modelo.gamma.multi)
hist(modelo.gamma.multi$residuals)
plot(modelo.gamma.multi)

gamma.todos <- glm(mpg ~ . , data = mtcars, family =  Gamma())
modelo <- step(gamma.todos, direction = "both")

ig.todos <- glm(mpg ~ . , data = mtcars, family =  inverse.gaussian())
modelo.ig.step <- step(ig.todos, direction = "both")


summary(modelo)

hnp(modelo)
plot(modelo)



AIC(modelo.ig, modelo.gamma, modelo.linear, modelo.multi, modelo.gamma.multi, modelo)
anova(modelo.ig, modelo.gamma, modelo.linear, modelo.multi, modelo.gamma.multi, modelo)
