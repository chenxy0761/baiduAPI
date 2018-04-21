# -*- coding:utf-8 -*-
import json
import urllib2

import jsonpath
import time

import requests
import xlrd

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

data = xlrd.open_workbook('test.xlsx')
table = data.sheets()[0]
t = table.col_values(1)
nrows = table.nrows
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
headers = {"User-Agent":user_agent}
ops = []
for i in range(nrows):
    time.sleep(0.5)
    r1 = table.row_values(i)
    try:
        text = str(r1[1])[0:str(r1[1]).index('(')]
    except:
        text = str(r1[1])
    # print(text)
    response = requests.get(
        'http://api.map.baidu.com/place/v2/suggestion?query=' + text.strip() + '&region=上海&city_limit=true&output=json&ak=8xPapMW0KjwusZa6rDxnvqtTdIRBaZqO',headers = headers)
    # data = json.load(response)
    data = json.loads(response.content.decode())
    # print(data)
    re = jsonpath.jsonpath(data, '$..result')[0]
    # print(re)
    try:
        loc = str(jsonpath.jsonpath(re, '$..lng')[0]) + "," + str(jsonpath.jsonpath(re, '$..lat')[0])
    except:
        loc = '--------'
    print(loc)
