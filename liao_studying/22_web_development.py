#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: web开发

# 22.1 Http协议简介
# Elements显示网页的结构，Network显示浏览器和服务器的通信。
# 200表示一个成功的响应，后面的OK是说明。失败的响应有404 Not Found：网页不存在，500 Internal Server Error：服务器内部出错
# 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误


# 22.2 HTML简介


# 22.3 WSGI接口
# hello.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数


# # server.py
# # 从wsgiref模块导入:
# from wsgiref.simple_server import make_server
# # 导入我们自己编写的application函数:
# from hello import application
#
# # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
# httpd = make_server('', 8000, application)
# print('Serving HTTP on port 8000...')
# # 开始监听HTTP请求:
# httpd.serve_forever()


# 22.4 使用web框架
# Django：全能型Web框架；
# web.py：一个小巧的Web框架；
# Bottle：和Flask类似的Web框架；
# Tornado：Facebook的开源异步Web框架。