#!/bin/bash
# sends a delete request to url passed as argument
curl -s "$1" -X DELETE
