count_nums = 3
count_list = 4

new_list = [ list(range(x, x + count_list * (count_nums - 1) + 1, count_list)) for x in range(1, count_list + 1) ]

print(new_list)

# намудрил много, можно сделать гораздо проще: new_list = [[x + i for x in range(1, 10, 4)] for i in range(4)]

# зачтено
