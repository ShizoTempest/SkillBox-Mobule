films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
like_film = []
like_flag = False

word = ''
while word != 'end':
    word = input('Введите любимый фильм: ')
    count = 0
    for i in like_film:
        like_flag = False
        if word == i:
            like_flag = True
            break
    if like_flag:
        print('Данный фильм уже имеется в вашем списке.')
        continue
    for i in films:
        flag = False
        if word == i:
            like_film.append(i)
            flag = True
            break
        if count == len(films) - 1 and flag == False:
            print('Ошибка, такого фильма нет.')
        count += 1
print('Фильмы которые вы предпочитаете:', like_film)
