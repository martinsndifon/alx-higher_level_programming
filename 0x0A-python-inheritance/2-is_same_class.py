#!/usr/bin/python3

"""is_same_class module"""


def is_same_class(obj, a_class):
    """returns true is the object is exactly an instance of the specified
    class otherwise false"""

    return type(obj) is a_class
