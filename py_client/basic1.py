import requests

endpoint = "http://127.0.0.1:8000/api"

get_responce = requests.get(endpoint,json={"data":"hellow World"})

print(get_responce.text)
print(get_responce.json()["message"])
print(get_responce.status_code)

