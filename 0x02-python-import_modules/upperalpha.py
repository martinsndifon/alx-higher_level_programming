#!/usr/bin/python3
for i in range(65, 91):
    if i != 90:
        print("{}".format(chr(i)), end='')
    else:
        print("{}".format(chr(i)))

'''
you can also write it this way with import
from string import ascii_uppercase
print(ascii_uppercase)
'''
