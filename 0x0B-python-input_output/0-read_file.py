#!/usr/bin/python3


"""This module reads from a file"""


def read_file(filename=""):
    """Reads and prints to standard output the content of filename"""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
