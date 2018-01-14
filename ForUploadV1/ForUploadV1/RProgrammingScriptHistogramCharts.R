####RscriptFor commits per week and cumulative commits per week

v<-c(50,28,24,28,24,20,11,8,19,5,4,14,32,10,20,29,22,12,29,33)
v
png(file = "line_chart.jpg")
plot(v,type = "o", col = "red", xlab = "week", ylab = "Commits",
     main = "Commits by week")


dev.off()


vc<-c(50,78,102,130,154,174,185,193,212,217,221,235,267,277,297,326,358,360,389,422)
png(file = "line_chart.jpg")
plot(vc,type = "o", col = "red", xlab = "week", ylab = "Commits",
     main = "Cumulative Commits by week")
dev.off()


######
getwd()
authors<-read.csv("authorsum.csv", header = FALSE)
View(authors)
hist(authors$V2,
     main = "Histogram For Authors",
     xlab = "Authors",
     border = "blue",
     col = "green")
