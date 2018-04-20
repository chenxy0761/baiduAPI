# -*- coding:utf-8 -*-

import requests
import json

client_id = '8BXRM0rGAbVGFvmMqsv5lse3'
client_secret = 'GNlhve6aNxLjSQKptXgnYuOf8OHKquYq'
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
# body = {
#     "text": "一般，用料较差，总控太塑料感太强，做工不错。"
# }
headers = {'content-type': "application/json", }

# print type(body)
# print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
response = requests.post(url, headers=headers)
# 也可以直接将data字段换成json字段，2.4.3版本之后支持
# response  = requests.post(url, json = body, headers = headers)

# 返回信息
print response.text
# 返回响应头
# print response.status_code
