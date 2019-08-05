# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 9:55
# @Author  : CRS
import codecs

import jieba
import jieba.analyse


def jiebaf(file):
    # 载入词典
    # jieba.load_userdict(file_name)  # file_name
    fileresult = codecs.open("text.txt", "w+", encoding='utf-8')
    file.read().strip()
    jieba.analyse.set_idf_path("D:/python/Test/idf.txt")
    tags = jieba.analyse.extract_tags(file.read(), topK=50)
    print(tags)
    #fileresult.write(tags + '\n')
    file.close()
    fileresult.close()

if __name__ == "__main__":
    file = codecs.open("C:/Users/Administrator/Desktop/广州公共资源交易指数体系建设研究报告-V4.4-20171201-林.txt",
                       "r", encoding='utf-8')
    jiebaf(file)