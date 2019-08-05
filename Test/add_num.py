# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 16:21
# @Author  : CRS
from PIL import Image, ImageDraw, ImageFont
import random
import string


# 将 图片右上角 加上 数字
# 类似微信
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 45, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0


# 随机
def discount():
    f = open('discount.txt', 'w')
    for _ in range(200):
        chars = string.ascii_letters + string.digits
        print(chars)
        s = [random.choice(chars) for _ in range(10)]
        last = ''.join(s)+'\n'
        f.write(last)
    f.close()
# if __name__ == '__main__':
    # image = Image.open('C:/Users/Administrator/Desktop/1.jpg')
    # add_num(image)
discount()
