import math

hour = 30
min = 360
a = float(input('Введите отклонение часовой стрелки, в градусах: '))
optical = (a / hour - math.floor(a / hour)) * 30 * min / hour # В случае ломки мозга, удали и заново реши эту строчку
print('Минутная стрелка повернулась на', optical, 'градусов')

# зачтено
