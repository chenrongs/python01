# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 19:08
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : test.py
# @Software: PyCharm
from urllib.request import urlretrieve
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def login():
    dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置useragent
    dcap['phantomjs.page.settings.userAgent'] = (
        'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/60.0')  # 根据需要设置具体的浏览器信息
    driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    url = 'http://www.jkjsf.com/ecna/public/work/rec-homePage.html?teamId=1000809#/personalFiles/960CEFF26FED4F3BAE3D770A6827BA39'

    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    driver.add_cookie({
        'domain': '.www.jkjsf.com',  # 注意前面有个点
        'name': 'JSESSIONID',
        'value':'715D50B6BDA462E76A6EC49BD17E4381',
        'path': '/ecna'
    })
    driver.get(url)
    urlretrieve(
        'http://www.jkjsf.com/printservices/preview?__report=flReports/ecna/AssessNote.rptdesign&__format=pdf&assessNoteId=2E4E3FD33C02410CB3B4F1F7F7C0A397',
        filename='1', reporthook=None, data=None)
    print("ok")
    #print(driver.get_log('browser'))

if __name__== '__main__':
    # url1 = 'http://cp.zgzcw.com/lottery/bdplayvsforJsp.action?lotteryId=200&issue=81101'
    # html1 = urlopen(url1)
    a = [1,2,3,4,5,6]
    a.pop(2)
    a.pop(2)
    print(a)