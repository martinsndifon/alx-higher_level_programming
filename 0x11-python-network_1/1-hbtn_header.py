#!/usr/bin/python3
"""Displays the X-Request-Id of a url passed as argument"""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    header = response.getheader("X-Request-Id")

print(header)
