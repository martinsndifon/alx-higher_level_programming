#!/usr/bin/python3
"""fetch the url https://alx-intranet.hbtn.io/status"""

import requests


def main():
    result = requests.get('https://alx-intranet.hbtn.io/status')
    content = result.text

    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))


if __name__ == '__main__':
    main()
