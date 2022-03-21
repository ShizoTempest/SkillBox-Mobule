def tpl_sort(key):
    if all([True if isinstance(x, int) else False for x in key]):
        key = tuple(sorted(key))
        return key
    return key

print(tpl_sort((6, 3, -1, 8.5, 4, 10, -5)))
