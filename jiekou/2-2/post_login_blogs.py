# coding:utf-8
import requests,json
url = 'https://passport.cnblogs.com/user/signin'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           "Accept-Language": 'zh-CN,zh;q=0.8',
           "Accept-Encoding": 'gzip, deflate, br',
           "Content-Type":  'application/json; charset=UTF-8',
           "X-Requested-With": 'XMLHttpRequest',
           "Cookie": '__gads=ID=b37919386478dba9:T=1497232460:S=ALNI_MaViCeDh5X-pbkCg8RcDs5DJ9U3BA; pgv_pvi=323950592; UM_distinctid=160d514d75d2e7-056d5b5d5d58cf-6b1b1279-13c680-160d514d75e7c5; Hm_lvt_444ece9ccd5b847838a56c93a0975a8b=1520407355; __utma=226521935.214876567.1491875711.1521793673.1524213886.5; __utmz=226521935.1524213886.5.2.utmcsr=so.com|utmccn=(organic)|utmcmd=organic|utmctr=python%20pickle%E6%A8%A1%E5%9D%97; __guid=162291773.3264445550285863000.1524644067956.6982; _ga=GA1.2.214876567.1491875711; _gid=GA1.2.1990747426.1528164450; ASP.NET_SessionId=1dpvtf23zcelnhkct1ltdaie; monitor_count=1; SERVERID=34e1ee01aa40e94e2474dffd938824db|1528361085|1528361001',
           'Connection': 'keep-alive'
            }
payload = {"input1": "XX+76cmCpzF0Qvr9BHCC+D+0CS8U4CPOIdq/T5E+6owxkOjvZBPWAweUwf2VfseekRRST0nSfQqJhvIUYllW+Z7YVB7la3bwhIqcrSRYWWN+8cXxQ4fPsuxDD4fpDuBsiVngVFdZwQtQdmZvZl679Vc9O+osGkBAt4quxGxIc3I=",
           "input2": "mLetz6xk1flkU/wgj3NpDMIaSwohR+TnNEKWhZ/02cytIrAcrwzdBOVwyxl6zoPYMEnsY3d+1KAVKB+YyWnNLu9YKB6BUkSdhX+LzQtte4F/ZnMaXL/UW6soMm+ZBK6ze2ZRxuu1bdeaPsBeQ5FH62VJmxkaHa7eAV0v3UgtHkQ=",
           "remember": False}
#data_json = json.dumps(payload)
r = requests.post(url, json=payload, headers=headers, verify=False)
print(type(r.content))
print(type(r.json()))
print(r.status_code)
