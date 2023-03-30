#!/bin/bash
# sends a JSON POST request to a URL and displays the body of the response
body=$(cat $2); curl -s --header "Content-Type: application/json" -X POST -d "$body" "$1"
