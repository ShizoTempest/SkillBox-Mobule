while True:
    num = input('Введите экспанцианальную строку: ')
    if num.count('e') == 1 and num.count('-') == 1 and num.count('e-') == 1 and (num.count('.', 0, 2) == 1 and num.count('.') == 1):
        if num[num.index('-')+1:].isdigit() == True and num[0].isdigit() == True:
            break
        else:
            print('Не придуривайся дибил, читай.')
    elif num.count('e', 0, 2) == 1 and num.count('-') == 1 and num.count('e-') == 1 and (
            num.count('.', 0, 2) < 1 and num.count('.') < 1):
        if num[num.index('-')+1:].isdigit() == True and num[0].isdigit() == True:
            break
        else:
            print('Не придуривайся дибил, читай.')
    else:
        print('Косоглазый, научись читать')

ind = num.find('e')
ind1 = num.rfind('e')
print('Мантиса:', num[:ind])
print('Порядок:', num[ind1:])
