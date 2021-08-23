def count_letters():
    text = input('Введите текст: ')
    count1 = 0
    count2 = 0
    num = int(input('Какую цифру ищем? '))
    bukva = input('Какую букву ищем? ')
    for soul in text:
        if str(num) == soul:
            count1 += 1
        elif bukva == soul:
            count2 += 1
    print('Количество цифр', str(num) + ':', count1)
    print('Количество букв', bukva + ':', count2)

count_letters()

# принято

