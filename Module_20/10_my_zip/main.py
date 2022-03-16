def input_user():
    while True:
        word = input('Введите строку: ')
        word = list(word)
        print('Пример: (10, 20, 30, 40)')
        num_tuple = input('Кортеж чисел: ')
        num_tuple = num_tuple[1:-1]
        num_tuple = list(num_tuple.split(', '))
        if len(word) != len(num_tuple):
            print('Длина строки и кортежа чисел не равна.')
        else:
            break
    return word, num_tuple

word, num_tuple = input_user()

new_zip = zip(word, num_tuple)
print(new_zip)
new_zip = list(new_zip)

for elem in range(len(word)):
    print(new_zip[elem])
