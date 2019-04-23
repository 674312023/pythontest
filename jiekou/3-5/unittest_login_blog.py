# coding:utf-8
import json
import unittest,requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class BlogLogin(unittest.TestCase):

    def login(self, user, pwd, reme=True):
        '''三个参数：账号： username，密码： psw,记住登录： reme=False'''
        url = "https://passport.cnblogs.com/user/signin"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           "Accept-Language": 'zh-CN,zh;q=0.8',
           "Accept-Encoding": 'gzip, deflate, br',
           "Content-Type":  'application/json; charset=UTF-8',
           "X-Requested-With": 'XMLHttpRequest',
           "Cookie": '__gads=ID=b37919386478dba9:T=1497232460:S=ALNI_MaViCeDh5X-pbkCg8RcDs5DJ9U3BA; pgv_pvi=323950592; UM_distinctid=160d514d75d2e7-056d5b5d5d58cf-6b1b1279-13c680-160d514d75e7c5; Hm_lvt_444ece9ccd5b847838a56c93a0975a8b=1520407355; __utma=226521935.214876567.1491875711.1521793673.1524213886.5; __utmz=226521935.1524213886.5.2.utmcsr=so.com|utmccn=(organic)|utmcmd=organic|utmctr=python%20pickle%E6%A8%A1%E5%9D%97; __guid=162291773.3264445550285863000.1524644067956.6982; _ga=GA1.2.214876567.1491875711; ASP.NET_SessionId=01uikgwjczpijbn5aq2l4jfk; monitor_count=1; SERVERID=34e1ee01aa40e94e2474dffd938824db|1529378011|1529377966',
           'Connection': 'keep-alive'
            }

        json_data = {"input1": 'username1',
           "input2": 'pwd1',
           "remember":reme}

        res = requests.post(url, headers=headers, json=json_data, verify=False)
        result = res.content
        print(res.json())
        return res.json()


    def test01(self):
        '''测试登录：正确账号，正确密码'''
        username = "YbPsocKCiNoelaN/EyQY3KEFoEkR83iHm3vEi/3c4+UmuwmBdIPVss2QIeW0uM8qLY4eO1stDGH2iWsHH/e3W6lHmcKe/oD9KjNz6Ao/2vqSDIGp5ef5yL2E+jVVwLl8JY6wN1AZ6zoDw+okqk2I2PzG3ZYKm2ZXbIsGPjPOmFU="
        pwd = "WS9qoIuruw+1xOKXSUCt0yCmdaEKI7BxrreDmDRzGLf75htEdUh04Rg8Vgj9hoOfvbkPaO7jZC2yNVLaTpsf8gBTh2GTsLDnlL0rty8Ifkzr2jfvW2mN6Hu2DNohhYtyrwzYMdE+0RNgajAkJpFC+J9zl6Yn3kDxpntcO5IacE8="
        result1 = self.login(username, pwd)
        self.assertEqual(result1["success"], True)

if __name__ =='__main__':
    unittest.main()