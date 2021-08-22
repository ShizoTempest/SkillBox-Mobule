def treasure(x, y):
  if abs(x) <= 1 and abs(y) <= 1:
    print('近くのコイン')
  else:
    print('エリア内にコインはありません')

x = float(input('Введите координату Х: '))
y = float(input('Введите координату Y: '))

treasure(x, y)