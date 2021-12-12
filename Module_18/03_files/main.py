file = input('Введите имя файла: ')

if not file.endswith('.txt' or '.docx'):
    print('Ошибка: неверное расширение файла')
elif file.startswith(' @№$%^&*()'):
    print('Ошибка:недопустимый символ')
else:
    print('Файл назван верно')
