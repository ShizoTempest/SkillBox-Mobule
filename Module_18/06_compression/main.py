text = 'aaAAbbcaaaA'
second_text = ' '
num = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        num += 1
    if text[i] != text[i + 1] or i == len(text) - 2:
        second_text += text[i] + str(num)
        num = 1
if text[-2] != text[-1]:
    second_text += text[-1] + '1'

print(second_text)


# зачтено
