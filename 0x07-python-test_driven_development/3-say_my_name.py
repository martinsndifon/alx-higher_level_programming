#!/usr/bin/python3


"""
A module that prints first_name and last_name, with last_name as an
optional argument
"""


def say_my_name(first_name, last_name=""):

    """
    This module prints your first and last names
    - last_name is an optional argument
    - if both names are not strings, the program raises a type error
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f'My name is {first_name} {last_name}')
