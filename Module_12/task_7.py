def MinNumber(num1, num2):
  MinNumber = (num1 + num2) / 2 - (abs(num1 - num2)) / 2
  print('Минимальное число:', MinNumber)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

MinNumber(a, b)

# принято
