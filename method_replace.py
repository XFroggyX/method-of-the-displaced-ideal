"""
Метод перестановок
"""
from itertools import permutations
from main import *


def permutation_method(matrix_pr, eks=None):
    """Метод перестановок"""
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

    return complex_importance


def check(matrix, id_str_a, id_str_b):
    C = []
    H = []
    for i in range(len(matrix[id_str_a])):
        if matrix[id_str_a][i] > matrix[id_str_b][i]:
            C.append(i)
        elif matrix[id_str_a][i] < matrix[id_str_b][i]:
            H.append(i)

    return [C, H]


def calculat(check, l):
    C = check[0]
    H = check[1]

    pos = 0
    neg = 0
    for i in range(len(C)):
        pos += l[C[i]]
    for i in range(len(H)):
        neg += l[H[i]]
    return pos - neg

# TODO Не вычислять энтропию после каждой итерации

if __name__ == "__main__":
    """test"""
    matrix_pr = [[1000, 4800, 2048, 9940],[1000, 4500, 1024, 8400],[1050, 5500, 6144, 15629], [1020, 5400, 2048, 10799], ]
    #matrix_pr = [[10, 100, 0, 8150], [6, 1000, 0, 8600], [10, 100, 1, 9500], [5, 1000, 2, 17000]]
    #matrix_pr = [[40, 2.5, 11, 96.81], [130, 16.5, 56, 99.14], [71, 23, 13, 99.73], [175, 5.5, 3, 99.41]]

    #matrix_pr = [[4.8, 12, 24, 700], [4.80, 18, 36, 1000], [4.90, 16, 32, 595], [5.00, 8, 16, 556]]

    #eks = ((4, 4, 2, 6), (0.25, 0.25, 0.125, 0.375))  # TODO: значения

    l = permutation_method(matrix_pr)
    all_combinations = []
    C = []
    H = []
    for i in permutations('1234', 4):
        all_combinations.append(i)
    print(all_combinations)
    kekw = []
    for i in range(len(all_combinations)):
        B = 0
        for j in range(len(all_combinations[i])):
            k = j + 1
            if k >= len(all_combinations[i]):
                continue
            index_a = all_combinations[i][j]
            index_b = all_combinations[i][k]
            checkk = check(matrix_pr, int(index_a)-1, int(index_b)-1)
            B += calculat(checkk, l)
        print(all_combinations[i], B)
