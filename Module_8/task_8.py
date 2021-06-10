summ = 0
n = int(input('Введите число: '))
while True:
    n = int(input('Ошибка. Введите снова: '))
    if n < 1:
        print('Ошибочка, не верно введено условие.')
    else:
        break
for num in range(n + 1):
    summ = (-1) ** num * 1 / 2 ** num
print('Сумма составляет:', summ)

# сумма не считается. Результат выводит неверный
# ничего не изменено
