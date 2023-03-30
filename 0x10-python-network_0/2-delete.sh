#!/usr/bin/env bash
# takes in a URL, sends a DELETE request to that URL, and displays the
# body of the response

curl -sX DELETE "$1"
