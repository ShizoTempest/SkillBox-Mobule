violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
count = int(input('Сколько песен выбрать? '))
summ = 0
num = []
for i in range(count):
    flag = False
    while True:
        chose = input(f'Название {i + 1} песни: ')
        for j in violator_songs:
            if j.index(0) == chose:
                num = j
                flag = True
                break
        if flag == True:
            break
        else:
            print('Ошибка, такой песни нет.')
    summ += num.index(1)
print('Общее время звучания песен:', round(summ, 2))


# TODO Выдает сразу ошибку:
#  Сколько песен выбрать? 3
#  Название 1 песни: Halo
#  Traceback (most recent call last):
#   File "C:/Users/Amadu/PycharmProjects/Shizo/SkillBox-Mobule/Module_16/task_5.py", line 20, in <module>
#     if j.index(0) == chose:
#     ValueError: 0 is not in list

