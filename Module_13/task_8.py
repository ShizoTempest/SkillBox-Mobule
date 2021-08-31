while True:
  precision = float(input('Введите точность: '))
  if precision < 0:
    print('Ошибка ввода')
  else:
    break
x = float(input('Введите x: '))

count_num = 1
jump = 0
znak = -1
result = 1

while abs(count_num) > precision:
    jump += 2
    Difference = 1
    private = 1
    for numbers in range(1, jump + 1):
        Difference *= x
        private *= numbers
    count_num = znak * Difference / private
    znak *= -1
    result += count_num

print('Сумма ряда =', result)
