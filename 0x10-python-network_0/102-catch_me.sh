#!/bin/bash
# makes a request to a URL that causes the server to return with a message
curl -sL -H "origin: HolbertonSchool" -X PUT 0.0.0.0:5000/catch_me_3
