def test(list_user, user):
    new_list = []
    for i, j in list_user.items():
        if user in i:
            new_list.append(i)
            new_list.append(j)
    return new_list

phonebook = {}
while True:
    print('\nТекущий словарь контактов: \n')
    for name, phone_num in phonebook.items():
        print(f'{name}: {phone_num}')

    chose = int(input('\nВведите номер действия:\n1. Добавить контакт'
                      '\n2. Найти человека'))

    if chose == 1:
        name_surname = input('имя и фамилию нового контакта (через пробел): ')
        if not name_surname in phonebook:
            phonebook[name_surname] = int(input('Введите номер телефона: '))
        else:
            print('Такой человек уже есть')
    elif chose == 2:
        search = input('Введите фамилию для поиска: ')
        answer = test(phonebook, search)
        if len(answer) == 0:
            print('Список пуст')
        else:
            print(answer)
