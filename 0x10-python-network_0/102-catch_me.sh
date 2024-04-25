#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me that causes server responds
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
