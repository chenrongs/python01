# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 0:41
# @Author  : Crsboom
# @Email   : 1105959249@qq.com
# @File    : emailTest.py
# @Software: PyCharm
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.sina.com"                  # SMTP服务器
mail_user = "crsboom@sina.com"                   # 用户名
mail_pass = "asdf2791"                      # 授权密码，非登录密码

sender = 'crsboom@sina.com'              # 发件人邮箱(最好写全, 不然会失败)
receivers = '1105959249@qq.com'         # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

content = '''''
    你好，xiaoming
            这是一封自动发送的邮件。

'''
title = '这是一封信'                          # 邮件主题

def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = sender
    #message['From'] = "{}".format(sender)
    # message['To'] = ",".join(receivers)
    message['To'] = receivers
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
    email_client.quit()


def test():
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")


if __name__ == '__main__':
    # send_email2(mail_host,mail_user,mail_pass,receivers,title,content)
    sendEmail()
    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)

