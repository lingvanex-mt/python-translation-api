import requests

url = "https://api-b2b.backenster.com/b1/api/v3/translate"

payload = {
    "from": "en_GB",
    "to": "de_DE",
    "data": "London is the capital and largest city of England and of the United Kingdom.",
    "platform": "api"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Your authorization API key"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
