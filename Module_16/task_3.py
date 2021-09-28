shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
len_list = len(shop)
name_scrap = input('Название детали: ')
summ = 0
count_item = 0
len_for = 0

for i in shop:
    flag = False
    for j in i:
        if flag == True:
            summ += j
        if j == name_scrap:
            count_item += 1
            flag = True
    if count_item > 0:
        flag = True

    len_for += 1

    if len_for == len_list and flag == True:
        print('Кол-во таких вещей:', count_item)
        print('Общая стоимость:', summ)
        break
    elif len_for == len_list and flag != True:
        print('Такой вещи нет')
        break
