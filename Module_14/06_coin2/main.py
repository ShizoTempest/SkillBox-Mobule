import math

def requar(num):
    if num.count('.') == 0:
        num = int(num)
    else:
        num = float(num)
    return num

def point_rea(num1):
    num1 = str(num1)
    if num1.count('.') == 0:
       num1 = True
    else:
        num1 = False
    return num1

print('Введите кординаты монетки:')
x1 = input('X: ')
y1 = input('Y: ')

num1 = point_rea(x1)
x1 = requar(x1)

if num1 != False:
    num1 = point_rea(y1)
    y1 = requar(y1)
else:
    y1 = requar(y1)

while True:
    radius = input('Введите радиус: ')
    radius = requar(radius)
    if radius < 0 or radius < 0.0:
        print('Ошибка ввода, радиус не может быть отрицательным.')
    else:
        break
radius = str(radius)

if num1 != False:
    num1 = point_rea(radius)
    radius = requar(radius)
else:
    radius = requar(radius)

if num1 == True:
    radius = float(radius)
    x1 = float(x1)
    y1 = float(y1)

pifagor = round(math.sqrt(x1 ** 2 + y1 ** 2))

if radius > pifagor:
    print('Монетка где-то поблизости.')
else:
    print('Монетки нет в области.')
