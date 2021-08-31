def reverse(num):
    note = False
    if num < 0:
        num *= -1
        note = True
    num = str(num)
    len_num = len(num)
    num = int(num)
    count = 0
    reb_num = ''
    while len_num != count:
        reb_num += str(num % 10)
        num //= 10
        count += 1
    reb_num = int(reb_num)
    if note == True:
        reb_num *= -1
    return reb_num

F_num = int(input('Введите первое число: '))
S_num = int(input('Введите второе число: '))
print()

F_expression = reverse(F_num)
S_expression = reverse(S_num)

print('Первое число наоборот:', F_expression)
print('Второе число наоборот', S_expression)
print('Сумма:', F_expression + S_expression)
print()

F_expression = reverse(F_expression)
S_expression = reverse(S_expression)

print('Сумма наоборот:', F_expression + S_expression)