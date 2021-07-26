import math

count = int(input('Введите кол-во чисел: '))
amount = 0

while count != amount:
    num = float(input('Введите число: '))
    if num > 0:
        enter = math.ceil(num)
        print('x =', enter, 'log(x) =', math.log(enter))
    else:
        enter = math.floor(num)
        print('x =', enter, 'exp(x) =', math.exp(enter))
    amount += 1

# зачтено
