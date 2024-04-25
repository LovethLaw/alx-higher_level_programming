#!/bin/bash
# sends json POST request to the url, displays the body of the response
curl -s "$1" -d @"$2" -X POST -H "Content-Type: application/json"
