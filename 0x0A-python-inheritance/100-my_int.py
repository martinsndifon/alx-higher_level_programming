#!/usr/bin/python3

"""A rebel module"""


class MyInt(int):
    """A module that inherits from the int class"""

    def __eq__(self, __x: object):
        """Returns False if two MyInt is equal"""
        return not super().__eq__(__x)

    def __ne__(self, __x: object):
        """Returns True if two MyInt is equal"""
        return not super().__ne__(__x)
