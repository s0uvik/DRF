# this way we can consume API in python

import requests

# endpoint = "https://httpbin.org/anything/"
endpoint = "http://127.0.0.1:8000/api/"

response = requests.get(endpoint, params={"abc": 432}, json={"query": "Hello from client"})

# print(response.text)
print("Status code of API response: ",response.status_code)
print(response.json())
# print(response.status_code)

# HTTP request => HTML
# REST API HTTP request => JSON