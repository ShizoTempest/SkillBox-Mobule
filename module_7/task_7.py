count = 0
summ = 0
a = int(input('Укажите начало отрезка: '))
b = int(input('Укажите конец отрезка: '))
for number in range(a, b + 1):
  if number % 3 == 0:
    summ += number
    count += 1
print('Среднее арифметическое чисел, подходящее под задачу', summ / count)

#неверно работает. Проверь условие