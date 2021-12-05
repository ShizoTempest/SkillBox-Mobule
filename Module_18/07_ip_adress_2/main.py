IP = input('Введите IP: ')
answer_ip = IP.split('.')
first_count = 0
second_count = 0

if len(answer_ip) < 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    for i in range(len(answer_ip)):
        if answer_ip[i].isdigit():
            second_count += 1
        if int(answer_ip[i]) > 255:
            first_count += 1
            print(f' { answer_ip[i] } превышает 255')
        else:
            print(f' { answer_ip[i] } - не целое число')

if first_count == 0 and second_count == 4:
    print('IP-адрес корректен')


# TODO Ошибка на первом же примере
# Введите IP: 128.16.35.a4
#  128 - не целое число
#  16 - не целое число
#  35 - не целое число
# Traceback (most recent call last):
#   File "C:/Users/Amadu/PycharmProjects/Shizo/SkillBox-Mobule/Module_18/07_ip_adress_2/main.py", line 12, in <module>
#     if int(answer_ip[i]) > 255:
# ValueError: invalid literal for int() with base 10: 'a4'
