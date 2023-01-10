#!/usr/bin/python3

"""Input/Output Module"""


def append_after(filename="", search_string="", new_string=""):
    """Append new_string if search_string is found"""

    _res = ""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            _res += line
            if search_string in line:
                _res += new_string

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(_res)
