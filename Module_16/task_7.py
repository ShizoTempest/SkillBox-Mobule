count = int(input('Сколько коньков: '))
high_list = []
for i in range(count):
    high = int(input(f'Введите размер {i + 1} коньков: '))
    high_list.append(high)
print()
people = int(input('Кол-во людей: '))
summ = 0
for j in range(people):
    high = int(input(f'Размер ноги {j + 1} человека: '))
    for k in high_list:
        if high == k:
            summ += 1
            high_list.remove(k)
print('\nНаибольшее кол-во людей, которые могут взять ролики:', summ)


# TODO: Для текущих входных данных программа работает некорректно:
"""
Сколько коньков: 2
Введите размер 1 коньков: 41
Введите размер 2 коньков: 44

Кол-во людей: 3
Размер ноги 1 человека: 41
Размер ноги 2 человека: 41
Размер ноги 3 человека: 41

Наибольшее кол-во людей, которые могут взять ролики: 1
"""

#  По условию люди могут брать коньки на сколько угодно размеров больше, а не только свой

