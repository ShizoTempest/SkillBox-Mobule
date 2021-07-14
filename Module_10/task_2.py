change = int(input('Введите число: '))
for num in range(1, change + 1):
  for num1 in range(1, change + 1):
    if num >= num1:
      print(num, end = '\t')
  print()
