# Лабораторная работа № 5 «Вычисление формул с кванторами»

import csv

with open("stud.csv") as file:
    csv_file = csv.reader(file, delimiter=";")
    header = next(csv_file, None)  # пропустить заголовки
    data_str = [row for row in csv_file]
# список data_str содержит списки значений признаков в каждой строке

data_size = len(data_str)  # число наблюдений
num_cols = len(data_str[0])  # число столбцов (общее число признаков)

# data_x - список списков из атрибутов, расположенных в каждой строке файла
data_x = [[] for _ in range(data_size)]
for i in range(data_size):
    data_x[i] = data_str[i].copy()
x_len = num_cols  # число входных признаков
x_names = header[:]  # имена входных признаков

print("Наблюдений:", data_size)
print("Входных признаков:", x_len)
print(x_names)
print()

############################################

print("Правда ли, что все студенты старше 2 курса старше 18 лет?")
val = True  # значение высказывания
for i in range(data_size):  # перечисляем строки таблицы, i - индекс строки
    # проверяем, нарушает ли i-й студент квантор общности
    # если нарушает, то присвоим значению высказывания val = False
    age_str = data_x[i][0]  # столбец с возрастом имеет индекс 0
    if age_str[0:5] == 'более':
        age_num = 23
    elif age_str[0:5] == 'менее':
        age_num = 16
    else:
        age_num = int(age_str[0:2])
    course_str = data_x[i][1]  # столбец с курсом имеет индекс 1
    # здесь мы обратились к элементу таблицы data_x в строке i в столбце 1
    if course_str[2:6] == 'курс':
        course_num = int(course_str[0])
        if course_num > 2:
            val = val and (age_num > 18)
            print("Найден студент:", data_x[i])
print("Ответ:", val)
print()


print("Правда ли, что все студенты старше 1 курса старше 18 лет?")
val = True  # значение высказывания
# Задание 1
# Ответьте на поставленный вопрос, выведите строки, нарушающие квантор общности
# Для вывода i-й строки используйте оператор print(data_x[i])
for i in range(data_size):
    age_str = data_x[i][0]  # Столбец с возрастом
    course_str = data_x[i][1]  # Столбец с курсом
    # Определяем возраст
    if age_str[0:5] == 'более':
        age_num = 23
    elif age_str[0:5] == 'менее':
        age_num = 16
    else:
        age_num = int(age_str[0:2])
    # Определяем курс
    if course_str[2:6] == 'курс':
        course_num = int(course_str[0])
        # Проверяем условие для студентов старше 1 курса
        if course_num > 1:
            if age_num <= 18:
                val = False
                print("Нарушение:", data_x[i])

print("Ответ:", val)
print()


print("Правда ли, что найдутся студенты бакалавриата, которым менее 17 лет?")
val = False  # значение высказывания
for i in range(data_size):
    # проверяем, удовлетворяет ли i-й студент условию квантора существования
    # если удовлетворяет, то присвоим значению высказывания val = True
    age_str = data_x[i][0]
    if age_str[0:5] == 'более':
        age_num = 23
    elif age_str[0:5] == 'менее':
        age_num = 16
    else:
        age_num = int(age_str[0:2])
    course_str = data_x[i][1]  # столбец с курсом имеет индекс 1
    if 'бакалавриат' in course_str:
        val = val and (age_num == 16)
        print("Нарушение:", data_x[i])

print("Ответ:", val)
print()


print("Правда ли, что найдется студент, которому 21 год и который имеет стаж работы от 2 до 3 лет?")
val = False  # значение высказывания
# Задание 2
# Ответьте на поставленный вопрос, выведите строки, удовлетворяющие условию квантора существования
# Для вывода i-й строки используйте оператор print(data_x[i])

for i in range(data_size):
    age_str = data_x[i][0]  # Столбец с возрастом
    work_exp_str = data_x[i][3]  # Столбец с общим стажем работы
    # Определяем возраст
    if age_str[0:5] == 'более':
        age_num = 23
    elif age_str[0:5] == 'менее':
        age_num = 16
    else:
        age_num = int(age_str[0:2])
    # Проверяем стаж работы
    if '2 до 3 лет' in work_exp_str:
        if age_num == 21:
            val = True
            print("Найден студент:", data_x[i])

print("Ответ:", val)