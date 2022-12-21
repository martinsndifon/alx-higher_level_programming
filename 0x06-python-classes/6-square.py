#!/usr/bin/python3


"""class definition"""


class Square:
    """A class definition of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if len(position) != 2 or not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Initialize the getter for size"""

        return self.__size

    @size.setter
    def size(self, size):
        """Initialize the setter for size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        """Get the field position value"""

        return self.__position

    @position.setter
    def position(self, position):
        """Set the field position value"""

        if len(position) != 2 or not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        """Compute the area of the square."""

        return self.__size * self.__size

    def my_print(self):
        """print the square using '#' symbol"""

        i = 0
        if not self.__size:
            print()
            return
        print('\n' * self.__position[1], end='')
        for i in range(self.size):
            s = '#' * self.size
            print(' ' * self.__position[0], end='')
            print(s)
