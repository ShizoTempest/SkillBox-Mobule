count = int(input('Введите кол-во контейнеров: '))
conter = []
prev_num = 0
for i in range(count):
    while True:
        num = int(input('Введите вес контейнера в порядке возрастания: '))
        if num > 200:
            print('Ошибка, вес не должен превышать 200 кг')
        elif prev_num > num:
            print('Контейнер должен быть в порядке возростания.')
        else:
            break
    prev_num = num
    conter.append(num)

print()
new_conter = int(input('Введите вес нового контейнера: '))
print()
len_list = len(conter)

for i1 in range(len_list):
    if new_conter >= conter[i1] and new_conter < conter[i1 + 1]:
        print('Место, куда встанет новый контейнер:', i1)
        break
