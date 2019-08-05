# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 17:41
# @Author  : CRS
import codecs
import sys
import jieba
import os
import jieba.analyse


source_dir = './result_all/'
topic_dir = './'
topic_file = 'topic_all.txt'


def get_topic():
    print("start process")
    topic_filename = os.path.join(topic_dir, topic_file)
    if os.path.exists(topic_filename):
        print(topic_filename + 'exists')
        os.remove(topic_filename)
    file_write = codecs.open(topic_filename, 'w', encoding='utf-8')
    # 能够把给定的目录下的所有目录和文件遍历出来。
    for dirpath, dirnames, files in os.walk(source_dir):
        for item in files:
            file_name = os.path.join(source_dir, item)
            content = codecs.open(file_name, 'r', encoding='utf-8').read()
            tags = jieba.analyse.extract_tags(content, topK=50)
            file_write.writelines(tags + '\n')
    print("finished")


