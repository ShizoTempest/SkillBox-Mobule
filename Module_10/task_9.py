number = 1
count = 0
n = int(input('Введите количество уровней пирамиды: '))
midle = (n * 2 - 1) // 2
for row in range(n):
  for col in range(n * 2 - 1):
    if col == midle - row or col == midle + row:
      dop = col
      print(number, end = '\t')
      number += 2
    elif row >= 2 and col == dop + 2 and col < midle + row:
      print(number, end = '\t')
      number += 2
      dop += 2
    else:
      print(' ', end = '\t')
  print()