def correct_word1(first_n, num_count):
    first_num_count = 0
    temp = first_n
    while temp > 0:
        first_num_count += 1
        temp = temp // 10
    if first_num_count < num_count:
        print("В первом числе меньше трёх цифр.")
    last_digit = first_n % 10
    first_digit = first_n // 10 ** (first_num_count - 1)
    between_digits = first_n % 10 ** (first_num_count - 1) // 10
    first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
    return first_n

first_n = int(input("Введите первое число: "))

first_n = correct_word1(first_n, 3)

print('Изменённое первое число:', first_n)

second_n = int(input("\nВведите второе число: "))

second_n = correct_word1(second_n, 4)

print('Изменённое второе число:', second_n)

print('\nСумма чисел:', first_n + second_n)
