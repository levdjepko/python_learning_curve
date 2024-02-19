# there is an open API that gets the people who are currently in space
# we need to use an HTTP request to this open API:

import requests

# API endpoint is http://api.open-notify.org/astros.json (http://open-notify.org/Open-Notify-API/People-In-Space/)
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

for person in json['people']:
    print (person['name'])
