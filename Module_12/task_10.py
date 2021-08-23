def kitchen():
  print('Вы на кухне. Окно - 1, Коридор - 2')
  choice = int(input('Куда пойдем? '))
  if choice == 1:
    print('先輩, будьте осторжны... \nОй, вы же меня не слышите...\nот вас только и осталось, что глазки да мозги)')
  elif choice == 2:
    hallway()
  else:
    print('Ошибочка.')
    kitchen()

def bedroom():
  print('Вы в спальне. Ванная - 1, Коридор - 2')
  choice = int(input('Куда пойдем? '))
  if choice == 1:
    bathroom()
  elif choice == 2:
    hallway()
  else:
    print('Ошибочка.')
    bedroom()

def bathroom():
  print('Вы в ванной. Коридор - 1, Спальня - 2')
  choice = int(input('Куда пойдем? '))
  if choice == 1:
    hallway()
  elif choice == 2:
    bedroom()
  else:
    print('Ошибочка.')
    bathroom()

def hallway():
  print('Вы в коридоре. Спальня - 1, Ванная - 2, Кухня - 3, Дверь - 4')
  choice = int(input('Куда пойдем? '))
  if choice == 1:
    bedroom()
  elif choice == 2:
    bathroom()
  elif choice == 3:
    kitchen()
  elif choice == 4:
    print('Квартира покинута... \nНо конец ли это?.. \nВас не покидает чувство того, что вы все еще не одни...')
  else:
    print('Ошибочка.')
    hallway()

print('Квест начался.\n  Задача:\nПокинуть квартиру.')
bedroom()

# принято