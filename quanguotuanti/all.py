# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 18:57
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : all.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests
import uuid
#import cx_Oracle
import pymysql

def url_to_html(url):
    '''
    网址换成html形式的函数                                      #将URL转化为HTML文本
    :param url: 网址
    :return: bs:html文本
    '''
    try:
        res = requests.get(url)
        html = res.text
        bs = BeautifulSoup(html, "lxml")             # 初始化时加上解析器类型 "lxml"
    except Exception:
        return ''
    return bs


def for_url():
    f = open('url.txt','r')
    for i in f.readlines():
        print(i)


if __name__ == '__main__':
    # for_url()
    f = open('url.txt','r')
    j = 1
    error_list = []
    for i in f.readlines():
        url = ''.join(i.split())
        print(url)
        soup = url_to_html(
            url
        )
        #print(soup)
        tables = soup.select('table > tbody')
        contain = []
        list1 = []
        i = 0
        for tab in tables:
            # print(tab)
            for tr in tab.find_all('tr'):
                for td in tr.find_all('td'):
                    contain.append("".join(td.getText().split()))
                    # print (td.getText())
                    list1.append(i)
                    i+=1
        #dict1 = dict(zip(list1,contain))
        contain.append('')
        contain.append('')
        #print(dict1)
        #try:
        #conn =  cx_Oracle.connect('hii', 'hii', '200.100.100.68:1521/mydgr')
        conn = pymysql.connect(host="200.100.100.68", port=3306,
                               user="root", passwd="root", db="atticle", charset="utf8")
        # 返回连接的游标对象
        #cur = cx_Oracle.Cursor(conn)
        cur = conn.cursor()
        fid = uuid.uuid1().hex.upper()
        sql =  "insert into lab_standard values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
               % (fid,contain[1],contain[3],contain[5],contain[7],contain[9],contain[11],contain[16],contain[18],contain[20]
                  , contain[24],contain[26],contain[28],contain[34],contain[36],contain[38],contain[40],contain[42],contain[44],contain[46])#contain[40]

        print(sql)
        cur.execute(sql)
        # print(contain[40])
        # print(contain[42])
        #cur.execute("update lab_standard set fcontent = '%s' where fid ='%s'" % (contain[40],fid) )
        conn.commit()
        # except :
        #     error_list.append(url)
        print(j)
        j += 1
        print('error:')
        print(error_list)
    cur.close()

