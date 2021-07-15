count = 0
count_sequnces = int(input('Введите кол-во чисел в последовательности: '))

while count_sequnces > 0:
    count_sequnces -= 1
    point = 0
    num = int(input('Введите само число в последовательности: '))

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            point += 1
    if point == 1:
        count += 1
print('Простых чисел в последовательности:', count)

#зачтено

