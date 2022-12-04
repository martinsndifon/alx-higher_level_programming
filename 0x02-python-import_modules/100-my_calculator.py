#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    argc = len(argv)

    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], add(a, b)))
    elif argv[2] == '-':
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], sub(a, b)))
    elif argv[2] == '*':
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], mul(a, b)))
    elif argv[2] == '/':
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
