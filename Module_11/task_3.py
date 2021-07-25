exept = float(input('Укажите размер файла: '))
speed = float(input('Какова скорость загрузки: '))
end = 0
second = 1
while end <= exept:
    print('Прошло', second, 'сек. Скачано', end, 'из', exept, 'МБ "', round(end / exept * 100, 0) ,'% ".')
    end += speed
    second += 1
print('Прошло', second, 'сек. Скачано', exept, 'из', exept, 'МБ " 100 % ".')
