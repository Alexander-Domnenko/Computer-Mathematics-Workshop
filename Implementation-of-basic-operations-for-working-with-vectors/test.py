import pytest
from vector import *





@pytest.mark.parametrize("a,expected_result", [([2, 3], 3.61),
                                               ([1, 2, 3], 3.74),
                                               ([0, 0], 0),
                                               ([-2, -3, 2], 4.12)
                                               ])
def test_len_vector(a, expected_result):
    assert len_vector(a) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], 0, [0, 0]),
                                                 ([1, 2, 3], 4, [4, 8, 12]),
                                                 ([0, 0], 5, [0, 0]),
                                                 ([-2, -3, 2], -2.5, [5, 7.5, -5])
                                                 ])
def test_multiplying_a_vector_by_a_scalar(a, b, expected_result):
    assert multiplying_a_vector_by_a_scalar(
        a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], -1, [-2.0, -3.0]),
                                                 ([1, 2, 3], 4, [
                                                  0.25, 0.5, 0.75]),
                                                 ([0, 0], 5, [0, 0]),
                                                 ([-2, -3, 2], -2.5,
                                                  [0.8, 1.2, -0.8])
                                                 ])
def test_dividing_a_vector_by_a_scalar(a, b, expected_result):
    assert dividing_a_vector_by_a_scalar(
        a, b) == expected_result


@pytest.mark.parametrize("a,expected_result", [([2, 3], [0.55, 0.83]),
                                               ([1, 2, 3], [0.27, 0.53, 0.8]),
                                               ([-2, -3, 2], [-0.49, -0.73, 0.49])])
def test_normalization_of_the_vector(a,  expected_result):
    assert normalization_of_the_vector(
        a,) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], [0.55, 0.83], [2.55, 3.83]),
                                                 ([1, 2, 3], [0.27, 0.53, 0.8], [
                                                  1.27, 2.5300000000000002, 3.8]),
                                                 ([-2, -3, 2], [-0.49, -0.73,
                                                  0.49], [-2.49, -3.73, 2.49]),
                                                 ([0, 0], [-1, -1], [-1, -1])])
def test_sum(a, b, expected_result):
    assert sum_vector(
        a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], [0.55, 0.83], [1.45, 2.17]),
                                                 ([1, 2, 3], [0.27, 0.53, 0.8], [
                                                  0.73, 1.47, 2.2]),
                                                 ([-2, -3, 2], [-0.49, -0.73,
                                                  0.49], [-1.51, -2.27, 1.51]),
                                                 ([0, 0], [-1, -1], [1, 1])])
def test_subtraction_vecctor(a, b, expected_result):
    assert subtraction_vector(
        a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], [0, 0], False),
                                                 ([1, 2, 3], [1, 2, 3], True)])
def test_equality_of_vectors(a, b, expected_result):
    assert equality_of_vectors(
        a, b) == expected_result


@pytest.mark.parametrize("a,b,c,expected_result", [([2, 3], [0, 0], 2, False),
                                                   ([1, 2, 3], [-1, -2, -3], 4, True)])
def test_equality_of_vectors_with_accuracy(a, b, c, expected_result):
    assert equality_of_vectors_with_accuracy(
        a, b, c) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], [0, 0], 0),
                                                 ([1, 2, 3], [-1.1, -2, -3], -14.1)])
def test_scalar_product_of_vectors(a, b, expected_result):
    assert scalar_product_of_vectors(
        a, b,) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], [2, 3], 1.0),
                                                 ([1, 2, 3], [-1.1, -2, -3], -1.0)])
def test_cos_a(a, b, expected_result):
    assert cos_a(
        a, b,) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], [2, 3], 0.0),
                                                 ([1, 2, 3], [-1.1, -2, -3], 180.0)])
def test_angle_a(a, b, expected_result):
    assert angle_a(
        a, b,) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], [2, 3], True),
                                                 ([1, 2, 3], [-1.1, -2, -3], False)])
def test_co_directional_vectors(a, b, expected_result):
    assert co_directional_vectors(
        a, b,) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 3], [2, 3], False),
                                                 ([1, 2, 3], [-1, -2, -3], True)])
def test_oppositely_directed_vectors(a, b, expected_result):
    assert oppositely_directed_vectors(
        a, b,) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([2, 0], [0, 34], True),
                                                 ([1, 2, 3], [-1, -2, -3], False)])
def test_orthogonal_vectors(a, b, expected_result):
    assert orthogonal_vectors(
        a, b,) == expected_result


@pytest.mark.parametrize("a,expected_result", [([2, 0], [-2, 0]),
                                               ([1, 2, 3], [-1, -2, -3])])
def test_changing_the_direction_to_the_opposite(a, expected_result):
    assert changing_the_direction_to_the_opposite(
        a,) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([1, 2], [3, 4], 2.2),
                                                 ([1, 2, 3], [-1, -2, -3], -3.74)])
def test_scalar_projection_of_a_vector_onto_a_vector(a, b, expected_result):
    assert scalar_projection_of_a_vector_onto_a_vector(
        a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_result", [([4, 5], [6, 0], [4, 0]),
                                                 ])
def test_vector_projection_of_a_vector_onto_a_vector(a, b, expected_result):
    assert vector_projection_of_a_vector_onto_a_vector(
        a, b) == expected_result
