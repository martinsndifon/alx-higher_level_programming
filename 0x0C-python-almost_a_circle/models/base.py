#!/usr/bin/python3

"""The base class for this project"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if not list_objs:
            with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
                f.write("[]")
        else:
            res = []
            for obj in list_objs:
                res.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation json_string"""
        if not json_string:
            return "[]"
        return json.loads(json_string)

