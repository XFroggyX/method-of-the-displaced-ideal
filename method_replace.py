"""
Метод перестановок
"""

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


if __name__ == "__main__":
    """test"""
    matrix_pr = [[1000, 4800, 2048, 9940],
                 [1000, 4500, 1024, 8400],
                 [1050, 5500, 6144, 15629],
                 [1020, 5400, 2048, 10799], ]

    eks = ((4, 4, 2, 6), (0.25, 0.25, 0.125, 0.375))  # TODO: значения

    result = permutation_method(matrix_pr, eks)
    for elem in result:
        print(elem)