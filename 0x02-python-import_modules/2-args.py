#!/usr/bin/python3
import sys


def main():
    i = 1
    lenght = len(sys.argv) - 1

    if lenght == 0:
        print("{:d} arguments.".format(lenght))
    elif lenght == 1:
        print("{:d} argument:".format(lenght))
        print("{}: {}".format(lenght, sys.argv[1]))
    else:
        print("{:d} arguments:".format(lenght))
        while i <= lenght:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1


if __name__ == "__main__":
    main()
