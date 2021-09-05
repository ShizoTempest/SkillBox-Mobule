word = input('Введите слово: ')
list_word = list(word)
count = 1
flag = 'false'
for i in list_word:
    if i != list_word[count * -1]:
        flag = 'true'
        break
    count += 1
if flag == 'false':
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
