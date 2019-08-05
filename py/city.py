# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 15:46
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : city.py
# @Software: PyCharm
from urllib import request
import codecs
import json

useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

def getcityreq(url):
    req = request.Request(url)
    req.add_header('User-Agent',useragent)
    resp = request.urlopen(req)
    return json.loads(resp.read().decode('utf8'))

if __name__ == '__main__':
    code = getcityreq('http://report.amap.com/ajax/getCityInfo.do?')
    file = codecs.open('citycode.txt','w+','utf8')
    for codelist in code:
        file.write(str(codelist['code'])+codelist['name']+'\n')
    file.close()

    url1='http://report.amap.com/ajax/cityDailyQuarterly.do?cityCode=440100&year=2017&quarter=3'
    url2='http://report.amap.com/ajax/cityDaily.do?cityCode=440100'