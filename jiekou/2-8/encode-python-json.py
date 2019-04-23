# coding:utf-8
import json

#python字典

payload = {
    'god':True,
    '群':False,
    'python':25125

}
data_json = json.dumps(payload,ensure_ascii=False)
print(type(payload))
print(payload)

print(type(data_json))
print(data_json)

dict_data = json.loads(data_json)
print(dict_data)
