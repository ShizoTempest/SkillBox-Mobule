students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

<<<<<<< HEAD
def f(human):
    lst = []
    string = ''
    for i in human:
=======
def f(dict):
    lst = []
    string = ''
    for i in dict:
>>>>>>> main
        lst.extend(dict[i]['interests'])
        string += dict[i]['surname']
    cnt = len(string)
    return lst, cnt

pairs = []
for i in students:
    pairs.append((i, students[i]['age']))
print(pairs)

my_lst, l = f(students)
print(my_lst, l)
<<<<<<< HEAD
=======

# зачтено
# dict - зарезервированное имя. Впредь избегай ситуаций и не давай переменным имена функций.
>>>>>>> main
