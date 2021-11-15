import random
s = list('I' * int(input('Кол-во палок: ')))
count = len(s)

for i in range(1, int(input('Кол-во бросков: ')) + 1):
    num = random.randint(1, count)
    num_end = random.randint(num, count)
    print(f'Бросок {i}. Сбиты палки с номера', num)
    print('по номер', num_end)
    for j in range(num - 1, num_end):
        s[j] = '.'

print('Результат:', ''.join(s))


# Зачтено
