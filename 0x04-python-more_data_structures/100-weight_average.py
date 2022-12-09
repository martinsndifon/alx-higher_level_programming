#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight = 0
    sum = 0
    for a, b in my_list:
        sum += a * b
        weight += b
    return sum / weight
