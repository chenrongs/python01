# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 17:14
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : gogogo.py
# @Software: PyCharm
import datetime
import json
from urllib import request
from urllib.request import urlretrieve
from selenium import webdriver
import win32api
import pyperclip
import win32con
import time

CHROME_DRIVER = 'D:\\chormedriver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

cookie_str = r'JSESSIONID=4F267081AD08D46C0F803E66132203F0'
useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
# def JDBC():
#     # 连接数据库
#     conn = pymysql.connect(host="200.100.100.68", port=3306,
#                                user="root", passwd="root", db="test", charset="utf8")
#     return conn

# json 格式
#ok = open('ok.txt', 'w')


def req(url):
    req = request.Request(url)
    req.add_header('cookie', cookie_str)
    req.add_header('User-Agent', useragent)
    resp = request.urlopen(req)
    return json.loads(resp.read().decode('utf-8'))

# str
def reqstr(url):
    req = request.Request(url)
    req.add_header('cookie', cookie_str)
    req.add_header('User-Agent', useragent)
    return request.urlopen(req).read().decode('utf-8')


def login():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 登录后才能访问的网站
    url = 'http://www.jkjsf.com/ecna/subject/findArchive?teamId=1000809'
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    data=req(url)
    listdate =  data[1]['packList']
    print(listdate)
    file = open('newdata.txt', 'w')
    for next in listdate:
        file.write(str(next['packId'])+'\n')
    file.close()

def next(txt,okfile):

    seq = 0
    file=open(txt, 'r')
    ok=open(okfile,'w+')
    for next in file.readlines():
        print(next)
        ok.write(next)
        url = 'http://www.jkjsf.com/ecna/subject/findArchiveSubject?packId='+next
        req2data = req(url)
        #print(req2data)
        if  req2data is not None:
            print(req2data)
            for req2next in req2data:
                print('*'*20)
                if req2next['idNo'] is None:
                    req2next['idNo'] = ""
                print(req2next['subjectName']+req2next['idNo'])
                if req2next['subjectId'] is not None:
                    relist = furl(req2next['subjectId'])

                    #i = 1
                    for l in relist:
                        print(l)
                        download_pdf_path = 'E:\\pdf\\'+req2next['subjectName']+'-'+req2next['idNo']+'-1'
                        download(l,download_pdf_path)
                        # urlretrieve(l,
                        #     filename='E:\\pdf\\'+req2next['subjectName']+'-'+req2next['idNo']+'-'+str(i)+'.pdf', reporthook=None, data=None)
                        seq = seq + 1
                        print("ok---"+str(seq))
                        #i+=1
    ok.close()
    file.close()

def furl(id):
    returnlist = []
    url = 'http://www.jkjsf.com/ecna/subject/findArchiveSubjectDetail?subjectId='+id
    reqdata = req(url)
    print(reqdata['reportId'])
    if reqdata['reportId'] is not None:
        rurl = 'http://www.jkjsf.com/ecna/report/getPrintReportUrl?reportId='+reqdata['reportId']
        report1 = reqstr(rurl)
        returnlist.append(report1)
        #print(report1)
    #print(reqdata['assessNoteId'])
    # if reqdata['assessNoteId'] is not None:
    #     rurl2 = 'http://www.jkjsf.com/ecna/report/getAssessNoteUrl?assessNoteId='+reqdata['assessNoteId']
    #     report2 = reqstr(rurl2)
    #     #print(report2)
    #     returnlist.append(report2)
    return returnlist


def download(url,download_pdf_path):
    driver.get(url)
    pyperclip.copy(download_pdf_path)

    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(83, 0, 0, 0)  # s键位码是83
    # 放开
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(2)

    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v键位码是17
    # 放开
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(1)
    win32api.keybd_event(13, 0, 0, 0)  # 回车
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(1)


if __name__== '__main__':
    #login()
    next('newdata1.txt','newok.txt')
