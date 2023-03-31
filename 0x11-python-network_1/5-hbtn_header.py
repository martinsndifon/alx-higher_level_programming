#!/usr/bin/python3
"""Displays the X-Request-Id of a url passed as argument"""

import requests
import sys


def main():
    result = requests.get(sys.argv[1])
    header = result.headers.get("X-Request-Id")

    print(header)


if __name__ == '__main__':
    main()
