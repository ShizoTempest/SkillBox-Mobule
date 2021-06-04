month = 0
for grech in range(0, 100, 4):
    if grech >= 4:
        month += 1
        print('В этом месяце останется гречки:', 100 - grech)
        print('Месяц:', month)
    else:
        print('Гречка кончилась!')
