#!/usr/bin/python3

"""A student class"""


class Student:
    """A class Student that defines a student with set attributes"""

    def __init__(self, first_name, last_name, age) -> None:
        """Initialize Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """converts the class to json"""

        return self.__dict__
