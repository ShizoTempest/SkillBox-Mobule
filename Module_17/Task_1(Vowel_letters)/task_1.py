text = input('Введите текст: ')
world_list = 'аеёиоуыэюя'

list_text =[symbol for symbol in text if symbol in world_list]

print('Список гласных букв', list_text)
print('Кол-во их:', len(list_text))

# зачтено