St_year = int(input('Введите начало года: '))
En_year = int(input('Введите конец года: '))
if St_year > En_year:
    St_year, En_year = En_year, St_year
print()

print(f'Годы от {St_year} до {En_year} с тремя одинаковыми цифрами:')
for count in range(St_year, En_year + 1):
    count= str(count)
    len_num = len(count)
    for score in range(10):
        score = str(score)
        revert = count.count(score)
        if revert == 3:
            print(count)
            break
