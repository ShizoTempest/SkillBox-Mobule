n = int(input('Введите число: '))
for row in range(n):
  dop = ''
  for col in range(n + 1):
    if col <= row:
      print(n - col, end = '')
      dop = str(n - col) + dop
    elif col == n:
      print(dop)
    else:
      print('.', end = '')
      dop = '.' + dop