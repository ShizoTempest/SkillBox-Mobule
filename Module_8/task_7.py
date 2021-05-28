while True:
  educational_grant = int(input('Введите ежемесячную стипендию студента: '))
  expenses = int(input('Введите расходы на проживание, которые превышают стипендию и составляют: '))
  summ = expenses - educational_grant
  num = 10
  if educational_grant >= expenses:
    print('Расчет сломан. Повторите.')
  else:
    break
for month in range(num - 1):
  expenses += expenses * 3 / 100
  summ += expenses - educational_grant
  print(expenses, summ)
print('Не достаточно средств:', round(summ, 2), 'Попробуйте поросить эту суммы у родителей.')