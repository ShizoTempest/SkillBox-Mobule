goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key in goods:
    id_item = goods[key]
    summ = 0
    summ_item = 0
    for dct in store[id_item]:
        summ += dct['quantity'] * dct['price']
        summ_item += dct['quantity']
    print(f'{key} - {summ_item} шт, стоимость {summ} руб')

# принято
