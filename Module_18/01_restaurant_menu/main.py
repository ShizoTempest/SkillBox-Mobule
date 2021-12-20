menu = input('Доступное меню: ')
list_menu = menu.split(';')
answer_menu = ''
len_menu = len(list_menu)
for word in list_menu:
    if word == list_menu[len_menu - 1]:
        answer_menu += word
        continue
    answer_menu += word + ', '
print('На данный момент в меню есть:', answer_menu)
