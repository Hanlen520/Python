#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 电子邮件
from email.mime.text import MIMEText
import smtplib

# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
msg = MIMEText('Hello, send by python', 'plain', 'utf-8')

# 输入Email地址和口令
from_address = input('FROM: ')
password = input('Password: ')

# 输入收件人地址
to_address = input('To: ')

# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_address, password)
server.sendmail(from_address, [to_address], msg.as_string())
server.quit()


# ======================== POP3收取邮件 =====================================================
# 20.2 POP3收取邮件
# 收取邮件分两步：
# 第一步：用poplib把邮件的原始文本下载到本地；
# 第二部：用email解析原始文本，还原为邮件对象。