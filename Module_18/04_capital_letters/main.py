def capitalize(line):
    answer = ' '.join([s.capitalize() for s in line.split()])
    return answer

text = input('Введите текст: ')
print(capitalize(text))


# зачтено
