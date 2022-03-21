import random


old_list = [random.randint(0, 40) for _ in range(10)]
print('Оригинальный список:', old_list)
new_list = [*map(tuple, zip(old_list[::2], old_list[1::2]))]
print('Новый список:', new_list)

# TODO хороший способ, но обрати внимание, что по заданию ты должен был использовать генератор списков.
#  Добавь сюда еще 1 способ.
