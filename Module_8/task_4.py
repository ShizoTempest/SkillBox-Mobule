a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
с = int(input('Введите кратность: '))
summ = 0
count = 0
if a > b:
  a, b = b, a
for num in range(a, b):
    if num % с == 0:
        summ += num
        count += 1
print('Общее кол-во кратностей:', summ / count)

#Решение неверное.
#1. Ошбика в диапазоне итераций цикла не исправлена.
#2. Информационное уведомление принта не соответствует условию задачи.
#   Общее количество кратностей - это не среднее арифметическое их значений.
