# Лабораторная работа № 2 «Дизъюнктивные нормальные формы»

# возвращает таблицу истинности по кортежу значений функции 3 переменных
def truth_table_by_vec(v):
    assert(len(v) == 8)
    tt = {}
    i = 0
    for A in range(2):
        for B in range(2):
            for C in range(2):
                tt[A, B, C] = v[i]
                i += 1
    return tt

#v_maj = (0, 0, 0, 1, 0, 1, 1, 1)
#tt = truth_table_by_vec(v_maj)

# возвращает таблицу истинности по заданной функции 3 переменных
def truth_table_by_func(f):
    tt = {}
    for A in range(2):
        for B in range(2):
            for C in range(2):
                tt[A, B, C] = f(A, B, C)
    return tt

# def f_maj(x, y, z):
#     return x and y or x and z or y and z
#
# def f(x, y, z):
#     return y | z & ~x

#tt = truth_table_by_func(f_maj)
# tt = truth_table_by_func(f)
# print(tt)


# принимает на вход таблицу истинности и выдает строку с СДНФ
def fdnf(tt):
   return ' | '.join(map(conj_str, [key for key in tt if tt[key]]))

# принимает на вход кортеж значений переменных и выдает элементарную конъюнкцию с такими степенями переменных
def conj_str(vars):
    var_names = ('x', 'y', 'z')
    return '&'.join(map(literal_str, var_names, vars))

# принимает на вход имя переменной (str) и ее степень (bool), возвращает литерал
def literal_str(name, deg):
    if deg:
       return name
    else:
       return '~' + name

# тестирование функции literal_str
#print(literal_str('A', 1))
#print(literal_str('B', 0))

# тестирование функции conj_str
#print(conj_str((0, 1, 0)))

# тестирование функции fdnf
# print(fdnf(tt))

# 1. Тестирование с таблицей значений:
v_func = (0, 0, 0, 1, 1, 0, 1, 1)  # Вектор значений функции
tt_from_vec = truth_table_by_vec(v_func)  # Таблица истинности по вектору
print("Таблица истинности из вектора:")
print(tt_from_vec)

# Построение СДНФ
sdnf_vec = fdnf(tt_from_vec)
print("\nСДНФ по вектору значений:")
print(sdnf_vec)

# 2. Тестирование с булевой функцией:
def f(x, y, z):
    return y | z & ~x

tt_from_func = truth_table_by_func(f)  # Таблица истинности по функции
print("\nТаблица истинности из функции:")
print(tt_from_func)

# Построение СДНФ
sdnf_func = fdnf(tt_from_func)
print("\nСДНФ по функции:")
print(sdnf_func)

# 3. Входная функция на основе СДНФ из предыдущего шага:
def eval_sdnf(x, y, z):
    return eval(sdnf_func) 

# Таблица истинности на основе вычисления СДНФ
tt_from_sdnf = truth_table_by_func(eval_sdnf)

print("\nТаблица истинности на основе СДНФ:")
print(tt_from_sdnf)

# Проверка совпадения исходной и полученной таблиц
if tt_from_func == tt_from_sdnf:
    print("\nИсходная таблица истинности совпадает с таблицей, построенной на основе СДНФ.")
else:
    print("\nТаблицы истинности не совпадают.")
