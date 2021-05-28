number = 0
for number in range(10, 100):
  if number == number // 10 * number % 10 * 3:
    print(number)
