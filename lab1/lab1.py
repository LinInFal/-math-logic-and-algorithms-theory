# Лабораторная работа № 1 «Таблицы истинности»
import itertools


def conjunction(a, b):
    return a and b

def disjunction(a, b):
    return a or b

def implication(a, b):
    return int(not a or b)

def equivalence(a, b):
    return int(a == b)

def negation(a):
    return int(not a)

def xor(a, b):
    return a ^ b

def truth_table_by_func(f, f_name):
    print(f"\nФункция: {f_name}")
    print("Таблица истинности:")
    print("+---+---+---------+")
    print("| A | B | f(A, B) |")
    print("+---+---+---------+")
    for a, b in itertools.product([0, 1], repeat=2):
        print(f"| {a} | {b} |    {f(a, b)}    |")
    print("+---+---+---------+")

def truth_table_negation():
    print("\nФункция: Отрицание")
    print("Таблица истинности:")
    print("+---+---------+")
    print("| A | f(A)    |")
    print("+---+---------+")
    for a in [0, 1]:
        print(f"| {a} |    {negation(a)}    |")
    print("+---+---------+")

def functions_menu():
    print("\nВыберите операцию:"
          "\n1. Конъюнкция (&)"
          "\n2. Дизъюнкция (|)"
          "\n3. Импликация (→)"
          "\n4. Эквиваленция (↔)"
          "\n5. Отрицание (¬)"
          "\n6. Сложение по модулю два (⊕)")
    choice = input()

    if choice == '1':
        truth_table_by_func(conjunction, "Конъюнкция")
    elif choice == '2':
        truth_table_by_func(disjunction, "Дизъюнкция")
    elif choice == '3':
        truth_table_by_func(implication, "Импликация")
    elif choice == '4':
        truth_table_by_func(equivalence, "Эквиваленция")
    elif choice == '5':
        truth_table_negation()
    elif choice == '6':
        truth_table_by_func(xor, "Сложение по модулю два")
    else:
        print("Неверный ввод.")

def eval_formula(formula, a, b):
    formula = formula.replace('A', str(a)).replace('B', str(b))
    return int(eval(formula))

def check_equivalence(e_name, f_formula, g_formula):
    print(f"\nРавносильность: {e_name}")
    print("Таблица истинности:")
    print("+---+---+---------+---------+")
    print("| A | B | f(A, B) | g(A, B) |")
    print("+---+---+---------+---------+")
    equivalent = True
    for a, b in itertools.product([0, 1], repeat=2):
        f_val = eval_formula(f_formula, a, b)
        g_val = eval_formula(g_formula, a, b)
        print(f"| {a} | {b} |    {f_val}    |    {g_val}    |")
        if f_val != g_val:
            equivalent = False
    print("+---+---+---------+---------+")
    if equivalent:
        print("Формулы равносильны.")
    else:
        print("Формулы не равносильны.")

def equivalence_menu():
    print("\nВыберите равносильность:"
          "\n1. Закон двойного отрицания"
          "\n2. Закон де Моргана"
          "\n3. Закон склеивания")
    choice = input()

    if choice == '1':
        print("\nВведите формулу f(A, B) (например, not (not A)):")
        f_formula = input("f(A, B): ").strip()
        print("\nВведите формулу g(A, B) (например, A):")
        g_formula = input("g(A, B): ").strip()
        check_equivalence("Закон двойного отрицания", f_formula, g_formula)
    elif choice == '2':
        print("\nВведите формулу f(A, B) (например, not (A or B):")
        f_formula = input("f(A, B): ").strip()
        print("\nВведите формулу g(A, B) (например, not A and not B):")
        g_formula = input("g(A, B): ").strip()
        check_equivalence("Закон де Моргана", f_formula, g_formula)
    elif choice == '3':
        print("\nВведите формулу f(A, B) (например, A or (A and B)):")
        f_formula = input("f(A, B): ").strip()
        print("\nВведите формулу g(A, B) (например, A):")
        g_formula = input("g(A, B): ").strip()
        check_equivalence("Закон склеивания", f_formula, g_formula)
    else:
        print("Неверный ввод. Попробуйте снова.")

def main():
    while True:
        print("\nВыберите действие:"
              "\n1. Бинарные логические операции"
              "\n2. Равносильность"
              "\n3. Выход")
        choice = input()
        if choice == '1':
            functions_menu()
        elif choice == '2':
            equivalence_menu()
        elif choice == '3':
            break
        else:
            print("Неверный ввод. Выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
