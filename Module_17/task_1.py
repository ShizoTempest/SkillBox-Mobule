text = input('Введите текст: ')
word_list = 'аеёийоуыэюя'
list_text = []
for i in text:
    for j in word_list:
        if i == j:
            list_text.append(j)
            break
print("Список гласных букв:", list_text)
print('Кол-во их:', len(list_text))
