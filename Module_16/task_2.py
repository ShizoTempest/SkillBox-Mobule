F_class = []
S_class = []
sum_class = []
for i_class in range(160, 176 + 1, 2):
    F_class.append(i_class)
print('Первый класс:', F_class)
for i_class in range(162, 180 + 1, 3):
    S_class.append(i_class)
print('Второй класс:', S_class)
S_class.extend(F_class)
len_class = len(S_class)
for j_class in range(len_class):
    num = max(S_class)
    sum_class.append(num)
    S_class.remove(num)
print('Классы в одной шеренге:', sum_class)


# TODO 1. Ответ выведен неверно. Требовалось вывести учеников в порядке возрастания, а не убывания
# TODO 2. Задача можно решить в 5 строк, без циклов с помощью метода sort(), либо функции sorted()
