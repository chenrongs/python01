# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 14:20
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : findQ.py
# @Software: PyCharm
import re
import os
import codecs
def findq(ok):
    for list in os.listdir(ok):
        f = codecs.open(list, 'r+', encoding='GBK')
        print(f.readlines())
    #     if f.readlines():
    #         str = "adda'1*1',sadnk'*2'sdkkal'*3'"
    #         p = re.compile(r"\'\*.*\'")
    # #\'.*?\'
    #         all = p.findall(str)
    #         print(all)

findq('C:/Users/Administrator/Desktop/511/511/页面')
