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

# программа использует лишнюю переменную и ее можно было бы решить чуть более изящно:
# count = 0
# for district in range(30,36):
#   print('Людей в', district)
#   people = int(input('секторе: '))
#   if people > 10:
#     print('Нарушение! Слишком много людей в секторе')
#     count += 1
#   else:
#     print('Все спокойно.')
# print('Всего нарушений: ', count)

#зачтено
