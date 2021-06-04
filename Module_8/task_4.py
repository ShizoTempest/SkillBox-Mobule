a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
с = int(input('Введите кратность: '))
summ = 0
count = 0
if a > b: # Для проверки ввода и другой чебушни
  a, b = b, a
for num in range(a, b+1):
  if num % с == 0:
    print('Число из этого отрезка кратность', с, 'на', num)
    summ += num
    count += 1
print('Cреднее арифметическое из суммы всех чисел отрезка:', summ / count)