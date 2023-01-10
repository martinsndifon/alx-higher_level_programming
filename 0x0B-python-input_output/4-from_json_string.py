#!/usr/bin/python3


"""A module to return an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Return the object represented by a JSON string"""

    return json.loads(my_str)
