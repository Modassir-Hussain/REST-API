import requests

BASE_URL = 'http://127.0.0.1:8000/'

END_POINT = 'api/'

response = requests.delete(BASE_URL+END_POINT)

data = response.json()

print(data)