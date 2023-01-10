#!/usr/bin/python3


"""append a string to a file"""


def append_write(filename="", text=""):
    """appends to filename, the text contained in text"""

    with open(filename, mode="a+", encoding="utf-8") as f:
        i = f.write(text)
        return i
