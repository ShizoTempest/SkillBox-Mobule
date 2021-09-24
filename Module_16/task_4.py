guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    count = len(guests)
    print('Сейчас на вечеринке', count, 'человек:', guests)
    chose = input('Гость пришел или ушел? ')
    if chose == 'Пора спать' or chose == 'пора спать':
        break
    people = input('Имя гостя: ')
    flag = False
    for i in guests:
        if people == i and chose == 'ушел':
            flag = True
            break
        if people == i and chose == 'пришел' and count < 6:
            flag = True
            break
    if flag == True and chose == 'пришел':
        print('Ошибка ввода, такой человек уже есть.')
        continue
    elif flag == False and chose == 'ушел':
        print('Такого человека нет в списке')
        continue
    elif count == 6 and chose == 'пришел':
        print('На вечеринке уже есть 6 человек.')
        continue
    if chose == 'ушел':
        guests.remove(people)
    elif chose == 'пришел':
        guests.append(people)


# TODO Не выводится итоговое сообщение, когда все ложатся спать

