# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 20:41
# @Author  : CRS
from collections import Iterable, Iterator


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        return city

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather()


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


class isP:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def crs(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end+1):
            if self.crs(k):
                yield k


# 反向迭代器
class FloatIterator:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        x = self.start
        while x <= self.end:
            yield x
            x += self.step

    def __reversed__(self):
        x = self.end
        while x <= self.start:
            yield x
            x -= self.step

for x in FloatIterator(1, 10, 0.2):
        print(x)









