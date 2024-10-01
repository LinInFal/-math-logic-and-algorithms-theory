# Лабораторная работа № 3 «Логическое следствие»
import csv

with open("spect.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    header = next(tsv_file, None)  # пропустить заголовки
    data_str = [row for row in tsv_file]
# список data_str содержит списки значений признаков в каждой строке

data_size = len(data_str)  # число наблюдений
num_cols = len(data_str[0])  # число столбцов (общее число бинарных признаков)

# data_x - список списков из атрибутов, расположенных в каждой строке файла
# data_y - список значений выходных признаков для каждой строки
data_x = [[] for _ in range(data_size)]
data_y = [0.0 for _ in range(data_size)]
for i in range(data_size):
    data_x[i] = list(map(int, data_str[i]))  # применяем функцию int к каждому элементу списка
    data_y[i] = data_x[i].pop()  # удаляем из списка data_x[i] последний элемент
x_len = num_cols - 1  # число входных признаков
x_names = header[:-1]  # имена входных признаков

print("Наблюдений:", data_size)
print("Входных признаков:", x_len)
print(x_names)

############################################

# Поиск взаимосвязей между парами признаков
print("\nВзаимосвязи между парами признаков:")
for i in range(x_len):
    for j in range(i + 1, x_len):
        for A in 0, 1:
            for B in 0, 1:
                # считаем, сколько раз i-й признак равен A и j-й признак равен B
                cnt = 0
                for n in range(data_size):
                    if data_x[n][i] == A and data_x[n][j] == B:
                        cnt += 1
                # если такая комбинация не встретилась ни разу, выводим
                if cnt == 0:
                    print(f"{x_names[i]} = {A} -> {x_names[j]} = {B}")

# Поиск взаимосвязей между тройками признаков
print("\nВзаимосвязи между тройками признаков:")
for i in range(x_len):
    for j in range(i + 1, x_len):
        for k in range(j + 1, x_len):
            for A in 0, 1:
                for B in 0, 1:
                    for C in 0, 1:
                        # Считаем, сколько раз встретилась комбинация (i = A, j = B, k = C)
                        cnt = 0
                        for n in range(data_size):
                            if data_x[n][i] == A and data_x[n][j] == B and data_x[n][k] == C:
                                cnt += 1
                        if cnt == 0:
                            print(f"{x_names[i]} = {A}, {x_names[j]} = {B}, {x_names[k]} = {C}")

# Поиск взаимосвязей между одним входным признаком и выходным признаком
print("\nВзаимосвязи между входным признаком и выходным признаком:")
for i in range(x_len):
    for A in 0, 1:
        for B in 0, 1:
            # Считаем, сколько раз встретилась комбинация (i = A и Y = B)
            cnt = 0
            for n in range(data_size):
                if data_x[n][i] == A and data_y[n] == B:
                    cnt += 1
            if cnt == 0:
                print(f"{x_names[i]} = {A} -> Y = {B}")

# Поиск взаимосвязей между парами признаков и выходным признаком
print("\nВзаимосвязи между парами входных признаков и выходным признаком:")
for i in range(x_len):
    for j in range(i + 1, x_len):
        for A in 0, 1:
            for B in 0, 1:
                for C in 0, 1:
                    # Считаем, сколько раз встретилась комбинация (i = A, j = B, Y = C)
                    cnt = 0
                    for n in range(data_size):
                        if data_x[n][i] == A and data_x[n][j] == B and data_y[n] == C:
                            cnt += 1
                    if cnt == 0:
                        print(f"{x_names[i]} = {A}, {x_names[j]} = {B} -> Y = {C}")