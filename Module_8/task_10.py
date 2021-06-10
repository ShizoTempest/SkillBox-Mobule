boy = int(input('Введите количество мальчиков: '))
girl = int(input('Введите количество девочек: '))
result = boy / girl
sit_down, bg = '', ''
while True:
  if result < 0.5 or result > 2:
    print('Нет решения')
    break
  elif result > 1: #мальчиков больше
    bg = 'BGB'
  else:# девочек больше или равно
    bg = 'GBG'
    boy, girl = girl, boy
  while boy != girl:
    sit_down += bg
    boy -= 2
    girl -= 1
  bg = 'BG'
  for i in range(1, boy+1):
    sit_down += bg
  print(sit_down)
  break

  # Неверно. При входных данных я получаю неверный ответ.
  # Введите количество мальчиков: 5
  # Введите количество девочек: 5
  # GBGGBGGBGGBGGBG

# зачтено
