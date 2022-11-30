#!/usr/bin/python3

def uppercase(str):
    new_string = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            new_string += chr((ord(letter) - 32))
        else:
            new_string += letter
    print("{}".format(new_string))
