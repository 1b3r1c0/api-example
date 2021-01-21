#!/bin/python3

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#-----------------------------
# Retrieve data from a web page

# Create an SSL "contex" for urllib
# This will Ignore SSL certificate errors
ctx = ssl.create_default_context() 
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE 

# URL to retrieve data from 
# Sample
# url = "http://py4e-data.dr-chuck.net/comments_42.json"
# graded
url = "http://py4e-data.dr-chuck.net/comments_1123611.json"

# Make an HTTP connection and make the request 
uh = urllib.request.urlopen(url, context=ctx) 

# put the response into a varible 
data = uh.read()

# debug 
# convert from a "byte" string, or more likely a UTF-8 string, into a unicode string 
# data.decode() 

#----------------------------- 
# Extract JSON data 

# The json library Converts raw JSON into a python dictionary of nested lists & dictionaries
# It doesn't convert the raw data into an object like the etree lib does for XML
info = json.loads(data)
# The data structure will be somewhat complex, for example:
# nested dictionaeries in nested lists in a dictionary

# The value corresponding to the 'comments' key is a list that's iterated over
# each element of that list is a nested dictionary
# We want the "count: <number>" key/value pair from that nested dictionary
print( sum( [ x['count'] for x in info['comments'] ] ) )
#    debug = input("CTL+c to quit, RTN to continue") 

