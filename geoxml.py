#!/bin/python3

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as elmntTree
import ssl

# Define Constant: URL to retrieve data from
URL = " http://py4e-data.dr-chuck.net/comments_1123610.xml"

# Create an SSL "context" for urllib
# This will Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Make an HTTP connection and make the request
uh = urllib.request.urlopen(URL, context=ctx)

# put the response into a variable
data = uh.read()

# debug: convert from a "byte" string to a unicode string
# data.decode()

# Create a py object from the XML data
tree = elmntTree.fromstring(data)

# return specified XML elements  with an "Xpath expression" (xml module)
# ".//<string>" selects all <string> elements in the entire tree
# Since this will find more than 1 element, this will be a list
results = tree.findall('.//count')

# Sum the numbers and print
# Uses list comprehension
print(sum([int(x.text) for x in results]))

# debug = input("CTL+c to quit, RTN to continue")
# lat = results[0].find('geometry').find('location').find('lat').text
