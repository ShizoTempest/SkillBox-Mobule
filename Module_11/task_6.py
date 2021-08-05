while True:
  down = int(input('Введите нижнюю границу: '))
  up = int(input('Введите верхнюю границу: '))
  step = int(input('Шаг: '))
  if down >= up:
    print('Ошибка ввода. Низ должен быть меньше верха')
  else:
    break

print('\t', 'C\t', ' \t', 'F\t')

for num in range(down, up + 1, step):
  result = round(num * 1.8 + 32, 0)
  print('\t', num, ' \t', result)
  if num + step > up and num != up:
    result = round(up * 1.8 + 32, 0)
    print('\t', up, ' \t', result)
