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