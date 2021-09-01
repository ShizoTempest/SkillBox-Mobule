def repeat(word):
    len_word = len(word)
    word = int(word)
    summ = ''
    for count in range(1, len_word + 1):
        word_rage = word % 10
        word = word // 10
        word_rage = str(word_rage)
        summ += word_rage
    return summ

def recording(num):
    num = str(num)
    rage_num = num.find('.')
    roge_num = num.rfind('.')
    F_path = num[rage_num + 1:]
    S_path = num[:roge_num]
    F_path = repeat(F_path)
    S_path = repeat(S_path)
    total = S_path + '.' + F_path
    total = float(total)
    return total

F_num = float(input('Введите первое число: '))
S_num = float(input('Введите второе число: '))

f_flag = True
s_flag = True

if F_num < 0:
    F_num *= -1
    f_flag = False
if S_num < 0:
    S_num *= -1
    S_flag = False

F_total = recording(F_num)

S_total = recording(S_num)

score = str(S_total)
score = score.rfind('.')
score1 = str(F_total)
score1 = score1.rfind('.')
point = max(score, score1)

if f_flag == False:
    F_total *= -1
if s_flag  == False:
    S_total *= -1

print('Первое число наоборот:', F_total)
print('Второе число наоборот:', S_total)

print('Сумма:', round(F_total + S_total, point))
