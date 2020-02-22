from requests import get

url = "http://localhost:8123/ENDPOINT"
headers = {
    "Authorization": "Bearer ABCDEFGH",
    "content-type": "application/json",
}

response = get(url, headers=headers)
print(response.text)