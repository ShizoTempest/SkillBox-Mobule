def tpl_sort(key):
    if all(key):
        key = sorted(key)
        list_num = tuple(key)
        return list_num
    else:
        return ()

print(tpl_sort((6, 3, -1, 8.5, 4, 10, -5)))
