m, n = 4, 7
for row in range(m):
#  for col in range(n):
  print(' ' * (n // 2 - row), '#' * (n - 2 * (n // 2 - row)), ' ' * (n // 2 - row))
#    break

#Вообще не понял как оно работает