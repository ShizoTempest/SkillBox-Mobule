def tpl_sort(key):
    list_num = list(key)
    for num in list_num:
        if str(num).count('.') >= 1:
            return ()
        else:
            list_num.sort()
            list_num = tuple(list_num)
            return list_num

print(tpl_sort((6, 3, -1, 8.5, 4, 10, -5)))

# TODO не работает условие для дробных чисел (кортеж все равно сортируется). Почитай про функцию sorted() и не переводи
#  без нужды все в список.
#  Чтобы не использовать цикл для проверки каждого значения почитай про функцию all()
#  4 и 5 строки - не принимаются здесь. Используй либо type(), либо isinstance()
