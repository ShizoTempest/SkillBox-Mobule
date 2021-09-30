def incom(count):
    list_a = []
    for i in range(count):
        num = int(input('Введите число: '))
        list_a.append(num)
    return list_a
F_list = incom(3)
print('\nПервый список:', F_list)
print()
S_list = incom(7)
print('\nВторой список:', S_list)
F_list.extend(S_list)
for i in F_list:
    count = 0
    for j in F_list:
        if j == i:
            count += 1
    if count >= 2:
        for _ in range(count - 1):
            F_list.remove(i)
print('Новый первый список с уникальными элементами:', F_list)


# зачтено
