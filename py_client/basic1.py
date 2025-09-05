import requests

endpoint = "http://127.0.0.1:8000/api/"
response = requests.post(endpoint, json={"name": "Aditya"})

print("STATUS:", response.status_code)   # ✅ Should be 200
print("RAW TEXT:", response.text)        # ✅ {"name": "Aditya"}
print("PARSED JSON:", response.json())   # ✅ {'name': 'Aditya'}
