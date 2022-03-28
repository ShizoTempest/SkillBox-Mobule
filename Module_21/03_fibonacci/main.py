def fobinichi(num):
    Second_num = 0
    if num == 0:
        return Second_num
    else:
        return fobinichi(num - 1)

def fonb():
    First = 0
    Second = 1
    while (True):
        summ = First + Second
        yield summ #Завтра поменяй, если не разберешься
        Second = First
        First = Second

generet_fibi = fonb()

num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))

for i in range(num_pos + 1):
    if i == num_pos - 1:
        print(next(generet_fibi)) #Во втором задействуй
    else:
        next(generet_fibi)
