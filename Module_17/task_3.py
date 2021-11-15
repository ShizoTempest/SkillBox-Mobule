import random

Third_list = []
first_comand = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
print('Первая команда:', first_comand)
second_comand = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
print('Вторая команда:', second_comand)

Third_list = [(second_comand[count] if first_comand[count] <= second_comand[count] else first_comand[count]) for count in range(20)]

print('Список победителей:', Third_list)

# TODO не использовано понимание списка. Переделай с list comprehensions
