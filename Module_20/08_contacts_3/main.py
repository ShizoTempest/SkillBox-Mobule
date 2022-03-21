<<<<<<< HEAD
phonebook = {}

while True:
    if len(phonebook) > 0:
        print('\nТекущий словарь контактов:', phonebook)

    chose = int(input('\nВведите номер действия:\n1. Добавить контакт'
                      '\n2. Найти человека\n'))
=======
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
>>>>>>> main

    if chose == 1:
        name_surname = input('имя и фамилию нового контакта (через пробел): ')
        if not name_surname in phonebook:
<<<<<<< HEAD
            name_surname = name_surname.split()
            NS = tuple(name_surname)
            phonebook[NS] = int(input('Введите номер телефона: '))
=======
            phonebook[name_surname] = int(input('Введите номер телефона: '))
>>>>>>> main
        else:
            print('Такой человек уже есть')
    elif chose == 2:
        search = input('Введите фамилию для поиска: ')
<<<<<<< HEAD
        new_list = []
        for i, j in phonebook.items():
            if search in i:
                new_list.append(i)
                new_list.append(j)
        if len(new_list) == 0:
            print('Список пуст')
        else:
            print(new_list)


# зачтено
=======
        answer = test(phonebook, search)
        if len(answer) == 0:
            print('Список пуст')
        else:
            print(answer)

# TODO 1. Формат вывода НЕ соответствует примеру. Работа телефонной книги должна быть реализована с помощью составных
#  ключей.
#  2. Приглашение на ввод должно осуществляться с новой строки, а не сбоку возле уже выведенного приглашения.
#  3. Основной функционал (действия) НЕ описан в отдельных функциях. Что за посторонний код в 1-7 строках?!

# Что тебя смущает в 1 - 7 строке? Мне дала мысль автора, когда искал похожую задачу.
>>>>>>> main
