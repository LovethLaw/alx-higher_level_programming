#!/bin/bash
# sends request to a url and displays the status code
curl -s -o /dev/dull/ -w "%{http_code}" "$1"
