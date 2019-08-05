# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 20:50
# @Author  : CRS
# reuqest头
import requests
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Host': 'zhishu.sogou.com',
    'Connection': 'keep-alive'
}
str = "python"
strat = "20180101"
end = "20180416"


def Sougou(str, start, end):
    """
    :param str: 搜索名字
    :param start: 开始时间
    :param end: 结束时间
    :return:
    """
    url = "http://zhishu.sogou.com/getDateData?kwdNamesStr=" + str + "&startDate=" + start + "&endDate=" + end + "&dataType=SEARCH_ALL&queryType=INPUT"
    re = requests.get(url=url, headers=header)
    str_json = re.content.decode()
    json_data = json.loads(str_json)
    print(json_data)
    pv_list = json_data['data']['pvList'][0]
    dict1={}
    for elem in pv_list:
        dict1[elem["date"]] = elem["pv"]
    return dict1


data = Sougou(str, strat, end)
# data = json.loads(data_heat_dict)
for v in data:
    print(v+data[v])
