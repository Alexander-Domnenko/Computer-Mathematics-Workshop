
from check_operation import *
from vector.vector import *


# сложение матриц


def sum_matrix(first_matrix, second_matrix):
    ensure_is_equal_sum_or_sub_matrix(first_matrix, second_matrix)
    r = []
    for i in range(len(first_matrix)):
        ensure_is_equal_sum_or_sub_matrix(first_matrix[i], second_matrix[i])
        r.append(sum_vector(first_matrix[i], second_matrix[i]))
    return r


# вычитание матриц


def sub_matrix(first_matrix, second_matrix):
    ensure_is_equal_sum_or_sub_matrix(first_matrix, second_matrix)
    r = []
    for i in range(len(first_matrix)):
        ensure_is_equal_sum_or_sub_matrix(first_matrix[i], second_matrix[i])
        r.append(subtraction_vector(first_matrix[i], second_matrix[i]))
    return r


# транспонирование матрицы


def matrix_transponition(matrix):
    copy_matrix = [row[:] for row in matrix]
    n = len(copy_matrix)
    m = len(copy_matrix[0])
    r = [[0 for _ in range(n)]for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r[i][j] = copy_matrix[j][i]
    return r


# умножение матрицы на скаляр


def multiplying_matrix_by_scalar(matrix, scalar):
    r = []
    for i in matrix:
        r.append(multiplying_a_vector_by_a_scalar(i, scalar))
    return r


# получение строки по индексу


def getting_row_by_index(matrix, index):
    ensure_is_equal_index_row(index, matrix)
    copy_matrix = [row[:] for row in matrix]
    for i in range(len(copy_matrix)):
        return (copy_matrix[index])


# умножение одной строки матрицы по заданному индексу на скаляр


def multiplying_row_matrix_by_scalar(matrix, index, scalar):
    ensure_is_equal_index_row(index, matrix)
    copy_matrix = [row[:] for row in matrix]
    copy_matrix[index] = multiplying_a_vector_by_a_scalar(
        getting_row_by_index(copy_matrix, index), scalar)
    return copy_matrix


# сложение строк умноженных на число


def sum_row_multiplying_by_scalar(matrix, index, index2, scalar):
    ensure_is_equal_row(matrix, index, index2)
    copy_matrix = [row[:] for row in matrix]
    copy_matrix[index] = sum_vector(multiplying_a_vector_by_a_scalar(getting_row_by_index(
        copy_matrix, index), scalar), multiplying_a_vector_by_a_scalar(getting_row_by_index(copy_matrix, index2), scalar))
    return copy_matrix


# вычитание строк умноженых на число


def sub_row_multiplying_by_scalar(matrix, index, index2, scalar):
    ensure_is_equal_row(matrix, index, index2)
    copy_matrix = [row[:] for row in matrix]
    copy_matrix[index] = subtraction_vector(multiplying_a_vector_by_a_scalar(getting_row_by_index(
        copy_matrix, index), scalar), multiplying_a_vector_by_a_scalar(getting_row_by_index(copy_matrix, index2), scalar))
    return copy_matrix


# перестановка строк матрицы


def rearranging_strings(matrix, what, where):
    ensure_is_equal_rearranging_strings(matrix, what, where)
    copy_matrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        copy_matrix[what], copy_matrix[where] = copy_matrix[where], copy_matrix[what]
    return copy_matrix


# получение столбца по индексу


def getting_column_by_index(matrix, index):
    ensure_is_equal_index_column(index, matrix)
    copy_matrix = [row[:] for row in matrix]
    return getting_row_by_index(matrix_transponition(copy_matrix), index)


# умножение матриц


def multiplying_matrix(first_matrix, second_matrix):
    ensure_is_equal_len(first_matrix, second_matrix)
    row = len(first_matrix)
    column = len(second_matrix[0])
    r = [[0 for _ in range(row)]for _ in range(column)]
    second_matrix = matrix_transponition(second_matrix)
    for i in range(row):
        for j in range(column):
            r[i][j] = scalar_product_of_vectors(
                first_matrix[i], second_matrix[j])
    return r
