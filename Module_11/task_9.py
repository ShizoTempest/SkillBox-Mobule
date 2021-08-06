import math

while True:
  num = float(input('Введите число(кроме 0): '))
  if num != 0:
    break
  else:
    print('Ошибочка! Читай внимательнее!')

num1 = float(input('Введите действ. число: '))
num2 = float(input('Введите действ. число: '))

result = num1 ** 2 - 4 * num * num2

while result >= 0:
  krat = (- num1 + math.sqrt(num1 ** 2 - 4 * num * num2)) / 2 * num
  krat1 = (- num1 - math.sqrt(num1 ** 2 - 4 * num * num2)) / 2 * num
  if krat == krat1:
    print(krat)
  else:
    print(krat, krat1)
  break

# зачтено
