# count_order = int(input('Введите кол-во заказов: '))
# order_dict = {}
# for num in range(count_order):
#     order = input(f'{num + 1} заказ(Имя, Пицаа, кол-во): ')
count_order = int(input('Введите кол-во заказов: '))
order_dict = {}
for num in range(count_order):
    order = input(f'{num + 1} заказ(Имя, Пицаа, кол-во): ')
    name, pizza, amount = order.rsplit(maxsplit=3)
    amount = int(amount)
    if name not in order_dict:
        order_dict[name] = {pizza: amount}
    else:
        if pizza not in order_dict[name]:
            order_dict[name] |= {pizza: amount}
        else:
            order_dict[name][pizza] += amount
for name, order in sorted(order_dict.items()):
    print(f'{name}:')
    for pizza, amount in sorted(order.items()):
        print('    ', pizza, amount)


# TODO ошибка при вводе условия из примера
