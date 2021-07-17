change = int(input('Введите число: '))

for num in range(change):
  space = ''
  for num1 in range(change + 1):
    if num1 <= num: #Если считаеться не правильно, повернуть стрелку
      print(change - num1, end = '')
      space = str(change - num1) + space #Для подсета, менять в случае бесконечного высчета
    elif num1 == change:
      print(space)
    else:
      print('.', end = '')
      space = '.' + space

# Зачтено
