count = int(input('Введите кол-во чисел: '))
maxium = 0
while count > 0:
  count -= 1
  summ = 0

  while True:
    num = int(input('Ведите натуральное число: '))
    if num < 1:
      print('Ошибочка. Попытайтесь снова.')
    else:
      break

  for num1 in str(num):
    summ += int(num1)
  if summ > maxium:
    maxium = summ
    num2 = num

print('Наибольшее число из суммы цифр:', num2, ', его сумма:', maxium)
