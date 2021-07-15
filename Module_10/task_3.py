lenth = int(input('Введите длину: '))
width = int(input('Введите ширину: '))

for num in range(1, lenth+1):

    for j in range(1, width+1):
        if num == 1 or num == lenth:
            print('-', end = '')
        elif j == 1 or j == width:
            print('|', end = '')
        else:
            print(' ', end = '')
    print()

#зачтено
