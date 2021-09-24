human_count = int(input('Сколько человек? '))
num_lost = int(input('Какое число в считалке? '))
print(f'Значит выбывает каждый {num_lost} человек.')
F_num = 0
index = 1
people_list = list(range(1, human_count + 1))
while len(people_list) != 1:
    print('Текущий круг людей:', people_list)
    print('Начало счета с', people_list[index - 1])
    x = num_lost % len(people_list)
    #num_del = people_list.index(people_list[x])
    index = x + index - 1
    print('Выбывает человек под номером', people_list[index - 1])
    people_list.remove(people_list[index - 1])
    #index = num_del
    if index > len(people_list):
        index %= len(people_list)
print('\nОстается человек под номером:', people_list[0])
