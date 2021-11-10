while True:
    text = input('Введите текст: ')
    if text.count('h') != 2:
        print('В тексте нету двух одинаковых букв h')
    else:
        break

start = text.index('h')
end = text.rindex('h')
print(text[:start + 1] + text[end - 1: start - 1] + text[end:])
