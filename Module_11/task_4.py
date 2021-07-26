import math

num = float(input('Введите любое положительное число: '))
num = abs(num) #Не делал, если бы ты не бугуртил постоянно
print(math.floor((num - math.floor(num)) * 10))

# Принято.
