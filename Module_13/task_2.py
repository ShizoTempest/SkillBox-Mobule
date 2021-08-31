def maximum(a, b):
    return ((a + b) / 2) + abs((a - b) / 2)

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

d = maximum(a, b)

print('Максимальное число:', maximum(c, d))
