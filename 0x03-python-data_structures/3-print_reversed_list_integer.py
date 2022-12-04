#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return

    my_list.reverse()
    for item in my_list:
        print("{:d}".format(item))
