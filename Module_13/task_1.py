import math

while True:
    num = float(input('Введите число: '))
    if num > 0:
        break
    elif num < 0 or num == 0:
        print('Ошибка. Число должно быть либо больше нуля, либа больше десяти.')

if num > 10 and num == math.floor(num):
    num = math.floor(num)

if num > 0 and num < 10:
    num = str(num)
    len_num = len(num)
    num = float(num)
    print('Формат плавающей строки: x =', num * 10 ** (len_num - 3), '* 10 **', (len_num - 3) * -1)

elif num != math.floor(num):
    num = str(num)
    len_num = len(num) - 1
    num = float(num)
    print('Формат плавающей строки: x =', num * 10 ** ((len_num - 3) * -1), '* 10 **', (len_num - 3))

elif num == math.floor(num):
    num = str(num)
    len_num = len(num)
    num = float(num)
    print('Формат плавающей строки: x =', num * 10 ** ((len_num - 1) * -1), '* 10 **', len_num - 1)
