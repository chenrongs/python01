# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 18:06
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : test1.py
# @Software: PyCharm

import numpy as np
np.random.seed(1337)
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

X = np.linspace(-1,1,200)
np.random.shuffle(X)

Y = 0.5*X + 2+np.random.normal(0,0.05,(200,))
# plt.scatter(X, Y)
# plt.show()

X_train, Y_train = X[:160], Y[:160]     # 把前160个数据放到训练集
X_test, Y_test = X[160:], Y[160:]       # 把后40个点放到测试集

model = Sequential()

model.add(Dense(output_dim=1,input_dim=1))
model.compile(loss='mse',optimizer='sgd')
print('Training -----------')
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train) # Keras有很多开始训练的函数，这里用train_on_batch（）
    if step % 100 == 0:
        print('train cost: ', cost)
print('\nTesting ------------')
cost = model.evaluate(X_test, Y_test, batch_size=40)
print('test cost:', cost)
W, b = model.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)

# plotting the prediction
Y_pred = model.predict(X_test)
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred)
plt.show()