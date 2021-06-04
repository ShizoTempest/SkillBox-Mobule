while True:
  x = int(input('Введите число X от 1 до 6, которые не равнялось n во 2 степени: '))
  up = 1
  down = 1
  for num in range(1, 7):
    up *= (x - (2 ** num - 1))
    down *= (x - 2 ** num)
  if down == 0:
    print('Попробуйте снова. Ошибка в воде')
  else:
    break
print('Ответ:', up / down)