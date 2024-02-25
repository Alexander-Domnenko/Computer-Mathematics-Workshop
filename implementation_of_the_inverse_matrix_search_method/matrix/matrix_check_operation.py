# проверка выхода индекса из range для строк


def ensure(is_ok, msg=''):
    if not is_ok:
        raise ValueError(msg)


def is_equal_index_row(index, matrix):
    return 0 <= index <= len(matrix)


def ensure_is_equal_index_row(index, matrix):
    ensure(is_equal_index_row(index, matrix), 'Неправильный индекс')


# проверка допустимости умножения матриц


def is_equal_len(first_matrix, second_matrix):
    return len(first_matrix[0]) == len(second_matrix)


def ensure_is_equal_len(first_matrix, second_matrix):
    ensure(is_equal_len(first_matrix, second_matrix), 'Матрицы умножить нельзя')


# проверка выхода индекса из range для столбцов


def is_equal_index_column(index, matrix):
    return 0 <= index <= len(matrix[0])


def ensure_is_equal_index_column(index, matrix):
    ensure(is_equal_index_column(index, matrix), 'Неправильный индекс')


# проверка на перестановку строк


def is_equal_rearranging_strings(matrix, what, where):
    return what <= len(matrix) and where <= len(matrix) and what >= 0 and where >= 0


def ensure_is_equal_rearranging_strings(matrix, what, where):
    ensure(is_equal_rearranging_strings(matrix, what, where),
           'Нельзя поменять строки местами')


# проверка на сложение матриц


def is_equal_sum_or_sub_matrix(first_matrix, second_matrix):
    return len(first_matrix) == len(second_matrix)


def ensure_is_equal_sum_or_sub_matrix(first_matrix, second_matrix):
    ensure(is_equal_sum_or_sub_matrix(first_matrix,
           second_matrix), 'Нельзя сложить матрицы')


# проверка на выход из range для нескольких строк


def is_equal_row(matrix, index, index2):
    return 0 <= index <= len(matrix) and 0 <= index2 <= len(matrix)


def ensure_is_equal_row(matrix, index, index2):
    ensure(is_equal_row(matrix, index, index2), 'Неправильный индекс')
