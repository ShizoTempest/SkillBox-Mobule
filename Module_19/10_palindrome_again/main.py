def palindrom(symbols):
    dict_symbol = {}
    for sym in symbols:
        dict_symbol[sym] = dict_symbol.get(sym, 0) + 1
    count = 0
    for value_sym in dict_symbol.values():
        if value_sym % 2 != 0:
            count += 1
    return count <= 1

text = input('Введите строку: ')
if palindrom(text):
    print('Можно сделать полиндром.')
else:
    print('Нельзя сделать полиндром.')
