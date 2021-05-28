second = int(input('Сколько секунд до взрыва? '))
for time in range(second, 0, -1):
    change = ('Хотите обезвредить бомбу? (1 - да, 0 - нет): ')
    if change == 1:
        print('Бомба обезврежена!')
        print('Секунд до взрыва:', time)
    elif change == 0:
        print('Жалко...')
    elif time == 0:
        print('Бомба взорвалась!')
