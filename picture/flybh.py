# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 11:08
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : flybh.py
# @Software: PyCharm

import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt

def fourier_demo(path):
    #1、读取文件，灰度化
    img = cv.imread(path)
    cv.imshow('original', img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    cv.waitKey(0)
    #2、图像延扩
    h, w = img.shape[:2]
    new_h = cv.getOptimalDFTSize(h)
    new_w = cv.getOptimalDFTSize(w)
    right = new_w - w
    bottom = new_h - h
    nimg = cv.copyMakeBorder(gray, 0, bottom, 0, right, borderType=cv.BORDER_CONSTANT, value=0)
    cv.imshow('new image', nimg)

    #3、执行傅里叶变换，并过得频域图像
    f = np.fft.fft2(nimg)
    fshift = np.fft.fftshift(f)
    magnitude = np.log(np.abs(fshift))


    #二值化
    magnitude_uint = magnitude.astype(np.uint8)
    ret, thresh = cv.threshold(magnitude_uint, 11, 255, cv.THRESH_BINARY)
    print(ret)
    cv.imshow('thresh', thresh)
    cv.waitKey(0)
    print(thresh.dtype)
    #霍夫直线变换
    lines = cv.HoughLinesP(thresh, 2, np.pi/180, 30, minLineLength=40, maxLineGap=100)
    print(len(lines))

    #创建一个新图像，标注直线
    lineimg = np.ones(nimg.shape,dtype=np.uint8)
    lineimg = lineimg * 255

    piThresh = np.pi/180
    pi2 = np.pi/2
    print(piThresh)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(lineimg, (x1, y1), (x2, y2), (0, 255, 0), 2)
        if x2 - x1 == 0:
            continue
        else:
            theta = (y2 - y1) / (x2 - x1)
        if abs(theta) < piThresh or abs(theta - pi2) < piThresh:
            continue
        else:
            print(theta)

    angle = math.atan(theta)
    print(angle)
    angle = angle * (180 / np.pi)
    print(angle)
    angle = (angle - 90)/(w/h)
    print(angle)

    center = (w//2, h//2)
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(img, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
    cv.imshow('line image', lineimg)
    cv.imshow('rotated', rotated)

fourier_demo('2.png')
cv.waitKey(0)
cv.destroyAllWindows()
