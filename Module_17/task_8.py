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


# TODO не надо запрашивать у с какого по какой номер сбиты палки. Здесь должно быть рандомное число,
#  пользователь вводит только количество палок и количество бросков

# PS - Shizo: Не-ет, повторю.
# В восьмом не может быть рандомное число, в таком случае и бросков тоже должно быть N. А это не соответствует оформлению
