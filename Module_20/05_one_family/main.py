family = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Кто-то', 'Что-то'): 12
}

chose = input('Введите фамилию: ')

for sur_name in family:
    if chose.lower() != sur_name[0].lower():
        if sur_name[0].lower() == sur_name[0] + 'а'.lower() and chose.lower() == sur_name[0] + 'а'[:-1].lower() or chose[:-1].lower() in sur_name[0].lower():
            print(sur_name[0], sur_name[1], family[sur_name])
    else:
        print(sur_name[0], sur_name[1], family[sur_name])
<<<<<<< HEAD
=======

# зачтено
>>>>>>> main
