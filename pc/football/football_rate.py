# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 9:13
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : football_rate.py
# @Software: PyCharm

from urllib.request import urlopen
import lxml
from bs4 import BeautifulSoup
import uuid
import pymysql
conn = pymysql.connect(host="200.100.100.68",port=3306,user="root",passwd="root",db="football",charset="utf8")
cursor = conn.cursor()
# sql = 'select t.detail from football t where (select COUNT(1) num from rate t1 where t.detail = t1.gameid) = 0 and detail != 0'
# detail = cursor.execute(sql)
# cid=cursor.fetchall()
cid = ['2465134']
flag = 0
print(len(cid))
for pageid in cid:
    print(pageid)
    rate = []
    if len(pageid) == 7:
        url = 'http://fenxi.zgzcw.com/%s/ypdb' % (pageid)
        print(url)
        html = urlopen(url)
        bs = BeautifulSoup(html,'lxml')
        table = bs.findAll('table',class_='bf-tab-02')
        for i in table[0].findAll('tr'):
            a = [1,pageid[0]]
            for j in i.findAll('td'):
                a[0] = str(uuid.uuid1())
                if '' == j.text:
                    pass
                else:
                    a.append(j.text.replace('↑','').replace('↓',''))
            a.pop(2)
            a.pop(14)
            rate.append(tuple(a))
    try:
        # check_sql = '''SELECT * from rate where gameid ='%s' ''' % rate[0][1]
        # check_res = cursor.execute(check_sql)
        # res_check = cursor.fetchall()
        # len(res_check)
        if  0 == 0:
            print(rate)
            insert_sql = 'insert into rate(fid,gameid,company,host,pan,guest,new_host,new_pan,new_guest,new_rate_host,new_rate_guest,kaili_host,kaili_guest,peifu) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.executemany(insert_sql,rate)
            #conn.commit()
            flag +=1
            print(flag)
        else:
            print('有了！')
    except Exception as  e:
        print(e)
        print(pageid[0])
