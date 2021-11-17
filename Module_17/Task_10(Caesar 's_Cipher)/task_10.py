word = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
text = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))
text = [j for j in text]
count = 0

for i in text:
    if i == ' ':
        count += 1
        continue
    word_step = word.index(i)
    if word_step + (step - 1) > len(word):
        text[count] = word[word_step + (step - 1) - len(word)]
        count += 1
        continue
    text[count] = word[word_step + (step - 1)]
    count += 1

ready_text = ''
for j in text:
    ready_text += j
print('Зашифрованое сообщение:', ready_text)
