def tpl_sort(key):
    list_num = list(key)
    for num in list_num:
        if str(num).count('.') >= 1:
            return ()
        else:
            list_num.sort()
            list_num = tuple(list_num)
            return list_num

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
