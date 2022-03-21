players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

figny = []
for i in players:
    figny.append(i + players[i])

print(figny)


# зачтено. Как вариант можно было бы использовать метод items, а не обращаться снова по индексу к словарю
# figny = [i_key + i_val for i_key, i_val in players.items()] - такой вариант будет более pythonic и предпочтительнее.

