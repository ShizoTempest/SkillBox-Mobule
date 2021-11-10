import random

first = [random.randint(-5, 5) for i in range(random.randint(10, 20))]
print(first)

second = [i for i in first if i]
print(second)


# TODO не выполнена сортировка списка. Сначала нужно было все нулевые значения переместить в конец массива и только
#  потом удалять их
