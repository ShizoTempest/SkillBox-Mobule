count_num = int(input('Введите кол-во чисел в списке: '))
space = int(input('Сдвиг: '))

num_list = []
new_num_list = []

for _ in range(count_num):
    num = int(input('Введите число для списка: '))
    num_list.append(num)

for i in range(count_num):
    if count_num - space + i <= count_num - 1:
        new_num_list.append(num_list[count_num - space + i])
    else:
        new_num_list.append(num_list[i - space])
print('Старый список:', num_list)
print('Новый список:', new_num_list)
