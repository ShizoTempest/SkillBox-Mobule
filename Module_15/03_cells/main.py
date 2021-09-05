count = int(input('Введите кол-во клеток: '))
un_correct = ''

for i in range(count):
    num = int(input(f'Эффективность клетки №{i + 1}: '))
    if num < i + 1:
        num = str(num)
        un_correct += num + ' '
print()
print('Неподходящие числа:', un_correct)
