while True:
    text = input('Введите текст: ')
    if text.count('h') != 2:
        print('В тексте нету двух одинаковых букв h')
    else:
        break

start = text.index('h')
end = text.rindex('h')
text = text[start + 1: end]
print(text[::-1])


# зачтено
