#!/usr/bin/python3

"""A Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of an instance of the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the value of the instance field, size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of the instance field, size"""
        self.width = value
        self.height = value
