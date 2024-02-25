import pytest
from sle_by_gauss import *


@pytest.mark.parametrize("a,expected_result", [([[1, 2], [3, 4]], [[-2.0, 1.0], [1.5, -0.5]])])
def test_search_inverse_matrix_by_gauss_2d(a, expected_result):
    assert search_inverse_matrix_by_gauss(a) == expected_result


@pytest.mark.parametrize("a,expected_result", [([[1, 2, 5], [3, 2, 1], [1, 1, 1]], [[0.5, 1.5, -4.0], [-1.0, -2.0, 7.0], [0.5, 0.5, -2.0]])])
def test_search_inverse_matrix_by_gauss_3d(a, expected_result):
    assert search_inverse_matrix_by_gauss(a) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([[1, -6], [5, 6]], [[17], [13]], [[5.0], [-2.0]])])
def test_sle_by_gauss_2d(a, b, expected_result):
    assert sle(a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([[1, 1, 1], [1, 2, 3], [1, 3, 6]], [[3], [6], [10]], [[1.0], [1.0], [1.0]])])
def test_sle_by_gauss_3d(a, b, expected_result):
    assert sle(a, b) == expected_result