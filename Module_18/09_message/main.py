def revert(a, b):
    return b, a

def revers_text(sentence):
    list_text = [i for i in sentence.split(" ")]
    Result = ""
    for string in list_text:
        string = [x for x in string]
        len_string = len(string) - 1
        num = 0
        while num < len_string:
            if not (string[num].isalpha() or string[num].isdigit()): #Вслучае не измениния текста, изменить
                num += 1
            elif not (string[len_string].isalpha() or string[len_string].isdigit()):
                len_string -= 1
            else:#Возможно лишнее
                string[num], string[len_string] = revert(string[num], string[len_string])
                num += 1
                len_string -= 1
        result = "".join(string)
        Result += (result+" ")
    return Result

text = input('Сообщение: ')

print('Новое сообщение:', revers_text(text))
