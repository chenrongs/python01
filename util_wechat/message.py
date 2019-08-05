import re
import time
import itchat
import platform
from itchat.content import *
# 用来存储消息相关信息的字典
msg_info = {}
# 调用platform库判断操作系统，以便接下来的登录操作
# 登录函数如下，该函数执行过后用户可通过扫描二维码登录网页版微信
if platform.platform()[:7] == 'Windows':
	itchat.login(enableCmdQR=False)
else:
	itchat.login(enableCmdQR=True)
# 注册，分别对应文本，图片，好友申请，名片，地图信息，分享，语音，附件，视频
# isFriendChat对应朋友会话，isMpChat对应公众号会话，另isGroupChat对应群组会话
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True, isMpChat=True)
def handleRMsg(msg):
	# 获取接收消息的时间并将时间字符串格式化
	msg_time_receive = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	# 获取发信人信息
	try:
		# 通过'FromUserName'寻找到一个字典并取其'NickName'赋值给msg_from
		msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
	except:
		# 如果非正常，则是WeChat官方声明
		msg_from = 'WeChat Official Accounts'
	# 获取发信时间
	msg_time_send = msg['CreateTime']
	# 获取信息ID
	msg_id = msg['MsgId']
	# 消息内容置空
	msg_content = None
	# link置空
	msg_link = None
# 文本或者好友推荐
	if msg['Type'] == 'Text' or msg['Type'] == 'Friends':
		msg_content = msg['Text']
		print('[Text/Friends]: %s' % msg_content)
	# 附件/视频/图片/语音
	elif msg['Type'] == 'Attachment' or msg['Type'] == "Video" or msg['Type'] == 'Picture' or msg['Type'] == 'Recording':
		msg_content = msg['FileName']
		msg['Text'](str(msg_content))
		print('[Attachment/Video/Picture/Recording]: %s' % msg_content)
	# 推荐名片
	elif msg['Type'] == 'Card':
		msg_content = msg['RecommendInfo']['NickName'] + '的推荐名片，'
		if msg['RecommendInfo']['Sex'] == 1:
			msg_content += '性别男。'
		else:
			msg_content += '性别女。'
		print('[Card]: %s' % msg_content)
	# 位置信息
	elif msg['Type'] == 'Map':
		x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
		if location is None:
			msg_content = r"纬度:" + x.__str__() + ", 经度:" + y.__str__()
		else:
			msg_content = r"" + location
		print('[Map]: %s' % msg_content)
	# 分享的音乐/文章
	elif msg['Type'] == 'Sharing':
		msg_content = msg['Text']
		msg_link = msg['Url']
		print('[Sharing]: %s' % msg_content)
	msg_info.update(
		{
			msg_id: {
				"msg_from": msg_from,
				"msg_time_send": msg_time_send,
				"msg_time_receive": msg_time_receive,
				"msg_type": msg["Type"],
				"msg_content": msg_content,
				"msg_link": msg_link
			}
		}
	)
# 再次注册NOTE即通知类型
@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
def monitor(msg):
	if '撤回了一条消息' in msg['Content']:
		# 此处\<msgid\>(.*?)\<\/msgid\>的原因是，如果将msg['Content']打印出来，会在其中得到含有\<msgid\> \<\/msgid\>的一段信息
	    # 而（.*?）则是正则表达式，用于匹配其中的任意字符串
	    # 同时，group(1)表示从第一个左括号处开始匹配
		recall_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
		recall_msg = msg_info.get(recall_msg_id)
		print('[Recall]: %s' % recall_msg)
		msg_prime = '---' + recall_msg.get('msg_from') + '撤回了一条消息---\n' \
														 '消息类型：' + recall_msg.get('msg_type') + '\n' \
																								'时间：' + recall_msg.get(
			'msg_time_receive') + '\n' \
								  '内容：' + recall_msg.get('msg_content')
		if recall_msg['msg_type'] == 'Sharing':
			msg_prime += '\n链接：' + recall_msg.get('msg_link')
		# 向文件助手发送消息
		itchat.send_msg(msg_prime, toUserName='filehelper')
		if recall_msg['msg_type'] == 'Attachment' or recall_msg['msg_type'] == "Video" or recall_msg[
			'msg_type'] == 'Picture' or recall_msg['msg_type'] == 'Recording':
			file = '@fil@%s' % (recall_msg['msg_content'])
			itchat.send(msg=file, toUserName='filehelper')
		msg_info.pop(recall_msg_id)

itchat.run()