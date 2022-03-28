def min_len(words, symbol):
    return min(len(words), len(symbol))

word = input('Введите строку: ')
print('Пример: (10, 20, 30, 40)')
num_tuple = input('Кортеж чисел: ')
num_tuple = num_tuple[1:-1]
num_tuple = tuple(num_tuple.split(', '))

pairs = ((word[counter], num_tuple[counter]) for counter in range(min_len(word, num_tuple)))
print(pairs)
