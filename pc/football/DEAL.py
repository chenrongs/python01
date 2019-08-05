# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 17:12
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : DEAL.py
# @Software: PyCharm


from util.jdbc import mysql_conn,mysql_cur
import pandas as pd

conn = mysql_conn()
cur = mysql_cur()

cur.execute('select * from football')
df = cur.fetchall()

print(df)