#!/usr/bin/python3


def number_keys(a_dictionary):
    if a_dictionary is None:
        return None

    i = 0

    for item in a_dictionary.keys():
        i += 1

    return i


'''
You can also use len(a_dictionary).
I just like custom functions for som weird reason
'''
