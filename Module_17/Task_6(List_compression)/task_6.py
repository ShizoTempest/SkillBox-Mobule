import random

first = [random.randint(-5, 5) for i in range(random.randint(10, 20))]
print(first)

second = [i for i in first if i]

count_zero = first.count(0)
for _ in range(count_zero):
    second.insert(0, 0)
print(second)

second = [i for i in first if i]
print(second)


# TODO не выполнена сортировка списка. Сначала нужно было все нулевые значения переместить в конец массива и только
#  потом удалять их

# Чаво, зачем это делать, если мы их потом удалим, да и не выводим сообщение об этом. Бред так делать.
