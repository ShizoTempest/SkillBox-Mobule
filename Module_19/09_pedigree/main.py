def revert(name):
    if name not in main_tree:
        heights[name] = 0
        return 0
    parent = main_tree[name]
    if parent in heights:
        value = heights[parent] + 1
    else:
        value = revert(parent) + 1
    heights[name] = value
    return value

count = int(input('Введите количество человек: '))
main_tree = {}

while True:
    for i in range(1, count):
        while True:
            line = input(f'{i} пара: ')
            child, parent = line.split()
            if child in main_tree.keys():
                print('Такой человек есть в отцах')
            else:
                break
        main_tree[child] = parent
    flag = False
    for key in main_tree:
        if key == main_tree.get(main_tree[key]):
            print(main_tree[key], main_tree.get(main_tree[key]))
            print('Такого быть не может. Ошибка ввода.')
            main_tree.clear()
            flag = True
            break
    if flag:
        continue

    all_tree = set(main_tree.keys()) | set(main_tree.values())
    heights = {}
    print()

    for name in all_tree:
        if name not in heights:
            revert(name)

    for name in sorted(heights):
        print(name, heights[name])
    break
