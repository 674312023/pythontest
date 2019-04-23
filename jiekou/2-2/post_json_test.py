# coding:utf-8
import requests
import json

payload = {'yoyo': 'hello word', 'python群': '1234567'}
print(type(payload))
data_json = json.dumps(payload)
print(type(data_json))
r = requests.post('http://httpbin.org/post', json=payload)
#r = requests.post('http://httpbin.org/post', json=data_json)
print(r.text)
#print(r.content)
