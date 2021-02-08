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

urlParameters = dict()
urlParameters['address'] = ADDRESS
urlParameters['key'] = API_KEY

# Ignore SSL certificate errors
# See previous notes about this SSL context 
sslContext = ssl.create_default_context()
sslContext.check_hostname = False
sslContext.verify_mode = ssl.CERT_NONE

# Use urllib to convert a py dictionary into a CGI URL
# address=South+Federal+University&key=42
url = SERVICEURL + urllib.parse.urlencode(urlParameters)

print('Retrieving', url)
# see previous notes about usign urllib for HTTP GET & responses
urllibHandle = urllib.request.urlopen(url, context=sslContext)
data = urllibHandle.read().decode()
print('Retrieved', len(data), 'characters')

try:
    # Convert JSON string into py dict or list
    jsonDict = json.loads(data)
except:
    jsonDict = None

if not jsonDict or 'status' not in jsonDict or jsonDict['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

# debug     print(json.dumps(js, indent=4))
# debug junk = input("CTL-c to quit, RTN to continue")

# Used "text" folding in Vim to find where place_id was in the large JSON file
# :set filetype=json
# :syntax on
# :set foldmethod=syntax
# zo, zc & za (while cursor is on fold point)
#
print("Place id:", jsonDict['results'][0]['place_id'])
# print( "place_id_startswith:", place_id_startswith )
