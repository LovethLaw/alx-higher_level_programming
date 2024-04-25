#!/bin/bash
# takes a url as argument, sends GET request to url, displays body of response
curl -s "$1" -H "X-School-User-Id: 98"
