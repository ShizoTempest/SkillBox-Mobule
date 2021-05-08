summ = 0
for month in range(12):
  print('Номер месяца:', month + 1)
  while True:
    income = int(input('Какая зарплата в этот месяц: '))
    if income < 0:
      print('Ошибка ввода, зарплата должна быть положительная.')
    else:
      break
  summ += income
summ /= 12
print('Средняя зарплата:', round(summ, 2))

# - Счетчик month - лишний. Цикл for умеет работать без принудительного счетчика,
# также не нужна инициализация этой переменной
# - Совершенно очевидно, что зарплата - положительное число и не может быть меньше нуля.
# Поэтому реализуй дополнительную проверку ввода пользователя, чтобы при вводе отрицательного числа программа
# выдавала ошибку и снова спрашивала число.
# - Ты вводишь числа 12 раз, но легко запутаться в этом меню. Добавь в каждый запрос пользователя № месяца за
# который вводится зарплата.
# - Средняя зарплата за год считается по формуле среднего арифметического. У тебя неверно.
