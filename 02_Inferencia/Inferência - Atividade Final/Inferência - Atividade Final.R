#
# Exercício 1
#
library(TeachingDemos)

amostra <- c(1.9, 1.7, 2.8, 2.4, 2.6, 2.5, 2.8, 3.2, 1.6, 2.5)
mu <- 2
sigma <- 0.5

## Realizando os cálculos manualmente

significancia <- 0.05
confianca <- 1 - significancia

k1 <- significancia/2
k2 <- confianca + significancia/2

media <- median(amostra)
n <- length(amostra)

Z <- (media - mu)/(sigma / sqrt(n))

Zk2 <- qnorm(k2)

if (Z > Zk2) {
  print('Rejeita-se a Hipósete Nula (H0)')
} else {
  print('Aceita-se a Hipósete Nula (H0)')
}

## Utilizando a função de teste-Z pronta

pvalue <- z.test(x=amostra ,mu=mu, stdev=sigma, alternative='greater')$p.value

if (pvalue >= significancia) {
  print('Aceita-se a Hipósete Nula (H0)')
} else {
  print('Rejeita-se a Hipósete Nula (H0)')
}

hist(amostra, probability=T, xlim=c(0,4), ylim=c(0,0.8), xaxt='n', yaxt='n')
axis(side=1, at=seq(0, 6, by=0.5), labels=T)
axis(side=2, at=seq(0, 0.8, by=0.1), labels=T)
curve(expr = dnorm(x, mean=mu , sd=sigma), col = "red", add=T)
abline(v=median(amostra), col='blue')



#
# Exercício 2
#

metal1 <- c(68, 75, 62, 86, 52, 46, 72)
metal2 <- c(61, 69, 64, 76, 52, 38, 68)
confianca <- 0.9
significancia <- (1 - confianca)

pvalue.v <- var.test(metal1, metal2)$p.value

if (pvalue.v > significancia) {
  var <- TRUE
} else {
  var <- FALSE
}

pvalue.t <- t.test(metal1, metal2, alternative = 'two.sided',
                   conf.level=confianca, var.equal=var)$p.value


# Se o valor do p-value é inferior ou igual ao nível de significância, então
# podemos rejeitar a Hipótese Nula (H0) e aceitar a Hipótese Alternativa (H1).
if (pvalue.t > significancia) {
  print('Aceita-se a Hipósete Nula (H0)')
} else {
  print('Rejeita-se a Hipósete Nula (H0)')
}



#
# Exercício 4 
#

lprod <- c(5.4, 4.5, 4.7, 4.0, 3.9, 5.3, 5.4, 5.1, 5.9, 7.1, 4.5, 2.7, 6.0, 4.3,
           4.3, 6.0, 4.7, 3.8, 5.2, 4.9, 5.0, 5.4, 4.6, 5.6, 4.8, 5.3, 6.1, 5.4,
           4.7, 6.1, 6.0, 5.5, 5.2, 4.4, 6.4, 4.4, 7.2, 6.5, 4.8, 4.0)

lprod.median <- median(lprod)
lprod.mean <- mean(lprod)
lprod.sd <- sd(lprod)

lprod.1qt <- as.numeric(quantile(lprod)['25%'])
lprod.2qt <- as.numeric(quantile(lprod)['50%'])
lprod.3qt <- as.numeric(quantile(lprod)['75%'])

boxplot(lprod)

hist(lprod)


# P(4.2 < X < 5.2) = P(X < 5.2) - P(X < 4.2)

getz <- function(x, mean=0, sd=0) {
  if (missing(mean)) {
    mean <- mean(x)
  }
  
  if (missing(sd)) {
    sd <- sd(x)
  }
  
  return ((x - mean)/sd)
}

# P(X < 5.2)
PZ_5.2 <- pnorm(getz(5.2, lprod.mean, lprod.sd))
PZ_5.2

# P(X < 4.2)
PZ_4.2 <- pnorm(getz(4.2, lprod.mean, lprod.sd))
PZ_4.2

P <- PZ_5.2 - PZ_4.2
P

curve(dnorm(x, mean=mean(lprod), sd=sd(lprod)), 
      from = min(lprod), to = max(lprod), 
      ylab="Densidade", xlab="Peso", xaxt='n')
axis(side=1, at=seq(min(lprod), max(lprod), by=0.5), labels=T)

seqx <- seq(4.2, 5.2, by=0.2)
xp <- c(4.2, seqx, 5.2)
yp <- c(0, dnorm(seqx, lprod.mean, lprod.sd), 0)
polygon(xp, yp, col="green")
abline(v=lprod.median, lty="dashed")
text(5, 0.05, sprintf("P = %.2f", P) , adj=c(1,0))















