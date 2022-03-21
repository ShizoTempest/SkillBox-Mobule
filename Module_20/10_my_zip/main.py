# def shortest(iter_1, iter_2):
#     return min(len(iter_1), len(iter_2))
#
#
# def iterable(iter):
#     if isinstance(iter, (str, list, dict, tuple)):
#         return True
#     else:
#         print('Предоставлен неитерируемый объект')
#     return False
#
#
# def input_answer(answer):
#     if answer == 'строка':
#         data = input('Введите любой текст: ')
#     elif answer == 'список':
#         data = input('Введите текст через пробел: ').split()
#
#     elif answer == 'словарь':
#         data_dict = input('Введите текст через пробел в формате ключ-значение: ').split()
#         # data = {data[i]: data[i+1] for i in range(0, len(data), 2)}
#         # выкидываем значения
#         data = [data_dict[i] for i in range(0, len(data_dict) + 1, 2)]
#
#     elif answer == 'кортеж':
#         data = tuple(input('Введите текст через пробел: ').split())
#     if iterable(data):
#         return data
#
#
# object_set = {'строка', 'список', 'словарь', 'кортеж'}
# while True:
#     answer = input('Выберите первый тип объекта: строка, список, словарь, кортеж: ').lower()
#     if answer in object_set:
#         data_1 = input_answer(answer)
#         break
# while True:
#     answer = input('Выберите второй тип объекта: строка, список, словарь, кортеж: ').lower()
#     if answer in object_set:
#         data_2 = input_answer(answer)
#         break
#
# pairs = ((data_1[index], data_2[index]) for index in range(shortest(data_1, data_2)))
# print(pairs)
# for index in pairs:
#     print(index)

def min_len(words, symbol):
    return min(len(words), len(symbol))

word = input('Введите строку: ')
print('Пример: (10, 20, 30, 40)')
num_tuple = input('Кортеж чисел: ')
num_tuple = num_tuple[1:-1]
num_tuple = tuple(num_tuple.split(', '))

pairs = ((word[counter], num_tuple[counter]) for counter in range(min_len(word, num_tuple)))
print(pairs)

for element in pairs:
    print(element)

