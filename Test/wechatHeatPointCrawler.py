# coding:utf-8


"""
@created time:2018/3/27 10:00
@Python version: python 3.5
@contact:QQ:1109203712@qq.com
@author: 李宗衡
@software: PyCharm Community Edition
@file: wechatAnalysis.py
@content: 爬搜狗微信热度并保存到数据库
"""

import requests
import time
import json
from urllib import parse
import logging
import cx_Oracle
import numpy as np
import random


# reuqest头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Host': 'zhishu.sogou.com',
    'Connection': 'keep-alive'
}
# 格式为日期：热度的字典
date_heat_dict = {}
# 开始时间
start_time = '20180410'
# 结束时间
end_time = '20180415'
# 用户
user = 'sys'
# 密码
psw = 'Qwer1234'
# 数据库
oracle = '127.0.0.1/orcl'
# 是否系统dba
sysdba = '1'


def logging_init():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
    )


def connect_oracle(user, psw, oracle, sysdba):
    """

    :param user:
    :param psw:
    :param oracle:
    :param sysdba:
    :return:
    """
    try:
        if sysdba == '1':
            connection = cx_Oracle.connect(user, psw, oracle, cx_Oracle.SYSDBA, encoding='utf-8')
        else:
            connection = cx_Oracle.connect(user, psw, oracle, encoding='utf-8')


        cursor = cx_Oracle.Cursor(connection)
        return cursor, connection
    except Exception:
        logging.debug('connect_oracle error')


def select_oracle(cursor, connection):
    """

    :param cursor:
    :param connection:
    :return:
    """
    try:
        name_list = []
        sql = "select fWordsCN from wxidx_tbc_KeyWordsDef where fStatus = '1'"
        cursor.execute(sql)
        name_tuple_list = cursor.fetchall()
        for name_tuple in name_tuple_list:
            name_list.append(name_tuple[0])
        return name_list
    except Exception:
        logging.debug('select_oracle error')


def insert_oracle(data_dict, search_name, cursor, connection):
    """

    :param data_dict:
    :param search_name:
    :param cursor:
    :param connection:
    :return:
    """
    try:
        for heat_time in data_dict:
            param = []
            param.append(heat_time)
            heat = data_dict[heat_time]
            param.append(heat)
            param.append(search_name)
            now_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            param.append(now_str)
            sql = "insert into wxidx_tbs_Indexes (FIDXDTKEY, FIDXVAL, FKEYWORD,fIdxDt,FCREATEDT,FLASTUPDDT) values(:1,:2,:3,to_date (:4, 'YYYY-MM-DD HH24:MI:SS' ),to_date (:4, 'YYYY-MM-DD HH24:MI:SS' ),to_date (:4, 'YYYY-MM-DD HH24:MI:SS' ))"
            # 传递给oracle后commit
            cursor.execute(sql, param)
            time.sleep(1)
            connection.commit()
    except Exception:
        logging.debug('insert_oracle error')


def get_heat(start_time, end_time, search_name):
    """

    :param start_time:
    :param end_time:
    :param search_name:
    :return:
    """
    try:
        date_heat_dict = {}
        search_name_encode = parse.quote(search_name)
        url = 'http://zhishu.sogou.com/getDateData?kwdNamesStr=' + search_name_encode + '&startDate=' + start_time + '&endDate=' + end_time + '&dataType=MEDIA_WECHAT&queryType=INPUT'
        re = requests.get(url=url, headers=header)
        str_json = re.content.decode()
        json_data = json.loads(str_json)
        pv_list = json_data['data']['pvList'][0]
        for elem in pv_list:
            date_heat_dict[elem["date"]] = elem["pv"]
        return date_heat_dict
    except Exception:
        logging.debug('sougou util_wechat have no word %s' % search_name)


if __name__ == '__main__':
    logging_init()
    logging.debug('start oracle connect')
    cursor, connection = connect_oracle(user, psw, oracle, sysdba)
    logging.debug('finish oracle connect')
    logging.debug('start select oracle')
    search_name_list = select_oracle(cursor, connection)
    logging.debug('finish select oracle')
    logging.debug('start get heat and insert')
    for search_name in search_name_list:
        try:
            logging.debug('start get_heat %s' % search_name)
            date_heat_dict = get_heat(start_time, end_time, search_name)
            logging.debug('finish get_heat %s' % search_name)
            time.sleep(2*random.random())
            logging.debug('start insert %s' % search_name)
            insert_oracle(date_heat_dict, search_name, cursor, connection)
            logging.debug('finish insert %s' % search_name)
        except Exception:
            continue
    logging.debug('finish get heat and insert')
    logging.debug('perfect')