setwd('~/Py/constructions/')

data = read.csv('data.tsv', sep='\t', header = T)

data$neg = as.factor(data$neg)

summary(data)

can.usual.neg.count <- sum(data[data$verb.category=='can.usual',]$neg)
can.usual.pos.count <- nrow(data[data$verb.category=='can.usual',]) - can.usual.neg.count

can.into.neg.count <- sum(data[data$verb.category=='can.into',]$neg)
can.into.pos.count <- nrow(data[data$verb.category=='can.into',]) - can.into.neg.count

can.usual <- c(neg=can.usual.neg.count, pos=can.usual.pos.count)
can.into <- c(neg=can.into.neg.count, pos=can.into.pos.count)
df = as.data.frame(rbind(can.usual, can.into))
chisq.test(df)

