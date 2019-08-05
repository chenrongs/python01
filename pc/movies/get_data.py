# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 12:22
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : get_data.py
# @Software: PyCharm
import json
import lxml
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import pandas as pd


def get_movie(year,id):
    # url = 'http://movie.mtime.com/boxoffice/?year=2018&area=china&type=MovieRankingYear&category=all&page=%s&display=list&timestamp=1543584211252&version=07bb781100018dd58eafc3b35d42686804c6df8d&dataType=json' % id
    url = 'http://movie.mtime.com/boxoffice/?year=%s&area=china&type=MovieRankingYear&category=china&page=%s&display=list&timestamp=1544013062074&version=07bb781100018dd58eafc3b35d42686804c6df8d&dataType=json'% (year,id)
    # print(url)
    data = []
    rq = requests.get(url=url)
    str_json = rq.content.decode()
    json_data = json.loads(str_json)
    bs = BeautifulSoup(json_data['html'],'lxml')
    datal = bs.findAll('div',class_= 'movietopmod')
    for _ in datal:
        try:
            name = _.find('div', class_='picbox').find('a')['title']
            murl = _.find('div', class_='picbox').find('a')['href']
            pf = _.find_all('p')[0].text  # 票房
            sy = _.find_all('p')[1].text  # 上映
            dy = _.find('div', class_='txtbox').find_all('a')[2].text  # 导演
            dyurl = _.find('div', class_='txtbox').find_all('a')[2]['href']  # 导演
            dyscore = xa(find_id(dyurl))
            yy1 = _.find('div',class_= 'txtbox').find_all('a')[3].text #主演
            yy2 = _.find('div',class_= 'txtbox').find_all('a')[4].text
            yy1url = _.find('div',class_= 'txtbox').find_all('a')[3]['href'] #主演
            yy2url = _.find('div',class_= 'txtbox').find_all('a')[4]['href']
            yy1score = xa(find_id(yy1url))
            yy2score = xa(find_id(yy2url))
            dypf = _.find('div', class_='gradebox').find_all('p')[0].text  # 电影评分
            pjcount = _.find('div', class_='gradebox').find_all('p')[1].text  # 评价人数
            ndpf = _.find_all('p', 'totalnum')[0].text  # 年度票房
            rs = _.find_all('p', 'none')[0].text  # 年度票房
        except Exception as e:
            print(e)
            name=''
            pf=''
            sy=''
            dy=''
            yy1 = ''
            yy2 = ''
            yy1score = 0
            yy2score = 0
            dypf = 0
            pjcount=''
            ndpf=''
            rs=''
            dyscore=0
        data_row = [name,pf,sy,dy,dyscore,yy1,yy1score,yy2,yy2score,dypf,pjcount,ndpf,rs,year]
        # print(data_row)
        data.append(data_row)
    return  data
        # print(name,murl,'\n',pf,'\n',sy,
        #       '\n',dy,dyurl,'\n',yy1,yy1url,'\n',yy2,yy2url,'\n',dypf
        #       ,'\n',pjcount,'\n',ndpf,'\n',rs
        #      )

def find_id(url):
    return str(re.findall(r'com/(.*)/', url)[0])


def xa(id):
    try:
        url ='http://service.library.mtime.com/Person.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetPersonRatingInfo&Ajax_CrossDomain=1&Ajax_RequestUrl=file%3A%2F%2F%2FC%3A%2FUsers%2FRSGG%2FDesktop%2F%25E6%2596%25B0%25E5%25BB%25BA%25E6%2596%2587%25E6%259C%25AC%25E6%2596%2587%25E6%25A1%25A3.html&t=20181211443597642&Ajax_CallBackArgument0='+str(id)
        rq = requests.get(url=url)
        str_json = rq.content.decode()
        x = str_json.find(r'{',32)
        y = str_json.find(r'}',0)
        json_str = json.loads(str_json[x:y+1])
        return json_str['finalRating']
    except Exception as e:
        print(e)
        return 0

if __name__ == '__main__':
    data = []
    year = ['2017','2018']
    for j in year:
        for i in range(6):
            data+=get_movie(j,i)
    df = pd.DataFrame(data)
    print(df)
    df.to_excel('movies.xlsx')