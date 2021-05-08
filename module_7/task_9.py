income_end = 0
flag = True
for month in range(0, 10):
  income = int(input('Какая зарплата была в этом месяце? '))
  if income >= income_end:
    print('Зарплата больше, чем в прошлый месяц.')
  else:
    print('Зарплата понизилась.')
    flag = False
  income_end = income
if flag == False:
  print('Зарпалата не упорядочена.')
else:
  print('Зарплата упорядочена.')

# зачтено
