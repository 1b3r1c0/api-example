#!/bin/python3

import urllib.request
import urllib.error
import json
import ssl
# I don't think this module is used
# import urllib.parse

# Define Constants
# URL to retrieve data from
# Sample: URL = "http://py4e-data.dr-chuck.net/comments_42.json"
URL = "http://py4e-data.dr-chuck.net/comments_1123611.json"

# Create an SSL "context" for urllib
# This will Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Make an HTTP connection and make the request 
uh = urllib.request.urlopen(URL, context=ctx)

# put the response into a variable
data = uh.read()

# The json library Converts raw JSON into a python dictionary of nested lists & dictionaries
# It doesn't convert the raw data into an object like xml.etree does for XML
info = json.loads(data)
# The data structure will be something like nested dictionaries in nested lists in a dictionary

# The value corresponding to the 'comments' key is a list that's iterated over
# each element of that list is a nested dictionary
# We want the "count: <number>" key/value pair from that nested dictionary
# List comprehension
print(sum([x['count'] for x in info['comments']]))
#    debug = input("CTL+c to quit, RTN to continue")
