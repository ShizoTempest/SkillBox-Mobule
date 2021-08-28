def NOD():
    cycle = True
    while cycle:
        first = int(input('Введите первое число: '))
        second = int(input('Введите второе число: '))
        if first < second:
            first, second = second, first
            cycle = False
        elif first == second:
            print('Ошибочка. Числа должны быть разными.')
        elif first > second:
            cycle = False
    cycle = True
    while cycle:
        num = second
        second = first % second
        first = num
        if second == 0:
            print('НОД этих чисел:', num)
            break
        print(num, first, second)

NOD()