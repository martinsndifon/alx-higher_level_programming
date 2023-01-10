#!/usr/bin/python3
import json

"""A module that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """returns the JSON representation of an object"""

    s = json.dumps(my_obj)
    return s
