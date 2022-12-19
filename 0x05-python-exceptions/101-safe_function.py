#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        sys.stderr.write('Exception: ')
        sys.stderr.write(str(err))
        sys.stderr.write('\n')
        return None
    return result
