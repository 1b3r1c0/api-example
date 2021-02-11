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

API_KEY = 42
SERVICE_URL = 'http://py4e-data.dr-chuck.net/json?'
ADDRESS = "South Federal University"

parms = dict()
parms['address'] = ADDRESS
parms['key'] = API_KEY

print("parms:", parms, "\n")

print('urllib.parse.urlencode(parms):')
print(urllib.parse.urlencode(parms), "\n")

print("serviceurl + urllib.parse.urlencode(parms):")
print(SERVICE_URL + urllib.parse.urlencode(parms))
