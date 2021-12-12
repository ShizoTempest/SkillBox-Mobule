line_1 = list(input('Первая строка: '))
line_2 = list(input('Вторая строка: '))
count = len(line_1)
answer = 0

for i in range(count):
    num = []
    for j in range(count):
        num += line_1[(i + j) % count]
    if num == line_2:
        print('Первая строка получается из второй со сдвигом ',  i)
        answer += 1
        break
if answer == 0:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

# TODO Необходимо было получить число в случае возможности получения первой строки из второй, а не показывать список
