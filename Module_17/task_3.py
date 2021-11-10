import random

Third_list = []
first_comand = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
print('Первая команда:', first_comand)
second_comand = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
print('Вторая команда:', second_comand)

count = 0
for i in first_comand:
    for j in second_comand:
        if i > second_comand[count]:
            Third_list.append(i)
        elif i <= second_comand[count]:
            Third_list.append(second_comand[count])
        break
    count += 1

print('Список победителей:', Third_list)

# TODO не использовано понимание списка. Переделай с list comprehensions
