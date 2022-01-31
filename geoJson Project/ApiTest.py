# Made by Jesus Ugarte to test API for Interview

import requests

# Example : Orlando FLorida Coordinate Example
#longitude = -81.379234
#latitude = 28.538336

print("Hello Ryan, Welcome to my Python API Tester\n")
longitude = float(input("Please enter longitude: \n"))
latitude = float(input("Please enter latitude: \n"))

url = 'https://interviewresourcename.azure-api.net/isUrban/IsUrban'
myobj = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [longitude, latitude]
            }
        }

response = requests.post(url, json = myobj)

print(response.text)