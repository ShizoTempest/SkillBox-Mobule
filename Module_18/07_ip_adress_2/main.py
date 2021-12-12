IP = input('Введите IP: ')
answer_ip = IP.split('.')
ip_num_count = 0

if len(answer_ip) < 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    for range_ip in range(len(answer_ip)):
        if answer_ip[range_ip].isdecimal() == False:
            print(f' {answer_ip[range_ip]} - не целое число')
            ip_num_count += 1
            continue
        if int(answer_ip[range_ip]) > 255:
            ip_num_count += 1
            print(f' { answer_ip[range_ip] } превышает 255')

if ip_num_count == 0:
    print('IP-адрес корректен')
