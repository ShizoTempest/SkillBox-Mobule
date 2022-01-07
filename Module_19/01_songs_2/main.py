violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_songs = int(input('Сколько песен хотите выбрать? '))
summ_minutes = 0
for num in range(count_songs):
    while True:
        song = input(f'Название {num + 1} песни: ')
        if violator_songs.get(song):
            break
        else:
            print('Ошибка: такой песни нет.')
    summ_minutes += violator_songs[song]
print('Общее время звучания песен:', round(summ_minutes, 2), 'минут')
