import random


max_num = int(input('Введите максимальное число: '))
change_num = str(random.randint(1, max_num))
nums = set([str(i) for i in range(int(change_num) + 1)])
nums.remove('0')
print()

while True:
    answer_user = input('Нужное число есть среди вот этих чисел: ')
    if answer_user == 'Помогите!':
        print('Артём мог загадать следующие числа:', *sorted(nums), '\n')
        continue
    answer_user = set(answer_user.split())
    if answer_user == {change_num} and len(answer_user) == 1:
        print('Ответ Артёма: Ты угадал!')
        break
    elif change_num in answer_user:
        print('Ответ Артёма: Да\n')
        nums = nums & answer_user
    else:
        nums = nums - answer_user
        print('Ответ Артёма: Нет\n')

# TODO Выдает ошибку сортировки
