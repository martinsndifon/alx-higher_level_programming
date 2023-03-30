#!/usr/bin/env bash
# takes in a URL, sends a GET request to that URL, and displays the
# body of the response only if response code is 200

curl -sL "$1"
