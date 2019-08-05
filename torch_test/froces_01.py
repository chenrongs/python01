# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 13:21
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : froces_01.py
# @Software: PyCharm

'''
data: https://www.kaggle.com/c/bike-sharing-demand/data
datetime - hourly date + timestamp
season -  1 = spring, 2 = summer, 3 = fall, 4 = winter
holiday - whether the day is considered a holiday
workingday - whether the day is neither a weekend nor holiday
weather - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
temp - temperature in Celsius
atemp - "feels like" temperature in Celsius
humidity - relative humidity
windspeed - wind speed
casual - number of non-registered user rentals initiated
registered - number of registered user rentals initiated
count - number of total rentals
'''
import matplotlib.pyplot as plt

import torch
from torch import nn
import pandas as pd
import time
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
import numpy as np
from torch.autograd import Variable

df = pd.read_csv(r'C:\Users\RSGG\Desktop\train.csv')
df['hours'] = pd.to_datetime(df.datetime).dt.hour
# 独热编码
df = pd.get_dummies(df,columns=['season','holiday','workingday','weather'])
df = df.iloc[:,1:]
Y = df['count'].values
Y = Y.reshape(len(Y),1)
X = df.drop('count',axis = 1)

# 归一化
cen = X.iloc[:,0:4].values
std = StandardScaler()
#将x进行标准化
x_std = std.fit_transform(cen)
X_IN = np.append(X.iloc[:,4:-1].values,x_std,axis=1)

# 搭建简单的网络
neu = nn.Sequential(
    nn.Linear(18,5),
    nn.Sigmoid(),
    nn.Linear(5,1)
)
print(neu)

opt = torch.optim.SGD(neu.parameters(),lr=0.01)
#设置学习率为0.5，用随机梯度下降发优化神经网络的参数
cost = nn.MSELoss()

losses = []
for i in range(300):
    batch_loss = []
    batch_size=128
    for start in range(0,len(Y),batch_size):
        end = start + batch_size if start + batch_size <len(Y) else len(Y)
        xx = Variable(torch.FloatTensor(X_IN[start:end]))
        yy = Variable(torch.FloatTensor(Y[start:end]))
        p = neu(xx)
        loss = cost(p,yy)
        opt.zero_grad()
        loss.backward()
        opt.step()
        batch_loss.append(loss.data.numpy())
    if i % 100 ==0:
        losses.append(np.mean(batch_loss))
        print(i,np.mean(batch_loss))

neu.eval() # 必备，将模型设置为评估模式
with torch.no_grad(): # 禁用梯度计算
    output = neu(X_IN)
    print(output)
    # x = [i for i in range(len(Y))]
    # plt.plot(x,output)
    # plt.plot(x,Y)
    # plt.show()


