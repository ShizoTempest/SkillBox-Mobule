file = input('Введите имя файла: ')

if not file.endswith('.txt' or '.docx'):
    print('Ошибка: неверное расширение файла')
elif file.startswith('@' or '№' or '$' or '%' or '^' or '&' or'*' or '(' or')'):
    print('Ошибка:недопустимый символ')
else:
    print('Файл назван верно')


# TODO ошибка с первого же примера
# Введите имя файла: @example.txt
# Файл назван верно
#

