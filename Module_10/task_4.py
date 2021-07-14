count = 10

for num in range(count):

  for num1 in range(count):
    if num == num1 or num == count - 1 - num1:
      print('^', end = '')
    else:
      print(' ', end = '')
  print()
