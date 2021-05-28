lost = 0
num = int(input('Введите число карточек: '))
full = num
for card in range(1, num):
  print('Введите номер карточки от 1 до', num)
  card_number = int(input())
  lost += card_number
  full += card
card1 = full - lost
print('Номер потерянной карточки:', card1)
