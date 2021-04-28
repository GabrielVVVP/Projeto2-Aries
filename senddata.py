#!/usr/bin/env python3
# importing the requests library
import requests
  
# defining the api-endpoint 
parameter = "6"
API_ENDPOINT = "http://localhost:8000/api/values/"+parameter+"/"
print(API_ENDPOINT)
  
# data to be sent to api
data = {
        "readings": "9.1,15.3",
        "dates": "19:46:35,19:46:36"
        }
  
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)