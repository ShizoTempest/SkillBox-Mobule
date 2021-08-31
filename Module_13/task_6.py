while True:
    start_amplit = float(input('Введите начальную амплитуду: '))
    stop_amplit = float(input('Введите амплитуду остановки: '))
    if stop_amplit > start_amplit:
        start_amplit, stop_amplit = stop_amplit, start_amplit
        break
    else:
        break

percent = start_amplit * 8.4 / 100

count = 0
while start_amplit > stop_amplit:
    start_amplit -= start_amplit * 8.4 / 100
    count += 1
print('Маятник считается остановившимся через', count, 'колебаний.')
