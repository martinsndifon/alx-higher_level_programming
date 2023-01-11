#!/usr/bin/python3

"""A module Square that inherits from the module Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from rectangle"""

    def __init__(self, size):
        """Instantiation with size"""

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """computes the area of the square"""

        return self.__size ** 2

    def __str__(self):
        """prints string representation of module"""

        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
