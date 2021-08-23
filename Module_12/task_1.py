def point():
  summ = 0
  num = int(input('Введите целое положительное число: '))

  for count in range(1, num + 1):
    summ += count
  print('Сумма всех чисел от 1 до', num, 'включительно:', summ)
point()

# принято

