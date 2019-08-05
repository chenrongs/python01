# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 19:27
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : zmail_post.py
# @Software: PyCharm

import zmail


def zmail_post(subject,content,sent):
    # 使用你的邮件账户名和密码登录服务器
    mail_content = {
        'subject': subject,  # 随便填写
        'content_text': content,  # 随便填写
        'attachments': 'football.xlsx',  # 最好使用绝对路径，若你电脑没有这个文件会造成错
    }
    server = zmail.server('2670619875@qq.com', 'plqvwfktdadxdieh')
    # 发送邮件
    try:
        server.send_mail(sent, mail_content)
        print('sent!')
    except Exception as e:
        post_err()
    #给多个邮箱发送
    #server.send_mail(['555555@qq.com','666666@qq.com'], mail_content)

def post_err():
    zmail_post('爬虫问题需要解决！', '发送客户方失败！','1105959249@qq.com')

if __name__ == '__main__':
    subject = '有招标信息！请立马审查分析！'
    content =  '此内容为：xxxx公司'
    # 你的邮件内容
    sent = ['1105959249@qq.com']
    zmail_post(subject,content,sent)