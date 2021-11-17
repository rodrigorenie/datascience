#Funcções úteis

#                                 Binomial            Pois
# Função de densidade             dbinom(n,k,p)       dpois(k,n,p)
# Funcção de distribuição         pbinom(n,k,p)       ppois(k,lmbda)
# Função de quantis               qbinom(prob,n,p)    ppois(prob,lmbda)
# Função de amostras aleatórias   rbinom(amost,n,p)   ppois(amost,lmbda)


#                                 Normal
# Função de densidade             dnorm(x,mean,sd)
# Funcção de distribuição         pnorm(q,mean,sd)
# Função de quantis               qnorm(prob,mean,sd)
# Função de amostras aleatórias   rnorm(n,mean,sd)


# rxxx(n) gera uma sequencia de números aleatórios conforme a distribuiçao xxx
# dxxx(x) calcula a funcao densidade para o valor de x conforme a distribuiçao xxx
# qxxx(prob) calcula o valor de Z para a probabilidade acumulada prob
# pxxx(Z) calcula o valor da área acumulada sob a curva de densidade da distribuiçao para um dado valor de Z

#por exemplo, quando xxx é a normal trocamos xxx por norm, ou pois para poisson, unif para uniforme e assim por diante

rnorm(10) #gera uma sequencia de números aleatórios conforme a distribuiçao xxx
dnorm(0) #calcula a funcao densidade para o valor de x conforme a distribuiçao xxx
qnorm(0.975) #calcula o valor de Z para a probabilidade acumulada prob
pnorm(1.96) #calcula o valor da área acumulada sob a curva de densidade da distribuiçao para um dado valor de Z


##############################################################################
##############################################################################
# teorema central do limite Moeda
##############################################################################
contagem <- NULL
for (v in 1:1000) {
  a <- sample(c("Cara","Coroa"),10000,replace=T)
  contagem <- rbind(contagem, length(a[a=="Cara"]))
}
contagem
hist(contagem)


##############################################################################
##############################################################################
# teorema central do limite Dados com 6 lados e 10 linhas
##############################################################################
contagem <- NULL
for (v in 1:10) {
  a <- sample(1:6,100,replace=T)
  contagem <- rbind(contagem, length(a[a==3]))
}
contagem
hist(contagem, freq = F)
mean(contagem)


##############################################################################
##############################################################################
# teorema central do limite Dados com 6 faces e 1000 linhas
##############################################################################
contagem <- NULL
for (v in 1:1000) {
  a <- sample(1:6,100,replace=T)
  contagem <- rbind(contagem, length(a[a<=5]))
}
contagem
hist(contagem, freq = F)
mean(contagem)/100


##############################################################################
##############################################################################
# Teorema do limite central distribuição de POISON(5) Média
##############################################################################
rp <- rpois(n=100000, lambda = 5)
hist(rp)
mean(rp)

medias <- NULL
for (v in 1:1000) {
  a <- sample(rp,100,replace=T)
  medias <- rbind(medias, mean(a))
}
hist(medias, freq = F)


##############################################################################
##############################################################################
# Teorema do limite central pois(5) -> Somas
##############################################################################
rp <- rpois(n=100000, lambda = 5)
hist(rp)
mean(rp)

somas <- NULL
for (v in 1:1000) {
  a <- sample(rp,100,replace=T)
  somas <- rbind(somas, sum(a))
}
hist(somas, freq = F)








##############################################################################
##############################################################################
# Teorema do limite central Média de uma distribuição uniforme
##############################################################################
rp <- sample(1:6,10000,replace=T)
#limpa o gráfico
par(mfrow=c(1,1))
hist(rp, include.lowest = T)

par(mfrow=c(1,4))

for(n in c(1,4,8,16)){
  #  n=4
  p <- NULL
  for (v in 1:1000) {
    a <- sample(rp, n ,replace=T)
    p <- rbind(p, mean(a))
  }
  hist(p, freq = F, xlab = paste("Média =",round(mean(p),2)), ylab="Densidade", main = paste0("n=",n, " sd=",round(sd(p),2))  , ylim=c(0,1))
  curve(dnorm(x,mean=mean(p),sd = sd(p)), from = 0, to=6, add = T, col="red")
}



#Exemplo área de subtração de área de probabilidade
par(mfrow=c(2,1))

curve(dnorm(x, 0, 1), from = -4, to=4, xlim=c(-4, 4), ylab="Densidade", main="N(0,1)")
inicio_area <- -5
fim_area <- 0.95
x <- seq(inicio_area,fim_area,by=0.01)
polygon(c(inicio_area,x,fim_area), c(inicio_area,dnorm(x,0,1),0), col="yellow")
text(0.95, 0, paste0("p=",round( pnorm(fim_area,0,1),2) ) , adj = c(1,0))
axis(side=1,at=c(fim_area),labels=c(fim_area))





#Exemplo área de probabilidade vermelho
#curve(dnorm(x, 0, 1), from = -4, to=4, xlim=c(-4, 4), ylab="Densidade", main="N(0,1)")
inicio_area <- -5
fim_area <- 0
x <- seq(inicio_area,fim_area,by=0.01)
polygon(c(inicio_area,x,fim_area), c(inicio_area,dnorm(x,0,1),0), col="red")
text(0, 0, paste0("p=",round( pnorm(fim_area,0,1),2) ) , adj = c(1,0))
axis(side=1,at=c(fim_area),labels=c(fim_area))

#Exemplo área de probabilidade verde
curve(dnorm(x, 0, 1), from = -4, to=4, xlim=c(-4, 4), ylab="Densidade", main="N(0,1)")
x <- seq(0,0.95,by=0.01)
polygon(c(0,x,0.95), c(0,dnorm(x,0,1),0), col="green")
text(0.95, 0, paste0("p=",round( pnorm(0.95,0,1),2) ) , adj = c(1,0))
axis(side=1,at=c(0.95),labels=c(0.95))







##############################################################################
##############################################################################
## teorema central do limite Comparativo
##############################################################################
set.seed(123)
# altura da populacao em cm
# uma população possui altura média 1.65 e desvio padrão 0.3
# calcule a probabilidade de ter mais de 1,90 pela área de função de densidade e
# pelo teorema de limite central

populacao <- rnorm(10000, 1.65, 0.3)

altura <- 1.90
n <- 300

amostra <- sample(populacao,n,replace = TRUE)
#limpa o gráfico
par(mfrow=c(1,1))
hist(amostra)
mean(amostra)
sd(amostra)

#probabilidade de ter mais de 1,90 de altura
#P(X > 1,90) = 1 - P(X <= 1,90)
Z <- (altura-mean(amostra))/sd(amostra)
Z



#P(Z > 0.8654394) = 1 - P(Z<= 0.8654394)
probabilidade <- 1 - pnorm(Z)

#P(X > 1,90) = 0.1933988
probabilidade


#plotando o gráfico
par(mfrow=c(1,2))
#histograma
hist(amostra, probability = T, ylab="Densidade")

media <- mean(amostra)
desv <- sd(amostra)
#colocando a área da curva
curve(dnorm(x, media, desv), from = -4, to=4, xlim=c(-4, 4), add = T)
inicio_area <- altura
fim_area <- 3
x <- c(seq(inicio_area,fim_area,by=0.01))
polygon(c(inicio_area,x,fim_area), dnorm(c(0,x,fim_area), media, desv), col="red")
text(2.15, 0.1, paste0("p=",round(probabilidade,2)) )


# Calculando Pelo teorema do limite central


N <- 100
prob <- NULL
for (v in 1:100) {
  a <- sample(populacao,N,replace=T)
  prob <- rbind(prob, length(a[a>altura])/N)
}
prob
sd(prob)

Zc <- qnorm(0.975)
Zc
Zc*sd(prob)/sqrt(length(prob))

IC <- c(
        mean(prob) - Zc*sd(prob)/sqrt(length(prob)),
        mean(prob),
        mean(prob) + Zc*sd(prob)/sqrt(length(prob))
        )
IC <- round(IC,3)
hist(prob, freq = F, main = paste("p =",IC[2]))
abline(v = IC[1], col="green")
abline(v = IC[2], col="red")
abline(v = IC[3], col="green")
axis(side=3,at=IC[1])
axis(side=3,at=IC[3])




##############################################################################
##############################################################################
######################### Ex iC
##############################################################################

#A produção de uma peça tem desvio padrão de 6 horas.
#Coletamos 100 peças para análise com uma média de 450 horas.
#Qual o intervalo de confiança para a produção de peças com confiança de 90%?

sigma <- 6
N <- 100
med <- 450
conf <- 0.90
Zc <- qnorm(0.95, lower.tail = T)

IC <- med - Zc * sigma/sqrt(N)
IC
IC <- med + Zc* sigma/sqrt(N)
IC

##############################################################################
##############################################################################
######################### Ex iC Teste t
##############################################################################
#A amostra
#Coletamos 10 cabos para um teste destrutivo de resistência.
#Qual o intervalo de confiança para a produção de peças com confiança de 95%?
set.seed(123)
amostra <- round(rnorm(10, mean=1100, sd=50))
amostra

sigma <- sd(amostra)


N <- length(amostra)
med <- mean(amostra)
conf <- 0.95
gl <- N -1

Tc <- qt(0.975,lower.tail = T, df= gl)


IC <- c( med - Tc * sigma/sqrt(N),
   med + Tc* sigma/sqrt(N))

round(IC,1)


#criando uma função para calular o itervalo de confiança a partir de uma amostra
ic.m <- function(x, conf = 0.95){
     n <- length(x)
     media <- mean(x)
     variancia <- var(x)
     quantis <- qt(c((1-conf)/2, 1 - (1-conf)/2), df = n-1)
     ic <- media + quantis * sqrt(variancia/n)
     return(ic)
   }
ic.m(amostra)

#utilizando a funçao teste t
t.test(amostra)


##############################################################################
##############################################################################
# Ex probabilidade 1
##############################################################################
#A altura média de um time é de 174 cm e
#desvio padrão de 8cm. Qual a probabilidade de um jogador ter menos de 1,90.
#P(X < 190) = ?

med <- 174
desv <- 8
#P(X < 190) = P(Z < 190-174 )
X <- 190
Zc <- (X- med)/desv
Zc
P <- pnorm(Zc)
P


##############################################################################
##############################################################################
# Ex probabilidade 2
##############################################################################
#A altura média de um time é de 174 cm e
#desvio padrão de 8cm. Qual a probabilidade de um jogador ter mais  de 1,78.
#P(X > 178) = ?

med <- 174
desv <- 8
#P(X > 1,78) = P(Z < 190-174 )
X <- 178
Zc <- (X- med)/desv
Zc
P <- pnorm(Zc)
P


##############################################################################
##############################################################################
# Ex probabilidade 3
##############################################################################
#A altura média de um time é de 174 cm e
#desvio padrão de 8cm. Qual a probabilidade de um jogador ter entre 1,80 e 1,92.
#P(1,80 < X < 192) = ?

#P(1,80 < X < 192) = P(X >1,92) - P(X < 1,80 )

med <- 174
desv <- 8
#P(X > 1,78) = P(Z < 190-174 )
X <- 192
Zc <- (X- med)/desv
Zc
P_192 <- pnorm(Zc)

X <- 180
Zc <- (X- med)/desv
Zc
P_180 <- pnorm(Zc)

P <- P_192-P_180
P

curve(dnorm(x,mean=med, sd= desv), from = 150, to=200, ylab="Densidade")
abline(v=med,lty="dashed")

inicio_area <- 180
fim_area <- 192
seq_x <- seq(inicio_area, fim_area, by=0.1)
xp <- c(180,seq_x, 192)
yp <- c(0, dnorm(seq_x,med, desv),0)
polygon(xp,yp , col="yellow")


text(fim_area, 0.002, paste0("p=",round(P,2) ) , adj = c(1,0))
axis(side=3,at=c(med), gap.axis = 0.25)





