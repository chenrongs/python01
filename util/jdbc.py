# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 18:25
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : jdbc.py
# @Software: PyCharm
import cx_Oracle
import pymysql


Oracle_user = 'hii'
Oracle_password = 'hii'
Oracle_db = '200.100.100.68:1521/CRS'

mysql_user = 'root'
mysql_password = 'root'
mysql_db = 'football'

def Oracle_conn():
    conn = cx_Oracle.connect(Oracle_user,Oracle_password,Oracle_db)
    return conn

def Oracle_cur(sql):
    return Oracle_conn().coursor().excute(sql).fetchall()

def mysql_conn():
    conn = pymysql.connect(host="200.100.100.68", port=3306,
                           user=mysql_user, passwd=mysql_password, db=mysql_db, charset="utf8")
    return conn

def mysql_cur():
    return mysql_conn().cursor()