import pytest

from matrix.matrix import *


@pytest.mark.parametrize("a,b,expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[10, 10, 10], [10, 10, 10], [10, 10, 10]])])
def test_sum_matrixr(a, b, expected_result):
    assert sum_matrix(a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]])])
def test_sub_matrixr(a, b, expected_result):
    assert sub_matrix(a, b) == expected_result


@pytest.mark.parametrize("a,expected_result", [([[1, 2, 3]], [[1], [2], [3]])])
def test_matrix_transponition(a, expected_result):
    assert matrix_transponition(a,) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([[1, 2, 3]], 2, [[2, 4, 6]])])
def test_multiplying_matrix_by_scalar(a, b, expected_result):
    assert multiplying_matrix_by_scalar(a, b) == expected_result


@pytest.mark.parametrize("a,b, expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [4, 5, 6])])
def test_getting_row_by_index(a, b, expected_result):
    assert getting_row_by_index(a, b) == expected_result


@pytest.mark.parametrize("a,b, expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [2, 5, 8])])
def test_getting_column_by_index(a, b, expected_result):
    assert getting_column_by_index(a, b) == expected_result


@pytest.mark.parametrize("a,b,c, expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 0, [[4, 5, 6], [1, 2, 3], [7, 8, 9]])])
def test_rearranging_strings(a, b, c, expected_result):
    assert rearranging_strings(a, b, c) == expected_result


@pytest.mark.parametrize("a,b,c, expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 10, [[1, 2, 3], [40, 50, 60], [7, 8, 9]])])
def test_multiplying_row_matrix_by_scalar(a, b, c, expected_result):
    assert multiplying_row_matrix_by_scalar(a, b, c) == expected_result


@pytest.mark.parametrize("a,b, expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[30, 24, 18], [84, 69, 54], [138, 114, 90]])])
def test_multiplying_matrix(a, b, expected_result):
    assert multiplying_matrix(a, b) == expected_result


@pytest.mark.parametrize("a,b, c,d,expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 1, 2, [[10, 14, 18], [4, 5, 6], [7, 8, 9]])])
def test_sum_row_multiplying_by_scalar(a, b, c, d, expected_result):
    assert sum_row_multiplying_by_scalar(a, b, c, d) == expected_result


@pytest.mark.parametrize("a,b, c,d,expected_result", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2, 2, [[1, 2, 3], [-6, -6, -6], [7, 8, 9]])])
def test_sub_row_multiplying_by_scalar(a, b, c, d, expected_result):
    assert sub_row_multiplying_by_scalar(a, b, c, d) == expected_result
