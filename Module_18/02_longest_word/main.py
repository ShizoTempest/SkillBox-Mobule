first = 'one two three four five six'
line = first.split()
maximum = (line[0])

for i in range(1, len(line)):
    if len(line[i]) > len(maximum):
        maximum = line[i]

print(maximum, len(maximum))

# зачтено
