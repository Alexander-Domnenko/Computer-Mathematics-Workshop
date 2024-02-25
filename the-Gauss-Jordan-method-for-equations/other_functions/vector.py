import math


def len_vector(vector):
    r = []
    for i in range(len(vector)):
        r.append(vector[i]**2)
    return round(sum(r)**0.5, 2)


def multiplying_a_vector_by_a_scalar(vector, scalar):
    r = []
    for i in range(len(vector)):
        r.append(vector[i]*scalar)
    return (r)


def dividing_a_vector_by_a_scalar(vector, scalar):
    r = []
    for i in range(len(vector)):
        r.append(vector[i]/scalar)
    return (r)


def normalization_of_the_vector(vector):
    a2 = len_vector(vector)
    r = []
    for i in range(len(vector)):
        r.append(round(vector[i]/a2, 2))
    return r


def sum_vector(first_vector, second_vector):
    result_vector = []
    for i in range(len(first_vector)):
        result_vector.append(first_vector[i]+second_vector[i])
    return (result_vector)


def subtraction_vector(first_vector, second_vector):
    result_vector = []
    for i in range(len(first_vector)):
        result_vector.append(first_vector[i]-second_vector[i])
    return result_vector


def equality_of_vectors(first_vector, second_vector):
    k = 0
    for i in range(len(first_vector)):
        if first_vector[i] == second_vector[i]:
            k += 1
    if k == len(first_vector):
        return True
    else:
        return False


def equality_of_vectors_with_accuracy(first_vector, second_vector, accuracy=2):
    k = 0
    for i in range(len(first_vector)):
        if abs(first_vector[i]-second_vector[i]) < accuracy:
            k += 1
    if k == len(first_vector):
        return True
    else:
        return False


def scalar_product_of_vectors(first_vector, second_vector):
    r = []
    for i in range(len(first_vector)):
        r.append(first_vector[i]*second_vector[i])
    return sum(r)


def cos_a(firs_vector, second_vector):
    r = (scalar_product_of_vectors(firs_vector, second_vector)) / \
        (len_vector(firs_vector)*len_vector(second_vector))
    return round(r, 2)


def angle_a(first_vector, second_vector):
    c = cos_a(first_vector, second_vector)
    r = math.acos(c)
    return math.degrees(r)


def co_directional_vectors(first_vector, second_vector):
    if cos_a(first_vector, second_vector) == 1:
        return True
    else:
        return False


def oppositely_directed_vectors(first_vector, second_vector):
    if cos_a(first_vector, second_vector) == -1:
        return True
    else:
        return False


def collinear_vectors(first_vector, second_vector):
    if abs(cos_a(first_vector, second_vector)) == 1:
        return True
    else:
        return False


def orthogonal_vectors(first_vector, second_vector):
    if cos_a(first_vector, second_vector) == 0:
        return True
    else:
        return False


def changing_the_direction_to_the_opposite(vector):
    r = []
    for i in range(len(vector)):
        r.append(vector[i] * -1)
    return r


def scalar_projection_of_a_vector_onto_a_vector(first_vector, second_vector):
    r = scalar_product_of_vectors(
        first_vector, second_vector)/len_vector(second_vector)
    return round(r, 2)


def vector_projection_of_a_vector_onto_a_vector(first_vector, second_vector):
    r = scalar_product_of_vectors(
        first_vector, second_vector)/scalar_product_of_vectors(second_vector, second_vector)
    print(r)
    lr = multiplying_a_vector_by_a_scalar(second_vector, r)
    return lr
