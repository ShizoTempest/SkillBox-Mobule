word = 0
num_count = 0
for number in range(0, 10):
    num = int(input('Введите число: '))
    if num % 2 == 0 and num > 0:
        num_count += 1
        print('Число совпадающее по критериям:', num)
    else:
        print('Число не совпадающее по критериям:', num)
    word += 1
print('Общая количество чисел, которые подошли:', num_count)

# зачтено
