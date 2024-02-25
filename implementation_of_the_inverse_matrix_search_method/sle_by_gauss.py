from matrix.matrix import *
from sle.sle import sle


def build_unit_matrix(n):
    r = []
    for i in range(n):
        r.append([])
        for j in range(n):
            if i == j:
                r[i].append(1)
            else:
                r[i].append(0)
    return r


def search_inverse_matrix_by_gauss(matrix):
    unit_matrix = build_unit_matrix(len(matrix))
    res = []
    for i in range(len(matrix)):
        n = [[x[i]] for x in unit_matrix]
        res.append(getting_column_by_index(sle(matrix, n), 0))
        matrix = matrix_transponition(matrix)
        matrix.pop(-1)
        matrix = matrix_transponition(matrix)
    return matrix_transponition(res)


def sle_by_inverse_matrix(matrix, b):
    return multiplying_matrix(matrix, b)
