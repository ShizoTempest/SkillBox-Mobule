five, four, three = 0, 0, 0
schoolboy = int(input('Сколько учеников в классе? '))
for num in range(1, schoolboy + 1):
  print('Ученик:', num)
  score = int(input('Какую оценку он получил? '))
  if score == 5:
    five += 1
    print('Он получил пять.')
  elif score == 4:
    four += 1
    print('Он получил четыре.')
  elif score == 3:
    three += 1
    print('Он получил три.')
if five > four and five > three:
  print('Больше всего в классе пятёрок')
elif four > five and four > three:
  print('Больше всего в классе четверок')
elif five == four == three:
  print('В классе оценок поровну')
elif five == four and five > three and four > three:
  print('В классе пятёрок и четворок поровну, троек меньше всего.')
elif five < four and five < three and four == three:
  print('В клссе троек и четвёрок поровну, пятерок меньше всего.')
elif five > four and five == three and four < three:
  print('В классе пятерок и троек поровну, четверок меньше всего.')
elif five == four and five > three and four > three:
  print('Пятерок поровну с четверками')
elif four == three and five < three and four > five:
  print('Троек поровну с четврерками')
elif three == five and five > four and four < three:
  print('Пятерок поровну с тройками')
else:
  print('Больше всего в классе троек')

# Принту из 4 строки нужно больше информативности
# Программа работает неверно: на входных данных 5 учеников и с оценками 5,5,4,4,3 - выдает, что троек
# больше всего