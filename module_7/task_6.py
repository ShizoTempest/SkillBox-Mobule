five, four, three = 0, 0, 0
schoolboy = int(input('Сколько учеников в классе? '))
for num in range(1, schoolboy + 1):
  print(num)
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
if five > four and five> three:
  print('Больше всего в классе пятёрок')
elif four > five and four > three:
  print('Больше всего в классе четверок')
elif five == four == three:
    print('В классе оценок поровну')
else:
  print('Больше всего в классе троек')
