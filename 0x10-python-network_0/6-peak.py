#!/usr/bin/python3
"""Find peak module"""


def find_peak(list_of_integers):
    """Find the peak in a list of unsorted integers"""
    lst = list_of_integers
    size = len(lst)
    if not lst or size == 2:
        return None
    if size == 1:
        return lst[0]
    if lst[0] >= lst[1]:
        return lst[0]
    if lst[size - 1] >= lst[size - 2]:
        return lst[size - 1]

    for i in range(1, size - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            return lst[i]
    return lst[0]
