s = list('I' * int(input('Кол-во палок: ')))
for i in range(1, int(input('Кол-во бросков: ')) + 1):
    for j in range(int(input(f'Бросок {i}. Сбиты палки с номера ')) - 1, int(input('по номер '))):
        s[j] = '.'
print('Результат:', ''.join(s))