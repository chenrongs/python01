import pandas as pd
import numpy as np
import datetime as dt
import cx_Oracle

Oracle_user = 'hii'
Oracle_password = 'hii'
Oracle_db = '10.76.31.53:1521/dgr'
conn = cx_Oracle.connect(Oracle_user,Oracle_password,Oracle_db)
cur = cx_Oracle.Cursor(conn)
sql = 'insert into imp_weather_data values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,1)'
cur.prepare(sql)
print('oracle conncetion!')
weather= pd.read_csv(r'C:/Users/RSGG/Desktop/gdw17_18station.csv')
weather['日期'] = pd.to_datetime(weather['日期'])
weather['year'] = weather['日期'].dt.year
weather = weather.astype(str)
weather['n'] = None
weather['日期'] = pd.to_datetime(weather['日期'])
ins = weather[['站号','日期','year','日平均气温','日最高气温','日最低气温','日降水量',
               '日平均相对湿度','日平均风速','n','n','日平均气压','n','n'
              ,'日日照时数','n']]
ins_list = ins.values.tolist()
print()
cur.executemany(None,ins_list)
print('ins ok ')
cur.close()
conn.commit()
conn.close()
print('commit ok ')
