#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 常用第三方模块
import requests

# ==================================  Pillow  =========================================================
# 16.1 Pillow
# 16.1.1 操作图像


# ================================== requests ==========================================================
r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)


# ================================= chardet ===========================================================


# ================================ psutil =============================================================
