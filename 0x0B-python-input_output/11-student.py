#!/usr/bin/python3

"""A student class"""


class Student:
    """A class Student that defines a student with set attributes"""

    def __init__(self, first_name, last_name, age) -> None:
        """Initialize Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """converts the class to json"""

        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all students value with json value"""

        for k, v in json.items():
            self.__dict__[k] = v
