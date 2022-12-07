#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = []
    for item in matrix:
        sub_list = list(map(lambda x: x*x, item))
        new_matrix.append(sub_list)

    return new_matrix
