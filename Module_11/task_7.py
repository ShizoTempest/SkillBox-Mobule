import math
# * - Возможно ошибка
while True:
    print('Введите местоположение коня')
    HorisHorse = float(input('По горизонтали: '))
    VerticHorse = float(input('По вертикали: '))

    if HorisHorse < 0 or VerticHorse < 0 or HorisHorse > 0.8 or VerticHorse > 0.8:
        print('Клетки с такой координатой не существует.')
    else:
        break

while True:
    print('Введите местоположение точки на доске')
    x = float(input('По горизонтали: '))
    y = float(input('По вертикали: '))
    if x < 0 or y < 0 or x > 0.8 or y > 0.8:
        print('Клетки с такой координатой не существует.')
    else:
        break

x = int(x * 10)
y = int(y * 10)
HorisHorse = int(HorisHorse * 10)
VerticHorse = int(VerticHorse * 10)
print('Конь на (', str(HorisHorse), ',', str(VerticHorse), ')')#*
print('Сейчас она на (', str(x), ',', str(y), ')')#*
OptionHoris = abs(HorisHorse - x)
OptionVertic = abs(VerticHorse - y)

if OptionHoris == 1 or OptionVertic == 2 or OptionHoris == 2 or OptionVertic == 1:#*
    print('Да, конь может хоть в эту точку')
else:
    print('Нет, конь не может ходить в эту точку')

# зачтено
