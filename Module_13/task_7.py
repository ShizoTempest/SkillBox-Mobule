min_depth = 0
max_depth = 4
danger = float(input('Введите максимально допустимый уровень опасности: '))
depth = min_depth + max_depth / 2
D = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

if danger < 0:
    print('Ошибка.')
else:
    while abs(D) > danger:
        if D > 0:
            min_depth = depth
        else:
            max_depth = depth
        depth = min_depth + (max_depth - min_depth) / 2
        D = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

    print('Приблизительная глубина:', depth)