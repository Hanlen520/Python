#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 1.urllib.request模块是用来打开和读取URLs的；
#              2.urllib.error模块包含一些有urllib.request产生的错误，可以使用try进行捕捉处理；
#              3.urllib.parse模块包含了一些解析URLs的方法；
#              4.urllib.robotparser模块用来解析robots.txt文本文件.它提供了一个单独的RobotFileParser类，通过该类提供的can_fetch()方法测试爬虫是否可以下载一个页面。

from urllib import request
import chardet  # 解析网页编码的库

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)
    html = html.decode("utf-8")
    print(html)