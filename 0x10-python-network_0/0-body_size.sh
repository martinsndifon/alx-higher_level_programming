#!/bin/bash
# Sends a request to a URL, and displays the size of the body of the response
curl -sI "$1" | grep -iF "content-length" | cut -d " " -f 2
