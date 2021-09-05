count = int(input('Кол-во видеокарт сейчас? '))
num_max = 0
list_video = []
new_list_video = []

for i1 in range(count):
    num = int(input(f'{i1 + 1} Введите номер видео карты: '))
    if num > num_max:
        num_max = num
    list_video.append(num)
for i in list_video:
    if num_max != i:
        new_list_video.append(i)

print(f'Старый список видеокарт: {list_video}\nНовый список видеокарт: {new_list_video}')
