# coding:utf-8
import  requests

url = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

s = requests.session()
r = s.get(url, headers=headers, verify=False,allow_redirects=False)
print(r.status_code)
print(r.headers['Location'])
