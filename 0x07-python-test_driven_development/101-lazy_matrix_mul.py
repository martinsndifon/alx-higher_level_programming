#!/usr/bin/python3


"""A module that computes the multiplication of a matrix
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):

    """this function multiplies a matrix
    - m_a and m_b must be list of list of integers of floats
    - m_a and m_b cannot be empty
    - Each row of m_a and m_b must be of the same size
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(element, list) for element in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(element, list) for element in m_b):
        raise TypeError("m_b must be a list of lists")

    if not len(m_a) or all(len(arr) == 0 for arr in m_a):
        raise ValueError("m_a can't be empty")
    if not len(m_b) or all(len(arr) == 0 for arr in m_b):
        raise ValueError("m_b can't be empty")

    number_a = True

    for arr in m_a:
        for element in arr:
            if type(element) not in [int, float]:
                number_a = False
                break
        else:
            continue
        break

    if not number_a:
        raise TypeError("m_a should contain only integers or floats")

    number_b = True
    for arr in m_b:
        for element in arr:
            if type(element) not in [int, float]:
                number_b = False
                break
        else:
            continue
        break

    if not number_b:
        raise TypeError("m_b should contain only integers or floats")

    first_arr_len_a = len(m_a[0])
    if not all(first_arr_len_a == len(arr) for arr in m_a):
        raise TypeError("each row of m_a must be of the same size")

    first_arr_len_b = len(m_b[0])
    if not all(first_arr_len_b == len(arr) for arr in m_b):
        raise TypeError("each row of m_b must be of the same size")

    columns_b = len(m_b)
    rows_a = len(m_a[0])

    if rows_a != columns_b:
        raise ValueError("m_a and m_b can't be multiplied")

    a = np.array(m_a)
    b = np.array(m_b)
    res = a @ b
    ans = res.tolist()

    return ans
