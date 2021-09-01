while True:
    num = int(input('Введите число: '))
    if num < 0:
        print('Число должно быть положительным.')
    else:
        break
num = str(num)
len_num = len(str(num))
num = int(num)

summ = 0
for count in range(1, len_num + 1):
    rage_num = num % 10
    num = num // 10
    summ += rage_num
print('Сумма цифр:', summ)
print('Кол-во цифр в числе:', len_num)
print('Разность суммы и кол-во цифр:', summ - len_num)
