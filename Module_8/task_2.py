debtor = int(input('Введите кол-во должников: '))
summ = 0
for num in range(0, debtor, 5):
    print('Должник под номером:', num)
    nalog = int(input('Сколько он должен? '))
    summ += nalog
print('Общая сумма долга:', summ)
