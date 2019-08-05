# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 11:25
# @Author  : CrsBoom
# @Email   : daydayup@foxmail.com
# @File    : cap.py
# @Software: PyCharm

# 实现验证码的功能
import random
# import matplotlib.pyplot as plt
import string
import sys
import math
from PIL import Image,ImageDraw,ImageFont,ImageFilter
filename="C:/Users/123/Desktop/yzm/"
#字体的位置，不同版本的系统会有不同BuxtonSketch.ttf
#font_path = 'C:/Windows/Fonts/默陌肥圆手写体.ttf'
#生成几位数的验证码
number = 4
#生成验证码图片的高度和宽度
size = (129,53)
#背景颜色，默认为白色
bgcolor = (255,255,255)
#字体颜色，默认为蓝色
fontcolor = (112,112,112)
#干扰线颜色。默认为红色
linecolor = (233,0,41)
#是否要加入干扰线
draw_line = True
#加入干扰线条数的上下限
line_number = (1,3)
# 随机字母:
def gene_text():
    source = string.ascii_letters + string.digits
    image=[random.choice(source) for _ in range(4)]
    return image
#用来绘制干扰线
def gene_line(draw,width,height):
    # begin = (random.randint(0, width), random.randint(0, height))
    # end = (random.randint(0, width), random.randint(0, height))
    begin = (0, random.randint(0, height))
    end = (90, random.randint(0, height))
    draw.line([begin, end], fill = linecolor,width=3)

#生成验证码
def gene_code():
    width,height = size #宽和高
    image = Image.new('RGB',(width,height),bgcolor) #创建图片
    font = ImageFont.truetype("C:\Windows\Fonts\SHOWG.TTF",38) #验证码的字体
    draw = ImageDraw.Draw(image)  #创建画笔
    text = " ".join(gene_text()) #生成字符串
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / number, (height - font_height) / number),text,\
            font= font,fill=fontcolor) #填充字符串
    if draw_line:
        for _ in range(random.choice(line_number)):
            gene_line(draw,width,height)
    #image = image.transform((width+30,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    #image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
    # CONTOUR
    x= random.randint(1,4)
    if x == 1:
        image = image.filter(ImageFilter.FIND_EDGES)
    if x== 2:
        image = image.filter(ImageFilter.CONTOUR)
    if x == 3:
        image = image.filter(ImageFilter.EMBOSS)
    else:
        image = image.filter(ImageFilter.SHARPEN)
    # a = str(m)
    aa = str(".png")
    path = text + aa
    # cv2.imwrite(path, I1)
    # image.save('idencode.jpg') #保存验证码图片
    image.save(path)

if __name__ == "__main__":
    gene_code()
