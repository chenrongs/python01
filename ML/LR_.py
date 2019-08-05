# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 20:24
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : LR_.py
# @Software: PyCharm
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np

# sigmoid函数和初始化数据
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def init_data():
    # data = np.loadtxt('data.csv')
    # dataMatIn = data[:, 0:-1]
    # classLabels = data[:, -1]
    # dataMatIn = np.insert(dataMatIn, 0, 1, axis=1)  #特征数据集，添加1是构造常数项x0
    # return dataMatIn, classLabels
    cancer = load_breast_cancer()
    X = cancer.data
    y = cancer.target
    print('data sgape:{0}, no. positive:{1}, no. negative:{2}'.format(X.shape,
                                                                      y[y == 1].shape[0],
                                                                      y[y == 0].shape[0]))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=3)
    return X_train,y_train

# 梯度上升
def grad_descent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)  #(m,n)
    labelMat = np.mat(classLabels).transpose()

    m, n = np.shape(dataMatrix)
    weights = np.ones((n, 1))  #初始化回归系数（n, 1)
    alpha = 0.001 #步长
    maxCycle = 500  #最大循环次数

    for i in range(maxCycle):
        h = sigmoid(dataMatrix * weights)  #sigmoid 函数
        weights = weights + alpha * dataMatrix.transpose() * (labelMat - h)  #梯度
    return weights

if __name__ == '__main__':
    dataMatIn, classLabels = init_data()
    print(dataMatIn)
    print(classLabels)

    r = grad_descent(dataMatIn, classLabels)
    print(r)