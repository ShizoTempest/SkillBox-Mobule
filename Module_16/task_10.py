def is_palindrome(num_list):
    reverse_list = []
    for i in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i])
    if num_list == reverse_list:
        return True
    else:
        return False
num = [1, 2, 3, 4, 5]
F_list = []
S_list = []
for j in range(0, len(num)):
    for l in range(j, len(num)):
        F_list.append(num[l])
    if is_palindrome(F_list):
        for k in range(0, j):
            S_list.append(num[k])
        S_list.reverse()
        break
    F_list

print('Исходный список:', num)
print('Нужно чисел для палиандрома:', len(S_list))
print('Список этих чисел:', S_list)
