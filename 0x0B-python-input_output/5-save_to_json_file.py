#!/usr/bin/python3


"""Object to text file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file, using a JSON representation"""

    with open(filename, mode="w", encoding="utf-8")as f:
        json.dump(my_obj, f)
