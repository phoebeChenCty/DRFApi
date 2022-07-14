import requests

# endpoint = "http://httpbin.org/anything" # the url that this client talk to

endpoint = "http://127.0.0.1:8000/"

# get_response = requests.get(endpoint) # library API

# we want to build REST api, a web api
# this python client, just like browser. It set http request and get data from server

# print(get_response.text) # print the html(normal http request)/json(rest api http request) of that page
# print(get_response.json()) # print the json as python dict (null->None)

# get_response = requests.get(endpoint, json={"query":"Hello world"})
# print(get_response.json()) # echo back, show in 'data'

# get_response = requests.get(endpoint, data={"query":"Hello world"})
# print(get_response.json()) # echo back, show in 'form'

get_response = requests.get(endpoint) #, json={"query":"Hello world"})
print(get_response.text)
print(get_response.status_code) # 200 means success, 404 means not found