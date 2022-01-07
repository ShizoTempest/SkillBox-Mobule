def histogram(text):
    list_dict = dict()
    for symbol in text:
        if symbol in list_dict:
            list_dict[symbol] += 1
        else:
            list_dict[symbol] = 1
    return list_dict

def invert_hist(dict_text):
    new_dict = {}
    for symbol in dict_text:
        if new_dict.get(dict_text[symbol]) == None:
            new_dict[dict_text[symbol]] = []
        new_dict[dict_text[symbol]].append(symbol)
    return new_dict

text = input('Введите текст: ')
hist = histogram(text)

for symbol in sorted(hist.keys()):
    print(symbol, ':', hist[symbol])

print('\nИнвертированный словарь частот:')
new_dict = invert_hist(hist)
for key in new_dict:
    print(key, ':', new_dict[key])
