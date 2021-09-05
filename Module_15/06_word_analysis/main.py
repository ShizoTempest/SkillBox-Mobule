word = input('Введите слово: ')
word = list(word)
summ = 0
for i in word:
    count = 0
    for i1 in word:
        if i == i1:
            count += 1
    if count == 1:
        summ += 1

print('Уникальных букв:', summ)
