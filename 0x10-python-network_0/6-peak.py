#!/usr/bin/python3
"""Find peak module"""


def find_peak(list_of_integers):
    """Find the peak in a list of unsorted integers"""
    lst = list_of_integers
    n = len(lst)
    if n == 0 or n == 2:
        return None

    for i in range(1, n - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            return lst[i]
    return lst[0]
