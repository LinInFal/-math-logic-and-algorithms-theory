# Лабораторная работа № 4 «Метод резолюций»

'''Описание структуры данных "ДНФ":
ДНФ - это дизъюнкция конъюнктов
Представим конъюнкт в виде списка из n значений 0, 1, -1
  (n - число переменных), где 1 на i-й позиции означает, что
  переменная x_i присутствует в конъюнкте, -1 на i-й позиции означает,
  что присутствует отрицание переменной x_i, и 0 на i-й позиции означает,
  что переменной x_i в конъюнкте нет
Тогда ДНФ будет представляться в виде списка списков, в котором каждый список
  представляет конъюнкт, например: [[1, 0, -1], [0, 1, 1], [0, -1, 0]]
  означает формулу (x and not z) or (y and z) or (not y)'''

'''Принимает на вход ДНФ, возвращает СДНФ
Например: если на входе (x and not z) or (y and z) or (not y),
  то на выходе должно получиться
  (x and y and not z) or (x and not y and not z) or
  (x and y and z) or (not x and y and z) or (not x and not y and not z) or
  (not x and not y and z) or (x and not y and z)
Таким образом, в результирующем списке списков не будет нулей'''
def calc_fdnf(dnf):
    fdnf = []
    for conj in dnf:
        x_values = [1, -1] if conj[0] == 0 else [conj[0]]
        y_values = [1, -1] if conj[1] == 0 else [conj[1]]
        z_values = [1, -1] if conj[2] == 0 else [conj[2]]
        for x in x_values:
            for y in y_values:
                for z in z_values:
                    new_conj = [x, y, z]
                    new_conj_is_present = False
                    # Проверка на наличие такого же конъюнкта в списке fdnf
                    for c in fdnf:
                        if c == new_conj:
                            new_conj_is_present = True
                            break
                    if not new_conj_is_present:
                        fdnf.append(new_conj)
    return fdnf

# Принимает на вход ДНФ, возвращает строку с выражением
def dnf_str(dnf):
    s = ""
    start = True
    for conj in dnf:
        conj_str = ""
        if conj[0] == 1:
            conj_str += "x"
        elif conj[0] == -1:
            conj_str += "~x"
        if conj[1] == 1:
            conj_str += "y"
        elif conj[1] == -1:
            conj_str += "~y"
        if conj[2] == 1:
            conj_str += "z"
        elif conj[2] == -1:
            conj_str += "~z"
        if not start:
            s += " | "
        start = False
        s += conj_str
    return s

dnf_tests = [
    [[1, 0, -1], [0, 1, 1], [0, -1, 0]],  # Пример из лабораторной работы
    [[1, -1, 0], [0, 1, -1], [-1, 0, 1]], # Тест 2
    [[1, 1, 0], [0, -1, 1], [-1, 1, -1]], # Тест 3
    [[0, 0, 1], [1, 0, -1], [0, 1, 0]]    # Тест 4
]

for dnf in dnf_tests:
    print("ДНФ = ", dnf_str(dnf))
    fdnf = calc_fdnf(dnf)
    print("СДНФ = ", dnf_str(fdnf), "\n")

'''Описание структуры данных "КНФ":
КНФ - это конъюнкция дизъюнктов
Представим дизъюнкт в виде списка из n значений 0, 1, -1
  (n - число переменных), где 1 на i-й позиции означает, что
  переменная x_i присутствует в дизъюнкте, -1 на i-й позиции означает,
  что присутствует отрицание переменной x_i, и 0 на i-й позиции означает,
  что переменной x_i в дизъюнкте нет
Тогда КНФ будет представляться в виде списка списков, в котором каждый список
  представляет дизъюнкт, например: [[1, 0, -1], [0, 1, 1], [0, -1, 0]]
  означает формулу (x or not z) and (y or z) and (not y)'''

# Принимает на вход КНФ, возвращает строку с выражением
def cnf_str(cnf):
    s = ""
    start = True
    for disj in cnf:
        disj_str = "("
        if disj[0] == 1:
            if disj_str != "(":
                disj_str += "|"
            disj_str += "x"
        elif disj[0] == -1:
            if disj_str != "(":
                disj_str += "|"
            disj_str += "~x"
        if disj[1] == 1:
            if disj_str != "(":
                disj_str += "|"
            disj_str += "y"
        elif disj[1] == -1:
            if disj_str != "(":
                disj_str += "|"
            disj_str += "~y"
        if disj[2] == 1:
            if disj_str != "(":
                disj_str += "|"
            disj_str += "z"
        elif disj[2] == -1:
            if disj_str != "(":
                disj_str += "|"
            disj_str += "~z"
        disj_str += ")"
        if not start:
            s += " & "
        start = False
        s += disj_str
    return s

# Возвращает резольвенту дизъюнктов disj1 и disj2 по k-й переменной
# Например, если disj1 = [1, 0, -1], disj2 = [1, 1, 1], то
#   результатом будет дизъюнкт disj = [1, 1, 0]
def find_resolvent(disj1, disj2, k):
    # Применяем правило резолюции: сокращаем противоположную переменную,
    #   а остальные складываем
    disj = [0, 0, 0]
    for v in range(3):
        if disj1[v] == disj2[v]:
            disj[v] = disj1[v]
        else:
            disj[v] = disj1[v] + disj2[v]
    disj[k] = 0
    return disj

# Добавляет к КНФ резольвенту каких-нибудь двух резольвирующих дизъюнктов
# Возвращает True в случае наличия пустой резольвенты
#   (которая не добавляется к КНФ) и False иначе
def add_resolvent(cnf):
    for i in range(len(cnf)):
        for j in range(i + 1, len(cnf)):
            # для каждой пары дизъюнктов проверяем, резольвируют ли они
            # для этого считаем количество противоположных переменных
            disj1 = cnf[i]
            disj2 = cnf[j]
            cnt = 0  # счетчик противоположных переменных
            ind = -1  # индекс противоположной переменной
            for k in range(3):
                if disj1[k] != 0 and disj2[k] != 0 and disj1[k] != disj2[k]:
                    cnt += 1
                    ind = k
            # если ровно одна противоположная переменная,
            #   находим резольвенту и добавляем ее к КНФ
            #   (в случае, когда она непуста)
            if cnt == 1:
                res = find_resolvent(disj1, disj2, ind)
                if res != [0, 0, 0]:
                    if res not in cnf:
                        cnf.append(res)
                        return False
                else:
                    return True
    return False

'''Метод резолюций заключается в получении логических следствий из КНФ
Выбираются пары резольвирующих множителей КНФ (дизъюнктов)
Два дизъюнкта резольвируют, если содержат ровно одну пару
  противоположных литералов
Для выбранной пары резольвирующих дизъюнктов вычисляется
  их резольвента по правилу резолюции
Резольвента двух дизъюнктов - это их логическое следствие
Резольвента каждый раз добавляется к КНФ
Этот процесс продолжается до тех пор, пока не будет получена 
  пустая резольвента или пока метод не зайдет в тупик'''

def apply_resolution_method(cnf):
    print("Вход:", cnf_str(cnf))
    print("Логические следствия:")
    is_zero = False
    while True:
        cnf_size = len(cnf)
        is_zero = add_resolvent(cnf)
        if len(cnf) == cnf_size:
            break
        else:
            print(cnf_str([cnf[-1]])[1:-1])
    if is_zero:
        print(0)
        print("Результат: невыполнима\n")
    else:
        print("тупик")
        print("Результат: выполнима\n")

cnf_tests = [
    [[1, 0, -1], [0, 1, 1], [0, -1, 0], [-1, 0, 0]],  # Пример из лабораторной работы
    [[1, 1, 0], [-1, 0, 1], [0, -1, -1], [1, 0, -1]], # Тест 2
    [[1, -1, 1], [0, 1, -1], [-1, 0, 0], [1, 0, 0]],  # Тест 3
    [[0, 0, 1], [1, 0, -1], [0, 1, 0], [-1, 0, 0]]    # Тест 4
]

for cnf in cnf_tests:
    apply_resolution_method(cnf)

# Тестирование на примере 1.7 из методички
print("===Пример 1.7===")
cnf = [[0, 1, 1], [1, 0, -1], [-1, 0, -1], [0, 1, 0]]  # Пример для D = 0
apply_resolution_method(cnf)
cnf = [[0, 1, 1], [1, 0, -1], [-1, 0, -1], [0, 0, 1]]  # Пример для D = 1
apply_resolution_method(cnf)