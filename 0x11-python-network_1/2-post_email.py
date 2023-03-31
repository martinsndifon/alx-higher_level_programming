#!/usr/bin/python3

"""
Sends a POST request to passed URL with email as parameter and displays
the body of the response
"""

import urllib.request
import urllib.parse
import sys


def main():
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        byte = response.read()
    print(byte.decode())


if __name__ == '__main__':
    main()
