# Weather API key:
# a50abde1c87f4cbc931162529232509
import requests

url = 'http://api.weatherapi.com/v1/current.json?key=a50abde1c87f4cbc931162529232509&q=98685&aqi=no'
response = requests.get(url)
city = response.json().get('location').get('name')
temp = response.json().get('current').get('temp_f')
tempC = response.json().get('current').get('temp_c')
description = response.json().get('current').get('condition').get('text')

print ("Temperature in", city, "is", temp, "F", "or", tempC, "C")
print ("The weather is", description)
