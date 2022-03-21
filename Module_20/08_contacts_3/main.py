phonebook = {}

while True:
    if len(phonebook) > 0:
        print('\nТекущий словарь контактов:', phonebook)

    chose = int(input('\nВведите номер действия:\n1. Добавить контакт'
                      '\n2. Найти человека\n'))

    if chose == 1:
        name_surname = input('имя и фамилию нового контакта (через пробел): ')
        if not name_surname in phonebook:
            name_surname = name_surname.split()
            NS = tuple(name_surname)
            phonebook[NS] = int(input('Введите номер телефона: '))
        else:
            print('Такой человек уже есть')
    elif chose == 2:
        search = input('Введите фамилию для поиска: ')
        new_list = []
        for i, j in phonebook.items():
            if search in i:
                new_list.append(i)
                new_list.append(j)
        if len(new_list) == 0:
            print('Список пуст')
        else:
            print(new_list)


