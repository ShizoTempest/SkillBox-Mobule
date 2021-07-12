a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
с = int(input('Введите кратность: '))
summ = 0
count = 0
if a > b:
  a, b = b, a
for num in range(a, b + 1):
    if num % с == 0:
        summ += num
        count += 1
print(f'Среднее арифметическое чисел, кратных {с}: {summ / count}')

#Зачтено
