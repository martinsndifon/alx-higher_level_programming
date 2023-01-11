#!/usr/bin/python3

"""Add Attribute Module"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it is possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
