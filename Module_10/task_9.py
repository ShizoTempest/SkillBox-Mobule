summ = 1
count = 0
change = int(input('Введите количество уровней пирамиды: '))
conclusion = (change * 2 - 1) // 2 #Не трогай, писец всему коду

for first in range(change):
  for second in range(change * 2 - 1):
    if second == conclusion + first or second == conclusion - first: #Для построения
      bon = second
      print(summ, end = '\t') #Изменить в случае ошибки
      summ += 2
    elif first >= 2 and second < conclusion + first and second == bon + 2: #Для чисел в пирамиде
      print(summ, end = '\t')
      summ += 2
      bon += 2
    else:
      print(' ', end = '\t')
  print()