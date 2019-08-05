# -*- coding: utf-8 -*-
# @Time    : 2018/6/16 14:15
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : list.py
# @Software: PyCharm


def delrepeat(lis):
    x ={}

    return list(x.fromkeys(lis).keys())



import copy
def fun(list):
    print(id(list))
    for li in list:
        print(id(li))




if __name__ == "__main__":
    x = [x for x in range(1,5)]
    fun(x)
    x.append({'name':'ggg','age':15})
    print(id(x))
    for lx in x:
        print('-'*20)
        print(lx)
        print(id(lx))

    fun(copy.copy(x))
    print('*'*30)
    fun(copy.deepcopy(x))

