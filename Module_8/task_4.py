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
print('Общее кол-во кратностей:', summ)

#Решение неверное.
#1. Ошбика в диапазоне итераций цикла.
#2. Нет проверки ввода пользователя. Вдруг он введет первое число больше, чем второе?
#3. Условие проверки кратности никак не связанно с вводимым пользователем числом
#4. Среднее арифметическое считается неверно.