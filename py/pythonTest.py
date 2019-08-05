# coding=utf-8
import math
import time
import random
import timeit
from collections import Counter
from collections import OrderedDict
import re



def x():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (j != k) and (i != k):
                    print(str(i) + str(j) + str(k))
    ar = [0, 10, 20, 40, 60, 100]


def y(x):
    arr = [100, 60, 40, 20, 10, 0]
    arr1 = [0.01, 0.015, 0.03, 0.05, 0.075, 0.10]
    for i in range(0, 6):
        if x > arr[i]:
            money = 0
            print(str(arr[i]) + "+" + str(arr1[i]))
            print(x - arr[i])
            print(arr1[i])
            money += (x - arr[i]) * arr1[i]
            print(money)
    return money


def z():
    for i in range(10000):
        flag = int(math.sqrt(i + 100))
        if flag * flag == i + 100:
            y = int(math.sqrt(i + 268))
            if y * y == i + 268:
                print(i)


def year():
    yearInput = int(input('year='))
    monthInput = int(input('month='))
    dayInput = int(input('day='))
    print(yearInput, monthInput, dayInput)
    arr = (0, 31, 27, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    sum = 0
    if 0 < monthInput <= 12:
        for i in range(monthInput):
            print(i)
            sum += arr[i]
    else:
        print("月份输入错误！")
    sum += dayInput
    if monthInput > 2 and yearInput % 100 != 0 and yearInput % 4 == 0 or yearInput % 400 == 0:
        print("年份是闰年")
        sum += 1

    return sum


def sort():  # 排序  从小到大
    for i in range(3):
        i = int(input())
        x.append(i)
    x.sort()
    print(x)


def copy():
    a = [1, 2, 3, 4, 5]
    b = a[:]
    print(b)


def print99():
    for i in range(1, 10):
        print("\n")
        for j in range(i, 10):
            x = i * j
            y = str('%d * %d = %d') % (i, j, x)
            y += y
            print(y)


def time1():
    dirt1 = {1: 'hello', 2: 'python'}
    for key, value in dict.items(dirt1):
        print(key, value)
        time.sleep(1)  # 暂停1s


# 兔子的规律为数列1,1,2,3,5,8,13,21....
def find(put):
    put = round((put + 0.1) / 2)
    a, b = 1, 1
    for i in range(1, put):
        a = a + b
        b = a + b
    if put % 2 == 0:
        print(b)
    else:
        print(a)


# 筛数据  的几种方法 filter  [ for ]
def test2():
    # 随机生成 data列表
    data = [random.randint(-10, 10) for _ in range(10)]
    print(data)
    x = list(filter(lambda x: x >= 0, data))  # filter 生成迭代器 用list 输出
    data1 = [random.randint(-50, 50) for _ in range(20)]
    y = list(filter(lambda i: i >= 0, data1))
    print(y.__len__())
    print([x for x in data1 if x >= 0])
    print([x for x in data if x >= 0])
    # 测试运行时间
    t1 = timeit.Timer('[x for x in data if x>=0]', setup='from __main__ import data')
    t2 = timeit.Timer('list(filter(lambda x: x >=0,data))', setup='from __main__ import data')
    print(t2.timeit())
    print(t1.timeit())


# 迭代字典；
def test3():
    dict = {x: random.randint(50, 100) for x in range(1, 20)}
    dict1 = {k: v for k, v in dict.items() if v >= 90}
    print(dict1)


# 生成随机序列找次数最高的 并统计 出现的次数
def test4():
    data = [random.randint(0, 10) for _ in range(30)]
    print(data)
    # 老方法  建立字典 统计  排序
    # d = dict.fromkeys(data, 0)
    # for x in data:
    #     d[x] += 1
    # print(sorted(d.items(), key=lambda item: item[1], reverse=True))
    # Counter 类
    d1 = Counter(data)
    print(d1.most_common(3))


# 词频统计
def test5():
    txt = open('server.xml').read()
    re.split('\W+', txt)
    print(Counter(txt).most_common(10))


# 字典中公共键的问题  集合解决
def test6():
    c = random.sample('asdfghjk', random.randint(3, 6))
    print(c)
    s1 = {x: random.randint(1, 4) for x in random.sample('asdfghjk', random.randint(3, 6))}
    s2 = {x: random.randint(1, 4) for x in random.sample('asdfghjk', random.randint(3, 6))}
    s3 = {x: random.randint(1, 4) for x in random.sample('asdfghjk', random.randint(3, 6))}
    s4 = {x: random.randint(1, 4) for x in random.sample('asdfghjk', random.randint(3, 6))}
    print(s1.keys())
    print(s1.keys() & s2.keys() & s3.keys() & s4.keys())

test6()
# 模拟答题系统
def test7():
    dirt = OrderedDict()
    player = list('ABCDEFG')
    start = time.time()
    for x in range(7):
        # 模拟选手答题结束
        input()
        p = player.pop(random.randint(0, 6-x))
        end = time.time()
        print(p, end-start)
        dirt[p] = (x+1, end-start)
    print()
    print('-' * 20)
    for k in dirt:
        print(k, dirt[k])







