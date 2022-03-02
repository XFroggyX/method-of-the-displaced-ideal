"""
Метод смещенного идеала
"""

import math
from heapq import nsmallest


def calculation_best_value(matrix_pr):
    """Возвращает худший и лучший исход"""
    elem0 = [matrix_pr[index][0] for index in range(len(matrix_pr))]
    elem1 = [matrix_pr[index][1] for index in range(len(matrix_pr))]
    elem2 = [matrix_pr[index][2] for index in range(len(matrix_pr))]
    elem3 = [matrix_pr[index][3] for index in range(len(matrix_pr))]
    return [
        [max(elem0), max(elem1), max(elem2), min(elem3)],
        [min(elem0), min(elem1), min(elem2), max(elem3)],
    ]


def calculation_matrix_d(matrix_pr, id_nid):
    """вычисление матрицы d"""
    matrix_d = [[0 for _ in range(len(matrix_pr[0]))] for _ in range(len(matrix_pr))]

    for i in range(len(matrix_pr[0])):
        for j in range(len(matrix_pr)):
            num = id_nid[0][i] - matrix_pr[j][i]
            den = id_nid[0][i] - id_nid[1][i]
            result = num / den
            matrix_d[j][i] = result

    return matrix_d


def sum_st(matrix, index):
    """сумма столбца матрицы"""
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][index]
    return sum


def calculation_matrix_p(matrix_d, matrix_pr):
    """Вычисление p"""
    matrix_p = []

    for i in range(len(matrix_d)):
        matrix_p.append([])
        for j in range(len(matrix_d[i])):
            result = matrix_pr[i][j] / (sum_st(matrix_pr, j))
            matrix_p[i].append(result)
    return matrix_p


def log_func(matrix_p, index):
    """p * ln(p), где p элемент столбца | после этого все значения сумируются"""
    result = 0
    for j in range(len(matrix_p)):
        if matrix_p[j][index] == 0:
            return 0
        else:
            result += matrix_p[j][index] * math.log(matrix_p[j][index])

    return result


def calculation_entropy(matrix_p):
    """Вычисляем энтропию"""
    ent = []

    for j in range(len(matrix_p[0])):
        k = 1 / math.log(len(matrix_p))
        result = -k * log_func(matrix_p, j)
        ent.append(result)

    return ent


def calculation_inverse_entropy(matrix_entropy):
    """Вычисляем обратную энтропию"""
    inv_ent = []

    for i in range(len(matrix_entropy)):
        inv_ent.append(1 - matrix_entropy[i])
    return inv_ent


def calculation_complex_importance(inv_ent, eks=None):
    """Вычисляем комплексную важность"""
    ci = []
    if eks is not None:
        for i in range(len(inv_ent)):
            result = (inv_ent[i] * eks[1][i]) / sum([inv_ent[j] * eks[1][j] for j in range(len(inv_ent))])
            ci.append(result)
        return ci

    for i in range(len(inv_ent)):
        result = inv_ent[i] / sum([inv_ent[j] for j in range(len(inv_ent))])
        ci.append(result)
    return ci


def distance_ideal_object(matrix_d, inv_ent):
    """Определяем растояние от идеального объекта до i-ого"""

    matrix_ras = []

    for i in range(len(matrix_d)):
        matrix_ras.append([])
        for p in range(1, 6):
            value = []
            for j in range(len(matrix_d[i])):
                value.append((inv_ent[j] * (1 - matrix_d[i][j])) ** p)
            res = sum(value) ** (1 / p)
            matrix_ras[i].append(res)

    return matrix_ras


def method_displaced_ideal(matrix_pr, eks=None):
    """Метод смещённого идеала"""
    print("matrix-pr", matrix_pr)
    id_nid = calculation_best_value(matrix_pr)
    print("id-nid", id_nid)
    matrix_d = calculation_matrix_d(matrix_pr, id_nid)
    print("matrix_d", matrix_d)
    matrix_p = calculation_matrix_p(matrix_d, matrix_pr)
    print("matrix_p", matrix_p)
    entropy = calculation_entropy(matrix_p)
    print("entropy", entropy)
    inverse_entropy = calculation_inverse_entropy(entropy)
    print("inverse_entropy", inverse_entropy)
    complex_importance = calculation_complex_importance(inverse_entropy, eks)
    print("complex_importance", complex_importance)

    dist_ideal_obj = distance_ideal_object(matrix_d, complex_importance)  # TODO: проверить на первой итерации
    print("dist_ideal_obj", dist_ideal_obj)
    return dist_ideal_obj


def transposition_matrix(matrix):
    """Разворачивает матрицу"""

    tr_matrix = []
    for j in range(len(matrix[0])):
        tr_matrix.append([])
        for i in range(len(matrix)):
            tr_matrix[j].append(matrix[i][j])
    return tr_matrix


def most_frequent(List):
    """Элемент, который встречается чаще всего"""
    return max(set(List), key=List.count)


def ranking_alternatives_and_screening_out(matrix_displaced_ideal):
    """Ранжирование и отсеивание"""

    matrix_ranking_elem = transposition_matrix(matrix_displaced_ideal)
    ranking_item = []
    for i in range(len(matrix_ranking_elem)):
        smallest = nsmallest(1, matrix_ranking_elem[i])[0]
        ranking_item.append(matrix_ranking_elem[i].index(smallest))

    print("ranking_item", ranking_item)
    frequency_item = most_frequent(ranking_item)

    return frequency_item


def main(matrix_pr, eks=None):
    """main func"""
    len_matrix_pr = len(matrix_pr)
    if len_matrix_pr <= 1:
        return matrix_pr
    while len_matrix_pr > 1:
        matrix_displaced_ideal = method_displaced_ideal(matrix_pr, eks)
        index = ranking_alternatives_and_screening_out(matrix_displaced_ideal)
        del matrix_pr[index]
        print("_" * 100)
        len_matrix_pr = len(matrix_pr)

    return matrix_pr


if __name__ == "__main__":
    """test"""
    #matrix_pr = [[1000, 4800, 2048, 9940],
                # [1000, 4500, 1024, 8400],
                # [1050, 5500, 6144, 15629],
               #  [1020, 5400, 2048, 10799],]
    # id_nid = ((1050, 5500, 6144, 8400),
    # (1000, 4500, 1024, 15629),)

    """main"""

    matrix_pr = [[10, 100, 0, 8150], [6, 1000, 0, 8600], [10, 100, 1, 9500], [5, 1000, 2, 17000]]
    # id_nid = ((10, 1000, 2, 8150), (5, 100, 0, 17000))

    eks = ((4, 4, 2, 6), (0.25, 0.25, 0.125, 0.375))  # TODO: значения
    result = main(matrix_pr)
    for elem in result:
        print(elem)
