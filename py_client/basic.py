import requests

endpoint = "https://httpbin.org"  #HTTP request

 #API : Application programing interface


endpoint = "https://httpbin.org/anything"

get_responce = requests.get(endpoint,json = {"query":"Hellow World"}) #JSON responce

print(get_responce.text) #as we are useing json responce we will print in from of JSON 
print(get_responce.json()) #as we are useing json responce we will print in from of JSON

print(get_responce.status_code)
 
'''
HTTP Request -> will return -> HTML
REST API HTTP Request -> will return -> JSON
'''