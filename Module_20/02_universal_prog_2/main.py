def is_prime(num):
    flag = True
    for digit in range(2, num - 1):
        if num % digit == 0:
            flag = False
            break
    return flag

def crypto(elem):
    if (isinstance(elem, (list, tuple, set, dict, str))):
        lst = []
        for index, value in enumerate(elem):
            if index == 1 or index == 0:
                continue
            if is_prime(index) == True:
                lst.append(value)
    else:
        print('Нет')
    return lst

print(crypto('О Дивный Новый мир!'))

# зачтено
