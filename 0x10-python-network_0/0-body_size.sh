#!/bin/bash
# takes url, sends url request, returns size of body of response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
