# tl;dr
# 
# Use urllib to convert a py dictionary into a URL encoded CGI URL
# 
# For example, here's the dictionary
# 
#   dict = {'address': 'South Federal University', 'key': 42}
# 
# Here's the command & output
#
#   urllib.parse.urlencode(dict)
#   ----------------------------- 
#   address=South+Federal+University&key=42

import urllib.parse

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = "South Federal University"

parms = dict()
parms['address'] = address
parms['key'] = api_key

print( "parms:",parms )
print("")

print( 'urllib.parse.urlencode(parms):' )
print( urllib.parse.urlencode(parms) )
print("")

print( "serviceurl + urllib.parse.urlencode(parms):" )
print( serviceurl + urllib.parse.urlencode(parms) ) 
