
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 17:42
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : url.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from urllib.request import urlopen#用于获取网页

f = open('url.txt','w')
for i in range(1,277):
    print(i)
    url = 'http://www.ttbz.org.cn/Home/Standard?page='+str(i)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    #div = bsObj.find(id="standard_list_table")
    t1 = bsObj.find_all('a')
    for t2 in t1:
        t3 = t2.get('href')
        if t3.startswith('/StandardManage/Detail/'):
            t3 = 'http://www.ttbz.org.cn'+t3
            f.write(t3+'\n')
            print(t3)
f.close()


