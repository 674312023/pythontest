# coding:utf-8

import requests

par = {"Keywords": "yoyoketang"}
r = requests.get('http://zzk.cnblogs.com/s/blogpost', params=par)
#r = requests.get('http://www.baidu.com/')
#print(r.url)
print(r.status_code)
#print(r.text)
#print(type(r.cookies))
print(r.raw)
print(r.cookies)
