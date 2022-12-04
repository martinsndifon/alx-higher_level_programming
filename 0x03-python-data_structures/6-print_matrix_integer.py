#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return

    for a,b,c in matrix:
        print("{:d}".format(a), end=' ')
        print("{:d}".format(b), end=' ')
        print("{:d}".format(c))
