breach = 0
number = 30
for sector in range(0, 6):
  print('Участко под номером:', number)
  human = int(input('Сколько человек было в этой зоне?: '))
  if human > 10:
    print('Замечено нарушение!')
    number += 1
    breach += 1
  else:
    print('Нарушений нет.')
    number += 1
print('Общее кол-во нарушений:', breach)
