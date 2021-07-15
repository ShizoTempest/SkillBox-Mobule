num = int(input('Введите число: '))
summ = 0
factor = 1

for count in range(1, num + 1):
  factor *= count
  print(factor)
  summ += factor

print('Сумма факториалов числа', num , ':', summ)


#зачтено
