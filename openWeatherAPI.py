# Weather API key:
# a50abde1c87f4cbc931162529232509
# TODO This key expires often, though! Check for the new key in the account on -> weatherapi.com
import requests

weather_api_key = 'a50abde1c87f4cbc931162529232509'
zip = '98685'
url = 'http://api.weatherapi.com/v1/current.json?key=' + weather_api_key + '&q='+ zip +'&aqi=yes'
response = requests.get(url)
city = response.json().get('location').get('name')
temp = response.json().get('current').get('temp_f')
tempC = response.json().get('current').get('temp_c')
description = response.json().get('current').get('condition').get('text')

print ("Temperature in", city, "is", temp, "F", "or", tempC, "C")
print ("The weather is", description)
