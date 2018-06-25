# coding:utf-8
import requests

#python字典
url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


s = requests.session()
r = s.get(url, headers=headers, verify=False)
print(r.content)
result = r.json()
data = result['data']  # 获取 data 里面内容
print(r.encoding)
print(data)
print(data[0])  # 获取 data 里最上面有个
print(data[0]['context'])
need_result = data[0]['context']  #获取签收状态
#print(type(data[0]))
if '已签收' in need_result:
    print('签收成功了')
else:
    print('没有签收成功')