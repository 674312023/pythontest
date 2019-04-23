# coding:utf-8
import requests,json

payload = {'yoyo': 'hello word', 'python群': '1234567'}
r = requests.post('http://httpbin.org/post', data=payload)
print(type(r.content))
print(r.status_code)
r1 = r.json()
print(r1)
print(type(r1))
print(r1['url'])