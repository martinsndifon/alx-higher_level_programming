#!/usr/bin/python3


"""A module that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object"""

    s = json.dumps(my_obj)
    return s
