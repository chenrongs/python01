# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 11:59
# @Author  : CRS
import os
import time
import datetime
# filname ="sadasd.txt"
# pos = filname.find(".")
# content = filname[:pos] + str(time.time()).replace(".", "") + filname[pos:]
# print(content)
# print(str(datetime.datetime.now()))
def stopwordslist():
    # 停词库
    stoppath = "C:/Users/Administrator/Desktop/stopwords.txt"
    stopwordslist = [line.strip() for line in open(stoppath,'r',encoding='utf-8').readlines()]
    for _ in stopwordslist:
        print(_)
    # return stopwordslist


def list(path):
    for l in os.listdir(path):
       print(os.path.join(path, l))


list("C:/Users/Administrator/Desktop/分词")


