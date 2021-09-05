count = int(input('Введите кол-во чисел в списке: '))
num_list = []

for _ in range(count):
    num = int(input('Введите число в списке: '))
    num_list.append(num)
print('Изначальный список:', num_list)

for i1 in range(count):
    for i in range(i1 + 1, count):
        if num_list[i] < num_list[i1]:
            num_list[i1], num_list[i] = num_list[i], num_list[i1]
print('Отсортированный список:', num_list)
