import requests

url = "http://127.0.0.1:5000/recommend"

data = {
    "user_id": 1,
    "symptom": "diabetes"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())