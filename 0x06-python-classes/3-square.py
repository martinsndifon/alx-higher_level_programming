#!/usr/bin/python3


"""class definition"""


class Square:
    """A class definition of a square"""
    def __init__(self, size=0):
        """Initialize the square size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Compute the area of the square."""

        return self.__size * self.__size
