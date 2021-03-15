f <- function(x) {
  return(-x^4 + 2*x + 2)
}

curve(f, from=-2, to=3)
abline(v=-1, col="red", lty=4)
abline(v=2, col="red", lty=4)

x <- seq(from=-1, to=2, by=.01)
y <- f(x)

# O maior valor de y
max(y)

# No vetor de y, qual é a posição contendo o maior valor?
which(y == max(y))

# Nessa mesma posição no vetor de x, estará a posição do valor mínimo no gráfico
x[which(y == max(y))]

# Portanto, o y máximo:
y.max <- max(y)

# Portanto, o x máximo:
x.max <- x[which(y == max(y))]

points(x.max, y.max, col='red', pch=8)

# Ou, tudo automático:
result <- optimize(f, c(-1,2), maximum=T, tol=0.01)
x.max <- result$maximum
y.max <- result$objective

points(x.max, y.max, col='blue', pch=20)









da <- data.frame(y=c(51.03, 57.76, 26.60, 60.65, 87.07, 64.67, 91.28, 105.22,
                    72.74, 81.88, 97.62, 90.14, 89.88, 113.22, 90.91, 115.39,
                    112.63, 87.51, 104.69, 120.58, 114.32, 130.07, 117.65,
                    111.69, 128.54, 126.88, 127.00, 134.17, 149.66, 118.25,
                    132.67, 154.48, 129.11, 151.83, 147.66, 127.30),
                x=rep(c(15, 30, 45, 60, 75, 90, 120, 150, 180, 210, 240, 270), each=3),
                r=rep(1:3, 12))


plot(y~x, data=da, xlab="Dias após incubação", ylab="Conteúdo acumulado liberado de potássio")

f <- function(y, A, V) {
  y~A*x/(V+x)
}

# A = Assíntota (o maior valor da curva)
# V = Meia vida (qual é o valor de X onde estarão 50% dos meus dados)
n0 <- nls(formula=y~A*x/(V+x), data=da, start=list(A=160, V=40), trace=T)

summary(n0)

confint(n0)

coef(n0)

