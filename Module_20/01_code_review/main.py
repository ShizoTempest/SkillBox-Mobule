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

def f(dict):
    lst = []
    length = 0
    for i in dict:
        if dict[i]['interests'] not in lst:
            lst.extend(dict[i]['interests'])
        length += len(dict[i]['surname'])

    return lst, length



print('Список пар «ID студента — возраст»')
for i_key, i_val in students.items():
    print(f'{i_key} - {i_val["age"]}')

my_lst, length = f(students)

print('\nПолный список интересов всех студентов:', my_lst, '\nОбщая длина всех фамилий студентов:', length)
