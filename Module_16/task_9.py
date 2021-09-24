count_friends = int(input('Сколько друзей? '))
count_receipt = int(input('Сколько расписок? '))
list_receipt = []
for i in range(count_friends):
    nums = [i + 1, 0]
    list_receipt.append(nums)

print()
for j in range(count_receipt):
    print(f'{j + 1} расписка.')
    whose = int(input('Кому? '))
    for_his = int(input('От кого? '))
    summ = int(input('Сколько? '))
    for element_F in list_receipt:
        for element_S in element_F:
            if whose == element_S:
                element_F[1] -= summ
            if for_his == element_S:
                element_F[1] += summ
    print()

print('Баланс друзей')
for general_sum in list_receipt:
    print(f'{general_sum[0]} : {general_sum[1]}')
