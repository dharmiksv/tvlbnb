# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:54:14 2019

@author: dharmiksv
"""

import requests

payload = "client_id=wf5u9zaqksgeb7stzrq6cy2m&client_secret=xrfaTNrdtp&grant_type=client_credentials"



"""auth_headers = {
        "client_id=wf5u9zaqksgeb7stzrq6cy2m",
        "client_secret=xrfaTNrdtp",
        "grant_type=client_credentials"}"""

"""
-------Curl Statement-----
curl "https://api.lufthansa.com/v1/oauth/token" -X POST -d "client_id=wf5u9zaqksgeb7stzrq6cy2m" -d "client_secret=xrfaTNrdtp" -d "grant_type=client_credentials
"""

auth_url = "https://api.lufthansa.com/v1/oauth/token"
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
#response = requests.request("GET", city_url, data=payload, headers=headers, params=querystring)
response_token = requests.request("POST", auth_url,data=payload, headers=headers)
print(response_token.json())

token            = {
    'Authorization': 'bearer ' + response_token.json()['access_token'],
    'accept': "application/json"
    }

city_url = "https://api.lufthansa.com/v1/mds-references/cities/BER?limit=20&offset=0"

response = requests.request("GET", city_url, data=None, headers=token, params=None)

city_response = response.json()

print(response.text)
