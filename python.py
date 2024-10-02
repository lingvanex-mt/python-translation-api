import requests

url = "https://api-b2b.backenster.com/b1/api/v3/translate"

payload = { "platform": "api" }
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
