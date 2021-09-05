n = int(input('Введите целое положительное число: '))
summ = []
for i in range(n + 1):
    if i % 2 != 0:
        summ.append(i)

print('Список:', summ)
