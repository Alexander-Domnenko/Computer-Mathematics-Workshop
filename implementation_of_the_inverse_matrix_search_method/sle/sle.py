from matrix.matrix import *
from vector.vector import *


def reverse_matrix(matrix):
    r = matrix[::-1]
    for i in range(len(matrix)):
        r[i].reverse()
    return r


def sort_rows(matrix):
    for jj in range(len(matrix)):
        for i in range(len(matrix)):
            if matrix[i][i] == 0:
                for j in range(len(matrix)):
                    if matrix[j][i] != 0:
                        matrix = rearranging_strings(matrix, i, j)
    for ii in range(len(matrix)):
        if matrix[ii][ii] == 0:
            raise ValueError(
                "Решения нет, либо система имеет множество решений")
    return matrix


def merge_matrix(m1, m2):
    r = []
    for i in range(len(m1)):
        m1[i].append(m2[i][0])
        r.append(m1[i])
    return r


def main_loop(matrix):
    matrix = sort_rows(matrix)
    for i in range(len(matrix)):
        matrix = multiplying_row_matrix_by_scalar(matrix, i, 1/matrix[i][i])
        for j in range(i+1, len(matrix)):
            t = multiplying_row_matrix_by_scalar(matrix, i, matrix[j][i])
            matrix[j] = subtraction_vector(matrix[j], t[i])
        matrix = sort_rows(matrix)
    return matrix


def sle(matrix, b):
    matrix = merge_matrix(matrix, b)
    matrix = main_loop(matrix)
    m2 = []
    b2 = []
    m3 = []
    b3 = []
    for i in matrix:
        m2.append(i[:len(matrix)])
        b2.append(i[len(matrix):len(matrix)+1])
    m2 = reverse_matrix(m2)
    b2 = reverse_matrix(b2)
    m2 = merge_matrix(m2, b2)
    m2 = main_loop(m2)
    for i in m2:
        m3.append(i[:len(matrix)])
        b3.append(i[len(matrix):len(matrix)+1])
    return reverse_matrix(b3)




