def func(num):
  if num != 0:
    newnumber = ''
    for count in str(num):
      newnumber = count + newnumber
    print('Число наоборот', int(newnumber))
  else:
    print('Программа закончена.')

num = True
while num:
  num = abs(int(input('Введите число: ')))
  func(num)

  # принято
