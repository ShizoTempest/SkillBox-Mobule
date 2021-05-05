month = 0
summ = 0
for month in range(0, 12):
  income = int(input('Какая зарплата в этот месяц: '))
  summ += income
  month += 1
print('Средняя зарплата:', summ)
