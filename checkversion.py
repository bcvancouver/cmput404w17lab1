#!/usr/bin/env python

from __future__ import print_function

import requests
# prints out version of request library
print(requests.__version__)

response = requests.get("https://raw.githubusercontent.com/bcvancouver/cmput404w17lab1/master/checkversion.py")

print(response.status_code)

print(response.text)