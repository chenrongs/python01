# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 21:08
# @Author  : CRS
import os
import stat
import re


def test1():
    """
        找出以什么开头的和什么结尾的字符串
        re.sub 组合每组字符串 并替换
    :return:
    """
    list = os.listdir(".")
    print(list)
    filters = [name for name in os.listdir(".") if name.endswith('.py')]
    print(filters)
    print(os.stat("topic.py"))
    str1 = "2015-05-13"
    # sub 字符串分组
    str2 = re.sub('(\d{4})-(\d{2})-(\d{2})',r'\3/\2/\1',str1)
    print(str2)


def test2():
    """
        "".join拼接字符串
        对字符串打印 工整
    :return:
    """
    s = "sdjasdj"
    # s.ljust() ,s.rjust()
    print(s.ljust(20,"*"))
    # format(s,'<20')  '>10' '^20'居中 左对齐右对齐
    keys = ["sad","fdkjfnkd","sdsfsa","dsdbjabdsad"]
    values = [54,153,154,22]
    dirt1 = dict(zip(keys,values))
    # map 获取 字符串的长度 取最大值
    leng=max(map(len,dirt1.keys()))
    for keys,values in dirt1.items():
        # 对key取左对齐
        print(keys.ljust(leng),values)

test2()