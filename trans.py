# -*- coding:utf-8 -*-

import urllib2

url = urllib2.unquote(
    "http://api.map.baidu.com/?qt=cen&b=13528395.48%2C3642749.94%3B13528395.48%2C3642749.94&l=12&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk9440&ak=E4805d16520de693a3fe707cdc962045")

print(url)
