def tpl_sort(key1, key2, key3, key4, key5, key6, key7):
    list_num = []
    list_num.append(key1)
    list_num.append(key2)
    list_num.append(key3)
    list_num.append(key4)
    list_num.append(key5)
    list_num.append(key6)
    list_num.append(key7) #хер знает, как по другому
    for num in list_num:
        if str(num).count('.') >= 1:
            return ()
        else:
            list_num.sort()
            list_num = tuple(list_num)
            return list_num

print(tpl_sort(6, 3, -1, 0.5, 4, 10, -5))


# TODO Передавай в функцию кортеж, а не неопределенное количество аргументов.
#  Затем работай с кортежем, а не со списком. Тут не нужны никакие преобразования.
#
