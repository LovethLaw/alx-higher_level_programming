#!/bin/bash
# takes url, sends POST request to the url and displays body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
