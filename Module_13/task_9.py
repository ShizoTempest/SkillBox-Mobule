def sequence(i, n, s, k):
    a = k * s
    for year in range(1, n + 1):
        print('Период:', year)
        print('Остаток долга на начало периода:', round(s, 2))
        print('Выплаченно процентов:', round(s * i / 100, 2))
        print('Выплаченно тела кредита:', round(a - s * i / 100, 2))
        s -= a - s * i / 100
    print('Остаток долга:', round(s, 2))
    return s
    pass

def end(n, i):
    con = i / 100 * (1 + i / 100) ** n
    con1 = ((1 + i / 100) ** n - 1)
    k = con / con1
    return k
    pass

s = float(input('Введите сумму кредита: '))
n = int(input('На сколько лет выдан: '))
i = float(input('Сколько процентов годовых: '))

k = end(n, i)
s = sequence(i, n - 2, s, k)

print('\n====================\n')

year_con = int(input('На сколько лет продляется договор: '))
quar = float(input('Увеличение ставки до: '))

k = end(year_con + n - (n - 2), quar)
sequence(quar, year_con + n - (n - 2), s, k)