import random


list_num = [random.randint(0, 40) for i in range(10)]
new_list = []
for elem in list_num:
    new_list.append(tuple(elem, list_num[1]))
