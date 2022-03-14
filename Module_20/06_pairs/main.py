import random

original = [i for i in range(0, 10)]
print(f"Оригинальный список: {original} ")
result = dict()
for first_key, second_key in enumerate(original):
    if first_key % 2 == 0:
        result[first_key] = second_key

result = [(first_key, second_key + 1) for first_key, second_key in result.items()]
print("Новый список:", result)

# Второй метод, разкаминтируй если надо проверить.
#old_list = [random.randint(0, 40) for _ in range(10)]
#print('Оригинальный список:', old_list)
#new_list = [*map(tuple, zip(old_list[::2], old_list[1::2]))]
#print('Новый список:', new_list)


# зачтено
