# конструкция "уметь в X-а" на основе данных из twitter

## Данные

[Таблица с данными](https://github.com/gree-gorey/constructions/blob/master/data.tsv)

## Работа с данными

### Гипотеза

Конструкция "уметь в X-а" чаще встречается с отрицанием, чем просто конструкция "уметь X-овать" или просто "уметь" без аргументов.

### Данные

"уметь в" -- 63 твита<br>
"уметь" -- 61 твит<br>

Данные размечены и помещены в [таблицу](https://github.com/gree-gorey/constructions/blob/master/data.tsv).

### Статистика

```
data = read.csv('data.tsv', sep='\t', header = T)

can.usual.neg.count <- sum(data[data$verb.category=='can.usual',]$neg)
can.usual.pos.count <- nrow(data[data$verb.category=='can.usual',]) - can.usual.neg.count

can.into.neg.count <- sum(data[data$verb.category=='can.into',]$neg)
can.into.pos.count <- nrow(data[data$verb.category=='can.into',]) - can.into.neg.count

can.usual <- c(neg=can.usual.neg.count, pos=can.usual.pos.count)
can.into <- c(neg=can.into.neg.count, pos=can.into.pos.count)
df = as.data.frame(rbind(can.usual, can.into))
chisq.test(df)
```

Табличка для хи-квадрата:

|           | neg | pos |
| --------- | --- | --- |
| can.usual | 39  | 22  |
| can.into  | 58  | 5   |


### Результат

```

	Pearson's Chi-squared test with Yates' continuity correction

data:  df
X-squared = 12.793, df = 1, p-value = 0.000348
```

### Обсуждение результатов

Поскольку получившееся значение p-value < 0.001, это позволяет нам сделать вывод о том, что тип конструкции связан с отрицанием: конструкция "я (не) умею в Х-а" больше тяготеет к тому чтобы быть под отрицанием, чем просто конструкция "я (не) умею Х-овать".