#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 键盘事件

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# 驱动 Chrome 浏览器
drivers = webdriver.Chrome('./tools/chromedriver.exe')
drivers.get('http://www.baidu.com/')

# 输入框输入内容
drivers.find_element_by_id('kw').send_keys('selenium')
time.sleep(3)

# 删除一个m
drivers.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(3)

# 输入空格键 + “教程”
drivers.find_element_by_id('kw').send_keys(Keys.SPACE)
drivers.find_element_by_id('kw').send_keys(u"教程")
time.sleep(3)

# Ctrl+A 全选输入的内容
drivers.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
time.sleep(3)

# Ctrl+X 剪切输入框里的内容
drivers.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
time.sleep(3)

# Ctrl+V 粘贴
drivers.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
time.sleep(3)

# 操作回车
drivers.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(3)

