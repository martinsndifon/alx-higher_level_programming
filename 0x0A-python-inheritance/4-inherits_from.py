#!/usr/bin/python3

"""Inherits_from module"""


def inherits_from(obj, a_class):
    """checks if obj is a subclass of a_class"""

    return not type(obj) is a_class and issubclass(type(obj), a_class)
