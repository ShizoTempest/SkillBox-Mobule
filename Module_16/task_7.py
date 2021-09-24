count = int(input('Сколько коньков: '))
high_list = []
for i in range(count):
    high = int(input(f'Введите размер {i + 1} коньков: '))
    high_list.append(high)
print()
people = int(input('Кол-во людей: '))
summ = 0
for j in range(people):
    high = int(input(f'Размер ноги {j - 1} человека: '))
    for k in high_list:
        if high == k:
            summ += 1
            high_list.remove(k)
print('\nНаибольшее кол-во людей, которые могут взять ролики:', summ)
