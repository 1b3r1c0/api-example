#!/bin/python3

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#-----------------------------
# Retrieve data from a web page

# Create an SSL "contex" for urllib
# This will Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL to retrieve data from
url = "http://py4e-data.dr-chuck.net/comments_42.xml"

# Make an HTTP connection and make the request
uh = urllib.request.urlopen(url, context=ctx)

# put the response into a varible
data = uh.read()

# debug
# convert from a "byte" string to a unicode string
# data.decode()
 
#-----------------------------
# Extract XML data

# Create a py object from the XML data
tree = ET.fromstring(data)

# Use the "xml" module with an "Xpath expression" to return specified XML elements
# ".//<string>" selects all <string> elements in the entire tree
# Since this will find more than 1 elemment, this will be a list
results = tree.findall('.//count')

# Sum the numbers and print
print( sum( [ int(x.text) for x in results ] ) )

# debug = input("CTL+c to quit, RTN to continue")
# lat = results[0].find('geometry').find('location').find('lat').text
