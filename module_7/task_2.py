word = 0
num_count = 0
num = int(input('Введите число: '))
while word < 10:
    num = int(input('Введите число: '))
    if num % 2 and num > 0:
        num_count += 1
        print('Число совподающее по кретериям:', num)
    else:
        print('Число не совподающее по кретериям:', num)
    word += 1
print('Общая сумма чисел, которые подошли:', num_count)
