num = int(input('Сколько пар слов? '))
pair_lst = []
for count in range(num):
    pair = input(f'{count + 1} пара слов(через дефис): ').lower()
    pair_set = set(pair.split(' - '))
    pair_lst.append(pair_set)
print()

while True:
    word = input('Введите слово: ').lower()
    count = 0
    for elem in pair_lst:
        if word.lower() in elem:
            new = elem - {word}
            print('Синоним:', str(*new).capitalize())
            count += 1
    else:
        if count < 1:
            print('Такого слова в словаре нет.')
            count += 1
