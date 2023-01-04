#!/usr/bin/python3


"""
A module that prints two new lines after the characters . ? and :
"""


def text_indentation(text):

    """
    prints two new lines after the characters . ? and :
    - text must be a string
    - No spaces at the beginning or at the end of each printed line
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(f'{text[i]}', end='')
            print('\n')
            i += 1
            if i < len(text):
                if text[i] == ' ':
                    i += 1
                else:
                    continue
        else:
            print(f'{text[i]}', end='')
            i += 1
