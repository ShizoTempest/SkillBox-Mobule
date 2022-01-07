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

count = int(input())
main_tree = {}

for _ in range(1, count):
    line = input()
    child, parent = line.split()
    main_tree[child] = parent

all_tree = set(main_tree.keys()) | set(main_tree.values())
heights = {}

for name in all_tree:
    if name not in heights:
        revert(name)

for name in sorted(heights):
    print(name, heights[name])
