range_list = int(input('Введите длину списка: '))

list_num = [x % 5 if x % 2 else 1 for x in range(range_list)]

print(list_num)
