while True:
    num = int(input('Введите число: '))
    if num < 1:
        print('Ошибка ввода. Число должно быть больше 1.')
    else:
        break

count = 0
while True:
    count += 1
    num_del = num / count
    if count != 1 and round(num_del) == num_del:
        print('Наименьший делитель, отличный от единицы:', count)
        break
