Задача 1. Космическая еда
Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться, то у вас будет уходить по 4 килограмма гречки в месяц. Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится. Используйте цикл for.


Задача 2. Долги
МирПрогБанк наконец-то разделил законопослушных граждан и должников и поместил их в разные базы. Но банк не торопится как-то слишком сильно давить на возврат денег. Сейчас операторам банка дали задание позвонить каждому пятому должнику из списка (они нумеруются с нуля) и спросить, сколько примерно денег каждый из них задолжал банку.

Напишите программу, которая принимает на вход количество должников, затем спрашивает у каждого пятого (начиная с 0) его долг. В конце выводится общая сумма долгов.

Пример:

Введите количество должников: 13
Должник с номером 0
Сколько должны? 1000
Должник с номером 5
Сколько должны? 5000
Должник с номером 10
Сколько должны? 2000
Общая сумма долга: 8000

Задача 3. Это будет бомба
Мы разрабатываем пошаговую игру по мотивам боевика. Игрок - главный герой и должен обезвредить бомбу, которая взорвётся через N секунд. Программа спрашивает пользователя хочет ли он обезвредить бомбу сейчас. Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается. Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”, а если не достиг, то программа вновь переспрашивает, не хочет ли игрок обезвредить бомбу, и сообщает, сколько времени осталось до взрыва.. Если ответ “да”, то программа выводит на экран сообщение о том, что бомба обезврежена и сколько секунд оставалось до взрыва. Используйте цикл for.


Задача 4.
Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу c.


Задача 5. Функция 2
В прошлый раз мы написали Саше программу, которая считает функцию в каждой точке отрезка и выводит значение на экран. Но теперь ему нужно, чтобы значения считались в обратном порядке. Плюс к этому в программе ему нужно сделать так, чтобы можно было настраивать шаг, с которым он скачет по точкам отрезка.

Напишите программу, которая получает на вход начало и конец отрезка, а также шаг. Затем высчитывает функцию игрек в каждой точке отрезка и с нужным шагом, начиная с конца, и выводит ответ на экран.

Сама функция выглядит так:


Пример:

Введите начало отрезка: -2
Введите конец отрезка: 2
Введите шаг: -1
В точке 2 функция равна 9
В точке 1 функция равна 0
В точке 0 функция равна 1
В точке -1 функция равна 6
В точке -2 функция равна 9

Задача 6. Письмо
У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги, которое не помещается в конверт. Напишите программу, которая подскажет сколько раз нужно сложить письмо пополам, чтобы оно поместилось в конверт. Размеры письма вводятся с клавиатуры.


Задача 7. Стипендия
Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца. Составьте программу расчета суммы денег, которую необходимо получить у родителей один раз в начале обучения, чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.


Задача 8. Сумма ряда
Дано натуральное число N. Напишите программу для вычисления следующей суммы ряда (начиная с единицы)



Задача 9. Выражение
Дано число x. Напишите программу для вычисления следующего выражения



Задача 10. Кинотеатр
X мальчиков и Y девочек пошли в кинотеатр и купили билеты на подряд идущие места в одном ряду. Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам, чтобы рядом с каждым мальчиком сидела хотя бы одна девочка, а рядом с каждой девочкой — хотя бы один мальчик.

На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y. В ответе выведите какую-нибудь строку, в которой будет ровно X символов “B” (обозначающих мальчиков) и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи. Пробелы между символами выводить не нужно. Если рассадить мальчиков и девочек согласно условию задачи невозможно, выведите строку “Нет решения”.

Пример 1:

Введите кол-во мальчиков: 5
Введите кол-во девочек: 5
Ответ: BGBGBGBGBG
Пример 2:

Введите кол-во мальчиков: 5
Введите кол-во девочек: 3
Ответ: BGBGBBGB
Пример 3:

Введите кол-во мальчиков: 100
Введите кол-во девочек: 1
Ответ: Нет решения