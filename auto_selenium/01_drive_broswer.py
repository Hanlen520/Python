#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: selenium驱动浏览器

from selenium import webdriver
from time import sleep


# 驱动Edge浏览器
browsers = webdriver.Edge('./tools/MicrosoftWebDriver.exe')
browsers.get("http://www.baidu.com")

# 固定浏览器打开的大小窗口
browsers.set_window_size('300', '300')
sleep(3)

# 使浏览器最大化
browsers.maximize_window()

browsers.find_element_by_id("kw").send_keys("博客园")
browsers.find_element_by_id("su").click()


sleep(5)
browsers.close()