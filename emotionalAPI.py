# -*- coding:utf-8 -*-
import pymysql
import requests
import json
import jsonpath
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

conn = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='root', db='test', charset='utf8mb4')

url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=24.0a5cfd84db329d3ff26af08885eac866.2592000.1526720122.282335-11126907'
headers = {'content-type': "application/json", }
i = 1434
while i < 1460:
    cur = conn.cursor()
    cur.execute('select text from baojing where seq = %s', [i])
    # 获取数据方法
    rows = cur.fetchall()[0]
    # print(rows[0])
    if rows[0] != "":
        body = {
            "text": rows[0][0:1000]
        }
        # print(str(text)[0:100])
        time.sleep(0.1)
        response = requests.post(url, data=json.dumps(body), headers=headers)
        jsonobj = json.loads(response.text)

        try:
            # 从根节点开始，匹配name节点
            sentiment = jsonpath.jsonpath(jsonobj, '$..sentiment')[0]  # 0为消极 1为中性 2为积极
            # text = jsonpath.jsonpath(jsonobj,'$..text')
            confidence = jsonpath.jsonpath(jsonobj, '$..confidence')[0]
            items = jsonpath.jsonpath(jsonobj, '$..items')[0]
            # citylist = jsonpath.jsonpath(jsonobj,'$..sentiment')
            #
            # print(confidence)
            # print sentiment
            # print(str(items[0]))
            ops = [str(items[0]), sentiment, i]
            try:
                cur.execute("update baojing set json= %s,flag= %s where seq = %s", ops)
                conn.commit()
                cur.close()
            except Exception as e:
                print(e)
        except:
            pass
    i += 1
conn.close()
