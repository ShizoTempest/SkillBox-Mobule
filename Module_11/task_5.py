import math

rad = float(input('Введите радиус планеты: '))
v = 4 / 3 * math.pi * rad ** 3
earth = 10.8321 * 10 ** 11

if earth >= v:
    result = round(earth / v, 3)
    print('Объём планеты Земля больше в', result)
else:
    result = round(v / earth, 3)
    print('Объём планеты Земля меньше в', result)

# зачтено