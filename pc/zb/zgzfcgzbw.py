# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 19:39
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : zgzfcgzbw.py
# @Software: PyCharm

import sys
from util_emailT import zmail_post
import pymysql
import requests
from bs4 import BeautifulSoup
from copy import deepcopy

sys.path.append('../')

conn = pymysql.connect(host="200.100.100.68", port=3306,
                       user='root', passwd='root', db='football', charset="utf8")
cur = conn.cursor()


def get_page(url):
    rq = requests.get(url)
    bsObj = BeautifulSoup(rq.text, 'lxml')
    text = bsObj.find('div', id='pages').text
    pages = int(text[text.find('共') + 1:text.find('条')]) // 25 + 1
    return pages


def get_data(url):
    rq = requests.get(url)
    bsObj = BeautifulSoup(rq.text, 'lxml')
    zb_list = bsObj.find_all('tr', class_='listrow1') + bsObj.find_all('tr', class_='listrow2')
    ins = []
    for i in zb_list:
        j = i.find('a')
        # 维修不需要，配件不需要
        if j.text.find('维修') == -1 and j.text.find('配件') == -1 \
                and j.text.find('修理') == -1 and j.text.find('修复') == -1:
            content = i.find_all('td')
            if content[3].text.find('招标公告') != -1:
                ins.append([j.text, 'https://www.chinabidding.cn' + j['href'],
                            content[4].text, content[5].text, content[6].find('div').text
                               , content[3].text])
    ins_res = check(ins)
    if len(ins_res) > 0:
        ins_mysql(ins_res)
        return ins_res
    return []


def check(ins):
    res = deepcopy(ins)
    for i in ins:
        check_sql = '''select * from zb where fname = '%s' and url ='%s' ''' % (i[0], i[1])
        try:
            num = cur.execute(check_sql)
            if num > 0:
                res.remove(i)
        except Exception as e:
            print(e)
    return res


def ins_mysql(ins):
    sql = 'insert into zb(fname,url,city,industry,ftime,ftype) values (%s,%s,%s,%s,%s,%s)'
    try:
        cur.executemany(sql, ins)
        conn.commit()
        print('入库成功-----')
    except Exception as e:
        print(e)


def post_email(data):
    par = '尊敬的领导您好:\n  请审核招标信息：\n'
    content = ''
    for i in data:
        if len(i) == 6:
            content += '  标名：' + i[0] + '\n  链接：' + i[1] + '\n  城市：' + i[2] + '\n  行业：' + i[3] + '\n  时间：' + i[
                4] + '\n  ' + '-' * 30 + '\n'
        else:
            content += '\n'.join(content)
    content = par + content
    subject = '有招标信息！请立马审查分析！'
    #
    zmail_post.zmail_post(subject, content, '15005932520@139.com')


def main(url_list):
    res = []
    for url in url_list:
        start = 1
        url_end = '&categoryid=&rp=22&table_type=1000&b_date=1month'
        url_go = url + str(start) + url_end
        page = get_page(url_go)
        for i in range(1, page + 1):
            print(url + str(i) + url_end)
            res += get_data(url + str(i) + url_end)
    print(res)
    if len(res) == 0:
        print('无新标书！')
    else:
        post_email(res)
    conn.close()


if __name__ == '__main__':
    url = ['https://www.chinabidding.cn/search/searchzbw/search2?areaid=&keywords=%E7%AE%A1%E5%B8%A6%E6%9C%BA&page=',
           'https://www.chinabidding.cn/search/searchzbw/search2?areaid=&keywords=%E7%9A%AE%E5%B8%A6%E6%9C%BA&page=']
    main(url)
