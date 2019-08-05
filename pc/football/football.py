# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 21:47
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : football.py
# @Software: PyCharm
import lxml
import re
import pymysql
import uuid
import pandas as pd
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
from urllib.request import urlopen

#iii = [80901,80902,80903,80904,80905,81001]
#iii = [81002,81003]
#iii = [81004,81005]
#iii = [81101,81102] iii = [81103,81104,81105,81201,81202,81203，81204,]
#iii = [81205,90101] 90102,90103,
# iii = [90104,90201]
# iii = [90202,90203,90301]
iii =[90303,90304]

ok = 1
conn = pymysql.connect(host="200.100.100.68", port=3306,
                       user="root", passwd="root", db="football", charset="utf8")
cursor = conn.cursor()
for i in iii:
    print('*'*20,i)
    detail_list = []
    url = 'http://cp.zgzcw.com/lottery/bdplayvsforJsp.action?lotteryId=200&issue='+str(i)
    # url1 = 'http://fenxi.zgzcw.com/2465135/ypdb'
    #for i in range(1,6):
        #url = url + str(i)
    try:
        html = urlopen(url)
    except Exception as e:
        print(e)
    bsObj = BeautifulSoup(html, 'lxml')
    div = bsObj.find_all('span',class_='g_qt')
    tream1 = bsObj.find_all('td',class_='wh-4 t-r')
    score = bsObj.find_all('td',class_='wh-5 bf')
    tream2 = bsObj.find_all('td',class_='wh-6 t-l')
    rangqiu  = bsObj.find_all('em',class_='rq')
    rate = bsObj.find_all('a',class_='weisai')
    go_rate = bsObj.find_all('td',class_='wh-10 b-l')
    res_rate = []
    for i in rate:
        res_rate.append(float(i.text))
    res_rate1 = []
    for i in range(1,int(len(rate) / 3)+1):
        i = 3*i
        res_rate1.append(res_rate[i-3:i])
    x = []
    for i in range(len(div)):
        flag = div[i].text.strip().strip('\n').strip('\r')
        host_team = re.findall('tn="(.*?)"',str(tream1[i]))[0].replace('\u3000','')
        guest_team = re.findall('tn="(.*?)"',str(tream2[i]))[0].replace('\u3000','')
        fscore = score[i].text.strip().strip('\n').strip('\r').split(':')
        if 2 == len(fscore):
            host_score = int(fscore[0])
            guest_score = int(fscore[1])
        else:
            host_score = 99
            guest_score = 99
        if  '' != rangqiu[i].text:
            res_rq = int(rangqiu[i].text)
        else:
            res_rq = 0
        detail = re.findall('newplayid="(.*?)"',str(go_rate[i]))[0]
        detail_list.append(detail)
        uuid1 = uuid.uuid1()
        x.append((str(uuid1),flag,host_team,guest_team,host_score,guest_score,res_rq,res_rate1[i][0],res_rate1[i][1],res_rate1[i][2],detail))
    print(x)
    # :1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11
    sql = '''insert into football(fid,flag,host_team,guest_team,host_score,guest_score,rq,win,flat,lose,detail)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor.executemany(sql,x)
    conn.commit()
    print(ok)
    ok+=1
    flag = 1
    print(detail_list)
    for  id in detail_list:
        rate = []
        if len(id) == 7:
            url = 'http://fenxi.zgzcw.com/%s/ypdb' % (id)
            print(url)
            html = urlopen(url)
            bs = BeautifulSoup(html, 'lxml')
            table = bs.findAll('table', class_='bf-tab-02')
            try:
                for i in table[0].findAll('tr'):
                    a = [1, id]
                    for j in i.findAll('td'):
                        a[0] = str(uuid.uuid1())
                        # if '' == j.text:
                        #     pass
                        # else:
                        a.append(j.text.replace('↑', '').replace('↓', ''))
                    a.pop(10)
                    a.pop(2)
                    a.pop(14)
                    rate.append(tuple(a))
            except Exception as e:
                print(e)
        try:
            sql_ch = 'SELECT * FROM rate T where t.gameid =\'%s\'' % id
            print(sql_ch)
            count = cursor.execute(sql_ch)
            if count == 0:
                insert_sql = 'insert into rate(fid,gameid,company,host,pan,guest,new_host,new_pan,new_guest,new_rate_host,new_rate_guest,kaili_host,kaili_guest,peifu) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                print(insert_sql)
                flag+=1
                cursor.executemany(insert_sql, rate)
                conn.commit()
                print('finish insert!' + str(flag) + '-' * 20)
            else:
                print('存在！')
        except Exception as  e:
            print(e)
conn.close()
cursor.close()



