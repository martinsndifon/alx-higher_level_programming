#!/usr/bin/python3


"""class definition"""


class Rectangle:
    """An empty class that defines a Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def print(self):
        """print string representation of the rectangle"""
        if not self.__width or not self.__height:
            return
        for i in range(self.__height):
            print(str(self.print_symbol) * {}.format(self.__width))

    def __str__(self):
        """Return string representation of the rectangle"""
        if not self.__width or not self.__height:
            return ""
        i = 0
        res = ""
        while i < self.__height:
            res += str(self.print_symbol) * self.__width
            res += "\n"
            i += 1
        return res[:len(res) - 1]

    def __repr__(self) -> str:
        """Return string representation of an object"""
        return f"Rectangle({self.__width}, {self.__height})"

    @classmethod
    def eval(cls, obj):
        """Converts string representation of an object to an object"""
        w, h = obj.split()
        w = w[10:]
        w = int(w[:len(w) - 1])
        h = int(h[:len(h) - 1])

        return cls(w, h)

    def __del__(self):
        """Tells us when an object is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle of two rectangles"""

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
