summ = 0
for month in range(12):
  print('Номер месяца:', month + 1)
  while True:
    income = int(input('Какая зарплата в этот месяц: '))
    if income < 0:
      print('Ошибка ввода, зарплата должна быть положительная.')
    else:
      break
  summ += income
summ /= 12
print('Средняя зарплата:', round(summ, 2))

# зачтено
