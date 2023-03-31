#!/usr/bin/python3

"""
Sends a POST request to passed URL with email as parameter and displays
the body of the response
"""

import requests
import sys


def main():
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    res = requests.post(url, data=email)
    print(res.text)


if __name__ == '__main__':
    main()
