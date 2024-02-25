import pytest

from sle import sle


@pytest.mark.parametrize("a,b,expected_result", [([[2.0, 3.0], [4.0, 3.0]], [[2.0], [7.0]], [[2.5], [-1.0]])])
def test_sle_2d_1(a, b, expected_result):
    assert sle(a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([[1, -6], [5, 6]], [[17], [13]], [[5.0], [-2.0]])])
def test_sle_2d_2(a, b, expected_result):
    assert sle(a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([[-1, 2, 6], [3, -6, 0], [1, 0, 6]], [[15], [-9], [5]], [[-7.0], [-2.0], [2.0]])])
def test_sle_3d_1(a, b, expected_result):
    assert sle(a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([[1, 1, 1], [1, 2, 3], [1, 3, 6]], [[3], [6], [10]], [[1.0], [1.0], [1.0]])])
def test_sle_3_2(a, b, expected_result):
    assert sle(a, b) == expected_result
