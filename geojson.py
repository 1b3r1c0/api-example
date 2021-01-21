import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
# See previous notes about this SSL context 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# This while loop is not really being used
while True:

    address = input("Enter location: ")
    address = "Missouri University of Science and Technology"
    # address = "South Federal University"
    place_id_startswith = "ChIJr3S"

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key

    # Use urllib to convert a py dictionary into a CGI URL
    # address=South+Federal+University&key=42
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    # see previous notes about usign urllib for HTTP GET & responses
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        # Convert JSON string into py dict or list
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # debug     print(json.dumps(js, indent=4))
    # debug junk = input("CTL-c to quit, RTN to continue")


    # Used "text" folding in Vim to find where place_id was in the large JSON file
    # :set filetype=json
    # :syntax on
    # :set foldmethod=syntax
    # zo, zc & za (while cursor is on fold point)
    #
    print( "Place id:", js['results'][0]['place_id'] )
    # print( "place_id_startswith:", place_id_startswith )
    
    # I totally mangled the logic for this while loop
    break
