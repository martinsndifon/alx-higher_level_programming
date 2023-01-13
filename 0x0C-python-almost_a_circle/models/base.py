#!/usr/bin/python3

"""The base class for this project"""


class Base:
    """The base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
