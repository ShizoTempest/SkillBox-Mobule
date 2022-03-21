def slicer(elem, num):
    if len(elem) < 2 or elem.count(num) == 0:
        elem = ()
        return elem
    elif elem.count(num) < 2:
        first_index = elem.index(num)
        elem = elem[first_index:]
        return  elem
    else:
        first_index = elem.index(num)
        second_index = elem.index(num, first_index + 1)
        elem = elem[first_index:second_index + 1]
        return elem

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10, 3), 3))

