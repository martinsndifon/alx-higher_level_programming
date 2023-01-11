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

    def area(self):
        """Implements the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
