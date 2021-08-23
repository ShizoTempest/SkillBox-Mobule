import random

def rock_paper_scissors(): #Камень, ножницы и бумага
  Сrandom = random.randint(1, 3)
  print('Камень - 1, Ножницы - 2, Бумага - 3')
  YourChoice = int(input('Сделайте выбор: '))

  if Сrandom == YourChoice:
    print('Ничья')
  elif YourChoice < 1 or YourChoice > 3:
    print('Ошибочка, 先輩')
    rock_paper_scissors()
  elif Сrandom - YourChoice == 1 or Сrandom - YourChoice == -2:
    print('Ваша взяла 先輩')
  else:
    print('Удача не ваш конек 先輩')

def guess_the_number(): #УгАдАй ЧиСлО
  Crandom = random.randint(0, 10)
  user_choice = int(input('Отгадайте число от 0 до 10: '))

  if Crandom == user_choice:
    print('Верно 先輩')
  else:
    print('Не верное 先輩, у меня', Crandom)
    guess_the_number()

def main(): #Меню
  print('Камень, ножницы, бумага - 1, Угадай число - 2')
  choice = int(input('Выберете игру: '))

  if choice == 1:
    rock_paper_scissors()
  elif choice == 2:
    guess_the_number()
  else:
    print('Ошибочка')
    main()

main()

# принято

