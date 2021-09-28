def mini(list_num, number):
    t = 0
    for i in list_num:
        if i == number:
            t += 1
    print(f'Кол-во цифр {number} при первом объединении:', t)
    return t
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
t = mini(a, 5)
for _ in range(t):
    a.remove(5)
a.extend(c)
t = mini(a, 3)
print('Итоговый список:', a)


# TODO рефакторинг не произведен. Сделай замену первого и последнего цикла методами.
# Неверно. Я сказал заменить циклы методами, а не засунуть циклы в функцию
