#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    argc = len(argv) - 1

    if argc == 0:
        print("{}".format(argc))
    else:
        for item in range(1, argc + 1):
            sum += int(argv[item])
        print("{}".format(sum))


if __name__ == "__main__":
    main()
