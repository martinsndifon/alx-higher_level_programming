#!/usr/bin/python3


"""
This module computes the division of all
elements of a matrix. Matrix must be a list of integers
of floats, each row of the matrix must be of the same size.
"""


def matrix_divided(matrix, div):

    """
    matrix_divided - divideds all elements of a matrix.
    div: must be a number(integer of float)
    div: cannot be equal to 0
    All elements of the matrix should be devided by div, rounded
    to 2 decimal places
    Returns a new matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or type(matrix) is not list:
        raise TypeError(msg)

    if not all(isinstance(element, list)for element in matrix):
        raise TypeError(msg)

    if all(len(arr) == 0 for arr in matrix):
        raise TypeError(msg)

    number = True
    for arr in matrix:
        for element in arr:
            if type(element) not in [int, float]:
                number = False
                break
        else:
            continue
        break

    if not number:
        raise TypeError(msg)

    first_arr_len = len(matrix[0])
    if not all(first_arr_len == len(arr) for arr in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")

    return list(list(map(lambda n: round(n/div, 2), item)) for item in matrix)
