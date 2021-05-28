a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
с = int(input('Введите кратность: '))
summ = 0
for num in range(a, b):
    if num // 3 == 0:
        summ += 1
print('Общее кол-во кратностей:', summ)