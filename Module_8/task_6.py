size1 = int(input('Введите размер письма: '))
size = 12
count = 0
while size < size1:
    size1 /= 2
    print('Нынешний размер письма:', size1)
    count += 1
print('Надо сложить письмо', count, 'раз.')
