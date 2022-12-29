#!/usr/bin/python3


"""
A module that prints a square using the '#' symbol
"""


def print_square(size):

    """
    prints a square uning the '#' symbol with size, size
    - size must be an integer
    - size must be greater than or less than 0
    - size cannot be of type float
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print(f'#' * size)
