# coding:utf-8
import requests
import json

payload = {'yoyo': 'hello word', 'python群': '1234567'}
data_json = json.dumps(payload)
r = requests.post('http://httpbin.org/post', json=data_json)
print(r.content)