#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for item in my_list:
            i += 1

        if x > i:
            x = i

        j = 0
        while j < x:
            print(my_list[j], end='')
            j += 1
        print()

        return j
    except SyntaxError:
        pass
