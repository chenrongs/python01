# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 9:37
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : insert.py
# @Software: PyCharm
import cx_Oracle
import pandas as pd
import datetime
import sys
import os
import re

# 连接数据库
Oracle_user = 'hii'
Oracle_password = 'hii'
Oracle_db = '10.76.31.53:1521/dgr'
conn = cx_Oracle.connect(Oracle_user, Oracle_password, Oracle_db)
cur = cx_Oracle.Cursor(conn)
print('数据库连接已启动'
      '现在准备读取数据')
# 进度条
def progress(recv_size,data_size,width=50):
    percent=int(100*recv_size/data_size)
    '''进度打印功能'''
    if percent >= 100:
        percent=100
    show_str=('[%%-%ds]' %width) %(int(width * percent/100)*"#") #字符串拼接的嵌套使用
    print('\r%s %d%%' %(show_str,percent),end='')

# 读取文件的地址
path = r'C:\Users\RSGG\Desktop\20190708'
for file in os.listdir(path):
    if file.endswith('06.csv'):
        # 2.xlsx 有两个病例未导入
        filepath = os.path.join(path, file)
        print('读取' + filepath)
        df = pd.read_csv(filepath, encoding='GBK')
        df['省市审核时间'] = None
        df['填卡医生'] = None
        df['地市审核时间'] = None
        df['订正终审时间'] = None
        df['县区审核时间'] = None
        df['报告卡录入时间'] = None
        df['医生填卡日期'] = None
        df['删除时间'] = None
        df['报告单位'] = None
        df['审核状态'] = None
        df['终审死亡时间'] = None
        rename = {'有效证件号': '身份证号',
                  '人群分类': '职业'
                  }
        df.rename(columns=rename, inplace=True)
        # 选取需要导入的列
        order = ['卡片编号',
                 '卡片ID',
                 '患者姓名',
                 '患儿家长姓名',
                 '性别',
                 '出生日期',
                 '身份证号',
                 '联系电话',
                 '职业',
                 '患者工作单位',
                 '报告单位',
                 '病人属于',
                 '现住详细地址',
                 '现住地址国标',
                 '疾病名称',
                 '病例分类',
                 '病例分类2',
                 '发病日期',
                 '诊断时间',
                 '医生填卡日期',
                 '死亡日期',
                 '填卡医生',
                 '备注',
                 '订正终审时间',
                 '终审死亡时间',
                 '县区审核时间',
                 '地市审核时间',
                 '省市审核时间',
                 '报告卡录入时间',
                 '删除时间',
                 '卡片状态',
                 '审核状态',
                 '实验室结果',
                 '重症患者']
        df = df[order]
        print('读取数据完成 ----开始处理')
        df = pd.concat([df, pd.DataFrame(columns=['age', '处理职业', '现住地址编码'])], sort=True)
        # df = pd.concat([df,pd.DataFrame(columns=['处理职业'])])
        # 计算两个时间的差向上取值
        df['age'] = (pd.to_datetime(df["诊断时间"]).dt.year - pd.to_datetime(df["出生日期"]).dt.year) * 12 + (
                    pd.to_datetime(df["诊断时间"]).dt.month - pd.to_datetime(df["出生日期"]).dt.month)
        # df['age'] = df['age'].replace(0,1)
        df['处理职业'] = df['职业']
        df['处理职业'].loc[(df['职业'] != '散居儿童')
                       & (df['职业'] != '幼托儿童')
                       & (df['职业'] != '学生')] = '其他'
        df['患者姓名'] = '***'
        col_type = {'卡片ID': 'str', '现住地址国标': 'int',
                    '患者姓名': 'str', '省市审核时间': 'datetime64[ns]',
                    '联系电话': 'str', '身份证号': 'str'}
        df = df.replace('.', '')
        df_deal = df.astype(col_type)
        col_type1 = {'卡片ID': 'str', '现住地址国标': 'str'
                     #             '联系电话':'str','身份证号':'str',
                     #             '实验室结果':'str','审核状态':'str'
                     }
        df_deal = df_deal.astype(col_type1)
        df_deal['现住地址编码'] = [i[0:6] for i in df_deal['现住地址国标']]
        df_test = df_deal.fillna('')
        df_notnull = df_test.replace('nan', '')
        df_in = df_notnull.values
        df_in = df_in.tolist()
        flag = []
        data_size = len(df_in)
        print('处理成功，开始入库! 数据总共:%s 条'% data_size)
        for i in range(data_size):
            try:
                # cur.executemany(None,[i])
                sql = '''INSERT INTO IMP_HFMD_DATA(FAGE,FBIRTHDATE,FDELETETIME,FDOCTOR_MARKDATE,FCARDID,FCARDSTATU,FCARDNUM,FCOUNTYAUDITTIME,FONSETDATE,FCITYAUDITTIME,FMARK_DOCTOR,FOCCUPATION1,FDETAIL,FLABRESULTS,FAUDITSTATU,FSEX,FPARENTNAME,FNAME,FCOMPANY,FREPORT_ORG,FREPORT_WRITE_DATE,FDEATH_DATE,FADDRESSNUM,faddresscode,FADDRESS,FDISEASENAME,FPAIENTBELONG,FCASETYPE,FCASETYPE2,FPROVINCEAUDITTIME,FFINALTRIALDEATHTIME,FOCCUPATION,FPHONENUMBER,FCORRECTTRIALTIME,FDIAGNOSTICTIME,FCREDITCARDID,FSEVERE) VALUES('''
                for j in range(1, 38):
                    flag_j = df_in[i][j - 1]
                    if type(flag_j) == str:
                        df_in[i][j - 1] = df_in[i][j - 1].replace('\'', '')
                    check = re.match( r'\d{4}-\d+-\d+', str(flag_j))
                    if type(flag_j) == pd.Timestamp or (check) != None :
                        sql += 'to_date(\'' + check.group() + '''\','YYYY-MM-DD HH24:MI:SS'),'''
                    else:
                        sql += '\'' + str(df_in[i][j - 1]) + '\','
                sql = sql[:len(sql) - 1] + ')'
                #print(sql)
                cur.execute(sql)
                if i % 1000 == 0:
                    progress(i,data_size)
            except Exception as e:
                print('\n', i, '行', str(e))
                ERROR = str(i) + str(e)
                flag.append(ERROR)
                with open('insert.txt', 'a', encoding='utf8') as f:
                    sql += ';'
                    f.write(sql)
            finally:
                conn.commit()
        with open('ERROR.txt', 'a', encoding='utf8') as f:
            if len(flag) !=0 :
                f.write(str(flag))
        print('完成入库')
