#!/usr/bin/python3

"""A rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from another class(BaseGeometry)"""

    def __init__(self, width, height):
        """Instantiation of Rectangle"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
