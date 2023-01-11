#!/usr/bin/python3

"""base_geometry module"""


class BaseGeometry:
    """defines the new empty class"""

    def area(self):
        """computes the area of a geometric object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the type of value(int)"""

        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
