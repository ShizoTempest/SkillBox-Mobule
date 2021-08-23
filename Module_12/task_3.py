
def MaxNumber(number):
    maxi = 0
    for cicle in str(number):
        if maxi < int(cicle):
            maxi = int(cicle)
    print('Максимальная цифра:', maxi)

def MinNumber(num):
    MinNumber = 9
    for cicle in str(num):
        if MinNumber > int(cicle):
            MinNumber = int(cicle)
    print('Минимальная цифра:', MinNumber)

def summ(num):
    summ = 0
    for count in str(num):
        summ += int(count)
    print('Сумма цифр:', summ)

def base():
    num = abs(int(input('Введите число: ')))
    print('Какое действие выполнить с числом?')
    choice = int(input('Вывести сумму цифр - 1, Вывести максимальную цифру - 2, Вывести минимальную цифру - 3: '))
    if choice == 1:
        summ(num)
        base()
    elif choice == 2:
        MaxNumber(num)
        base()
    elif choice == 3:
        MinNumber(num)
        base()

base()

# принято

