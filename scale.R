setwd("~/PycharmProjects/mlp")
x <- read.table("data.test.2", header=TRUE, sep = ',')
features=x[,c(2:ncol(x))]
features = scale(features, center=TRUE, scale=TRUE)
data = data.frame(x[,1], features)
write.table(data, file="scale.test.2", sep=", ", row.names=FALSE, col.names=FALSE)
