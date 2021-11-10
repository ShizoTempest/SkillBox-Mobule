import random

first = [random.randint(-5, 5) for i in range(random.randint(10, 20))]
print(first)

second = [i for i in first if i]
print(second)
