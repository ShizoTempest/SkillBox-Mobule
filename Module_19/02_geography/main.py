count_country = int(input('Введите кол-во стран: '))
country_dict = {}
for num in range(count_country):
    while True:
        city = input(f'{num + 1} страна и 3 города: ').split()
        if len(city) != 4:
            print('Ошибка ввода, ожидается 4 аргумента.')
        else:
            break
    country_dict[city[0]] = city[1:]
print()

for city in range(3):
    flag = False
    name_city = input(f'{city + 1} город: ')
    for key in country_dict:
        if name_city in country_dict.get(key):
            print(f'Город {name_city} расположен в стране {key}\n')
            flag = True
    if flag == False:
        print(f'По городу {name_city} данных нет.')

# принято
