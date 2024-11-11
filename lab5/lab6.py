from pycryptosat import Solver
import itertools


s = Solver()

cnf = []

"""
ПЕРВОЕ ЗАДАНИЕ
"""
# # индекс переменной x_ij
# # i, j = 1, 2, 3
# # индекс = 1..9
# def vind(s, i, j):
#     assert(s == 'X' or s == 'O')
#     ind = (i - 1) * 8 + j
#     if s == 'O':
#         ind += 9
#     return ind
#
# # добавить дизъюнкт к КНФ
# # vlist - список пар (i, j)
# def add_clause(vlist):
#     l = []
#     for p, i, j, r in vlist:
#         if r == '+':
#             l.append(vind(p, i, j))
#         elif r == '-':
#             l.append(-vind(p, i, j))
#         else:
#             raise ValueError("+ or - expected")
#     s.add_clause(l)
#     cnf.append(l)
#
# # def print_cnf(filename):
# #     with open(filename, 'w') as fout:
# #         print('p cnf', 18, len(cnf), file=fout)
# #         for clause in cnf:
# #             print(" ".join(list(map(str, clause))), file=fout)
#
# inds = range(1, 4)  # индексы клеток
#
# # инициализация игрового поля
# field = [['.' for _ in range(0, 4)] for _ in range(0, 4)]
#
# # игровая ситуация
# # field[1][1] = 'X'
# # field[1][3] = 'O'
# # field[2][1] = 'O'
# # field[3][3] = 'X'
#
# # 1 Задание - крестики и нолики сделали по 2 хода. Теперь ходят крестики. Смогут ли они выиграть за один ход? Введите
# # булевы переменные и запишите формулу алгебры логики для ответа на вопрос. Затем преобразуйте формулу к КНФ и введите в
# # SAT-солвер
# # игровая ситуация
# field[1][1] = 'X'
# field[1][2] = 'O'
# field[2][1] = 'O'
# field[2][2] = 'X'
#
# # вывод поля
# for i in inds:
#     for j in inds:
#         print(field[i][j], end='')
#     print()
#
# # 1. В одной и той же клетке не может одновременно находиться X и O
# for i in inds:
#     for j in inds:
#         add_clause([('X', i, j, '-'), ('O', i, j, '-')])
#
# # 2. Укажем, какие клетки заняты
# for i in inds:
#     for j in inds:
#         if field[i][j] == 'X':
#             add_clause([('X', i, j, '+')])
#         elif field[i][j] == 'O':
#             add_clause([('O', i, j, '+')])
#
# # 3. Ход X производится в одну клетку
# for i in inds:
#     for j in inds:
#         if field[i][j] == '.':
#             for k in inds:
#                 for l in inds:
#                     if (i, j) != (k, l) and field[k][l] == '.':
#                         add_clause([('X', i, j, '-'), ('X', k, l, '-')])
#
# # 4. В свободных клетках нет O
# for i in inds:
#     for j in inds:
#         if field[i][j] == '.':
#             add_clause([('O', i, j, '-')])
#
# # 5. Выигрыш, если три X стоят в одной горизонтали, вертикали или диагонали
#
# # Автоматически приведем условие выигрыша из ДНФ к КНФ
# # dnf = [[(1, 1), (1, 2), (1, 3)], [(2, 1), (2, 2), (2, 3)], [(3, 1), (3, 2), (3, 3)],
# #        [(1, 1), (1, 2), (1, 3)], [(1, 2), (2, 2), (3, 2)], [(1, 3), (2, 3), (3, 3)],
# #        [(1, 1), (2, 2), (3, 3)], [(1, 3), (2, 2), (3, 1)]]
# dnf = [
#     # Горизонтальные линии
#     [(1, 1), (1, 2), (1, 3)],
#     [(2, 1), (2, 2), (2, 3)],
#     [(3, 1), (3, 2), (3, 3)],
#     # Вертикальные линии
#     [(1, 1), (2, 1), (3, 1)],
#     [(1, 2), (2, 2), (3, 2)],
#     [(1, 3), (2, 3), (3, 3)],
#     # Диагонали
#     [(1, 1), (2, 2), (3, 3)],
#     [(1, 3), (2, 2), (3, 1)]
# ]
# dnf_len = len(dnf)
# # генерируем кортежи длины 8 из элементов 0, 1, 2
# for seq in itertools.product([0, 1, 2], repeat=dnf_len):
#     clause = []
#     for p in range(dnf_len):
#         i, j = dnf[p][seq[p]]
#         clause.append(('X', i, j, '+'))
#     add_clause(clause)
#
# # print_cnf("cnf.txt")
#
#
# sat, solution = s.solve()
# #print(sat)
# #print(solution)
#
# if not sat:
#     print('Нет решения')
# else:
#     new_field = [['.' for _ in range(0, 4)] for _ in range(0, 4)]
#     for i in inds:
#         for j in inds:
#             if solution[vind('X', i, j)]:
#                 new_field[i][j] = 'X'
#             elif solution[vind('O', i, j)]:
#                 new_field[i][j] = 'O'
#
#     # вывод поля
#     print("Решение:")
#     for i in inds:
#         for j in inds:
#             print(new_field[i][j], end='')
#         print()

"""
ВТОРОЕ ЗАДАНИЕ
"""
# определение индексов для ферзей
def vind(s, i, j):
    assert (s == 'Q')
    return (i - 1) * 8 + j

# добавить дизъюнкт к КНФ
# vlist - список пар (i, j)
def add_clause(vlist):
    l = []
    for p, i, j, r in vlist:
        if r == '+':
            l.append(vind(p, i, j))
        elif r == '-':
            l.append(-vind(p, i, j))
        else:
            raise ValueError("+ or - expected")
    s.add_clause(l)
    cnf.append(l)

inds = range(1, 9)  # индексы клеток

# 1. В каждой строке находится ровно один ферзь
for i in inds:
    # Хотя бы один ферзь в строке i
    add_clause([('Q', i, j, '+') for j in inds])
    # Не более одного ферзя в строке i
    for j1 in inds:
        for j2 in inds:
            if j1 < j2:
                add_clause([('Q', i, j1, '-'), ('Q', i, j2, '-')])

# 2. В каждом столбце находится ровно один ферзь
for j in inds:
    # Хотя бы один ферзь в столбце j
    add_clause([('Q', i, j, '+') for i in inds])
    # Не более одного ферзя в столбце j
    for i1 in inds:
        for i2 in inds:
            if i1 < i2:
                add_clause([('Q', i1, j, '-'), ('Q', i2, j, '-')])

# 3. По диагоналям не может быть больше одного ферзя
# Диагонали типа i - j = const
for diff in range(-8 + 1, 8):
    diag1 = [(i, i - diff) for i in inds if 1 <= i - diff <= 8]
    if len(diag1) > 1:
        for (i1, j1), (i2, j2) in itertools.combinations(diag1, 2):
            add_clause([('Q', i1, j1, '-'), ('Q', i2, j2, '-')])

# Диагонали типа i + j = const
for sum_idx in range(2, 2 * 8 + 1):
    diag2 = [(i, sum_idx - i) for i in inds if 1 <= sum_idx - i <= 8]
    if len(diag2) > 1:
        for (i1, j1), (i2, j2) in itertools.combinations(diag2, 2):
            add_clause([('Q', i1, j1, '-'), ('Q', i2, j2, '-')])

sat, solution = s.solve()

if not sat:
    print('Нет решения')
else:
    new_field = [['.' for _ in range(0, 9)] for _ in range(0, 9)]
    for i in inds:
        for j in inds:
            if solution[vind('Q', i, j)]:
                new_field[i-1][j-1] = 'Q'

    # вывод поля
    print("Решение:")
    for i in inds:
        for j in inds:
            print(new_field[i][j], end=' ')
        print()