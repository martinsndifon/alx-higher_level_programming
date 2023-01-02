#!/usr/bin/python3


"""class definition"""


class Rectangle:
    """An empty class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle width and height"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Initialize width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """Initialize width setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Initialize height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """Initialize height setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """computes the area of the rectangle"""

        area = self.__height * self.__width
        return area

    def perimeter(self):
        """computes the perimeter of the rectangle"""

        if not self.__height or not self.__width:
            return 0

        p = 2 * (self.__height + self.__width)
        return p
