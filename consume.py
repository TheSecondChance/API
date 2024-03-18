import requests


res = requests.get('http://127.0.0.1:8000/personDetail/1')


for key, value in res.json().items():
    print(key, value)