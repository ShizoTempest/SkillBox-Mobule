debtor = int(input('Введите кол-во должников: '))
summ = 0
for num in range(0, debtor, 5):
    print('Должник под номером:', num)
    nalog = int(input('Сколько он должен? '))
    nalog += summ
print('Общая сумма долга:', summ)
# При любом исходе: Общая сумма долга: 0
# Проверяй задачи перед сдачей.