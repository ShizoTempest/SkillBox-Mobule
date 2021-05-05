count = 0
num = 0
a = int(input('Укажите начало отрезка: '))
b = int(input('Укажите конец отрезка: '))
for number in range(a, b + 1):
  if num % 3 == 0:
    num += number
    count += 1
print('Среднее арифмитическое чисел, подходящее под задачу', num / count)
