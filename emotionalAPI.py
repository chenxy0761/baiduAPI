# -*- coding:utf-8 -*-

import requests
import json
import jsonpath

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=24.0a5cfd84db329d3ff26af08885eac866.2592000.1526720122.282335-11126907'
body = {
    "text": "充分发挥不要脸的精神。"
}
headers = {'content-type': "application/json", }

# print type(body)
# print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
response = requests.post(url, data=json.dumps(body), headers=headers)
# 也可以直接将data字段换成json字段，2.4.3版本之后支持
# response  = requests.post(url, json = body, headers = headers)

# 返回信息
print response.text
# 把json格式字符串转换成python对象
jsonobj = json.loads(response.text)

# 从根节点开始，匹配name节点
citylist = jsonpath.jsonpath(jsonobj,'$..sentiment')
text = jsonpath.jsonpath(jsonobj,'$..text')
confidence = jsonpath.jsonpath(jsonobj,'$..confidence')
# citylist = jsonpath.jsonpath(jsonobj,'$..sentiment')
# citylist = jsonpath.jsonpath(jsonobj,'$..sentiment')
#
print(text)
print(confidence)
print citylist
# print type(citylist)
# fp = open('city.json','w')
#
# content = json.dumps(citylist, ensure_ascii=False)
# print content
#
# fp.write(content.encode('utf-8'))
# fp.close()
