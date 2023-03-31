#!/usr/bin/python3

"""
Sends a request to passed URL and displays the body of the response
based on status_code
"""

import requests
import sys


def main():
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)


if __name__ == '__main__':
    main()
