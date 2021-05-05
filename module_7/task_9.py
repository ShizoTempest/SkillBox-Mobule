income_end = 0
for month in range(0, 10):
  income = int(input('Какая зарплата была в этом месяце? '))
  if income > income_end:
    print('Зарплата больше чем в прошлый месяц.')
  else:
    print('Зарпалата понизилась, нету смысла здесь оставаться.')
    break
  income_end = income
if income > income_end:
  print('Можно оставаться на этой должности.')
