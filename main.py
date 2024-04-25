import requests

url = "https://api.github.com/users/elhunter1990"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response)
print(response.json())
print(response.json()['login'])
print(response.json()['url'])
print(response.json()['id'])



url = "https://api.weather.gov/points/25.994912538023797,-80.3390686"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

url = "https://api.weather.gov/gridpoints/MFL/103,60/forecast"

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

