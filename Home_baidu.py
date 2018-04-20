# -*- coding:utf-8 -*-
import json
import urllib2

import jsonpath

response = urllib2.urlopen(
    'http://api.map.baidu.com/place/v2/search?query=电影院&location=31.151923,121.421885&radius=3000&output=json&ak=8xPapMW0KjwusZa6rDxnvqtTdIRBaZqO')
data = json.load(response)
print(data)
re = jsonpath.jsonpath(data, '$..results')
i = 0
while i < len(re[0]):
    province = jsonpath.jsonpath(re[0][i], '$..province')
    city = jsonpath.jsonpath(re[0][i], '$..city')
    name = jsonpath.jsonpath(re[0][i], '$..name')
    area = jsonpath.jsonpath(re[0][i], '$..area')
    telephone = jsonpath.jsonpath(re[0][i], '$..telephone')
    detail = jsonpath.jsonpath(re[0][i], '$..detail')
    location = jsonpath.jsonpath(re[0][i], '$..location')
    address = jsonpath.jsonpath(re[0][i], '$..address')
    i += 1
    print(province[0])
    print(city[0])
    print(name[0])
    print(area[0])
    try:
        print(telephone[0])
    except:
        print("")
    print(detail[0])
    print(str(jsonpath.jsonpath(location[0], '$..lng')[0]) + "," + str(jsonpath.jsonpath(location[0], '$..lat')[0]))
    print(address[0])
    print("-----------------------------------------------")
