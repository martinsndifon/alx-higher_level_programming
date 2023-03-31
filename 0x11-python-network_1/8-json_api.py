#!/usr/bin/python3

"""
Sends a POST request to passed URL with a letter as parameter and displays
the body of the response
"""

import requests
import sys


def main():
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = {'q': ""}
    else:
        q = {'q': sys.argv[1]}
    res = requests.post(url, data=q)
    try:
        obj = res.json()
        if not obj:
            print('No result')
        else:
            print(f"[{obj.get('id')}] {obj.get('name')}")
    except Exception:
        print('Not a valid JSON')


if __name__ == '__main__':
    main()
