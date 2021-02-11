import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# User defined constants
API_KEY = 42
SERVICEURL = 'http://py4e-data.dr-chuck.net/json?'
ADDRESS = "Missouri University of Science and Technology"
PLACE_ID_STARTSWITH = "ChIJr3S"

# Ignore SSL certificate errors
# See previous notes about this SSL context 
sslContext = ssl.create_default_context()
sslContext.check_hostname = False
sslContext.verify_mode = ssl.CERT_NONE

# Use urllib to convert a py dictionary into a CGI URL
# For example: address=South+Federal+University&key=42
# urllib.parse.urlencode requires a dictionary as input
urlParameters = dict()
urlParameters['address'] = ADDRESS
urlParameters['key'] = API_KEY
url = SERVICEURL + urllib.parse.urlencode(urlParameters)

print('Retrieving', url)
# see previous notes about using urllib for HTTP GET & responses
urllibHandle = urllib.request.urlopen(url, context=sslContext)
data = urllibHandle.read().decode()
print('Retrieved', len(data), 'characters')

try:
    # Convert JSON string into py dict/list
    jsonDict = json.loads(data)
except NameError:
    jsonDict = None

if not jsonDict or 'status' not in jsonDict or jsonDict['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

# TIP: Open the retrieved JSON file in Vim and use text folding to determine how to reference 'place_id'
# In Vim
# :set filetype=json
# :syntax on
# :set foldmethod=syntax
# zo, zc & za (while cursor is on fold point)
print("Place id:", jsonDict['results'][0]['place_id'])
# debug print( "place_id_startswith:", place_id_startswith )

# debug     print(json.dumps(js, indent=4))
# debug junk = input("CTL-c to quit, RTN to continue")
