summ = 0
n = int(input('Введите число: '))
while n < 1:
    n = int(input('Ошибка. Введите снова: '))
    if n > 1:
        break
for num in range(n + 1):
    summ = (-1) ** num * 1 / 2 ** num
print('Сумма состовляем:', summ)