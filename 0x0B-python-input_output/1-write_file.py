#!/usr/bin/python3


"""writing to a file"""


def write_file(filename="", text=""):
    """writes to filename, the text contained in text"""

    with open(filename, mode="w", encoding="utf-8") as f:
        i = f.write(text)
        return i
