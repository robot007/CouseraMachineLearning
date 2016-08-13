getwd()
a <- c(1,2,3, 4)
b <- c(2,4,6,8)
c <- b
b[2] <- 4.2
c[2]

levels <- factor(c("A","B","A","B"))
bubba <- data.frame(first=a,
                    second=b,
                    f=levels)
bubba

ls()
# adf
typeof(a)
