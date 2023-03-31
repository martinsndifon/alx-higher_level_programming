#!/usr/bin/python3

"""
Sends a POST request to passed URL with email as parameter and displays
the body of the response. Handles urllib.error.HTTPError
"""

import urllib.request
import sys


def main():
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            byte = response.read()
        print(byte.decode())
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    main()
