# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 15:35
# @Author  : Crsboom# @Email   : 1105959249@qq.com
# @File    : cal_uncertainty.py
# @Software: PyCharm
from scipy.stats import t
import pandas as pd
import numpy as np
import lab_dba
import util



#A类 贝塞尔法 - 大于10的时候用
def Bezier(data):
    df = pd.DataFrame(data,columns=['data'])
    df_mean = df['data'].mean()
    point = len(str(np.modf(df_mean)[0]))-2
    df['残差'] =[round(x-df_mean,point) for x in df['data']]
    df['残差平方'] = np.square(df['残差'])
    df_sum  = df.sum()
    df_sum['残差'] = round(df_sum['残差'],point)
    f = len(df)-1
    # 不确定度 标准偏差
    s = np.sqrt(df_sum['残差平方']/f)
    # 平均值标准偏差 = 平均值标准不确定度
    sx = s / np.sqrt(len(df))
    # 平均值扩展不确定度
    t_values = t.isf(0.025, df=f)
    U = t_values * sx
    res = str(df_mean)+'±'+str(U) + 'f = '+ f + 'P=95%'
    return res

#A类 极差法-小于10的时候用
def DMRT(data):
    C = {2:1.13,3:1.69,4:2.06,5:2.33,6:2.53,7:2.7,8:2.85,9:2.97}
    return (max(data)-min(data))/C[len(data)]

def main():
    pass

if __name__ == '__main__':
    # getparms = get_java(sys.argv[1])
    # print('python:',getparms)
    dba = lab_dba(getparms[1])
    data = dba.get_data(getparms[3].split('、'))
    data = [29.9950, 29.9958, 29.9954, 29.9955, 29.9954, 29.9953, 29.9956, 29.9956, 29.9956, 29.9952]
    # data = [0.38,0.31,0.35,0.34,0.37,0.39,0.4,0.34,0.3,0.36],9.92
    # data = [9.99,9.97,9.98,9.98,9.93,9.92,9.99,9.96,9.99]
    # data  = [0.6,    0.4,   0.8,   0.2,   0.3,   0.5,   0.5,   0.7,   0.4,   0.6]
    res = Bezier(data)
    # res1 =  DMRT(data)
    print(res)