# coding:utf-8
import requests

# 先打开登录首页，获取部分 cookie
url = "http://localhost:8080/jenkins/j_acegi_security_check"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

d = {"j_username": "674312023",
     "j_password": "20110678lsh",
     "from": "/",
     "Jenkins-Crumb": "7fea2823037a593d417101741e50abb9",
     "json": {"j_username": "674312023", "j_password": "20110678lsh", "remember_me": False, "from": "/",
              "Jenkins-Crumb": "7fea2823037a593d417101741e50abb9"},
     "Submit": "登录"
     }
# print(d['json'])
s = requests.session()
r = s.post(url, headers=headers, data=d)
#print(r.text)
print(r.content)
# 正则表达式提取账号和登录按钮
import re
r1 = re.findall(r'<b>(.+?)</b>',r.text)
print(r1)
