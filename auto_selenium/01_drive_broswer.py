#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: selenium驱动浏览器

from selenium import webdriver
from time import sleep

# ======================= WebDriver驱动浏览器基本操作 ====================================

# 驱动Edge浏览器
browsers = webdriver.Edge('./tools/MicrosoftWebDriver.exe')

first_url = 'http://www.baidu.com'
browsers.get(first_url)

# 固定浏览器打开的大小窗口
browsers.set_window_size('300', '300')
sleep(3)

# 使浏览器最大化
browsers.maximize_window()

# 打印当前页的url地址
print("First page's url is: %s" % first_url)


# 在百度页面寻找到 "新闻" 文本关键字并点击
browsers.find_element_by_link_text('新闻').click()

# browsers.find_element_by_id("kw").send_keys("博客园")
# browsers.find_element_by_id("su").click()

print("Current page's url is: %s" % first_url)


# ========================= WebElement接口常用方法 ====================================
sleep(3)

# 百度新闻搜索框size获取
# newSerach_size = browsers.find_element_by_id('ww').size
# print("百度新闻搜索框size: %s" % newSerach_size)


# 获取元素的文本
# text_content = browsers.find_element_by_class_name('cy').text
# print(text_content)


# 获取属性值
# attribute_value = browsers.find_element_by_id('kw').get_attribute('type')
# # print(attribute_value)


# 设置该元素是否用户可见
# display_result = browsers.find_element_by_id('kw').is_displayed()
# print(display_result)


sleep(5)
# browsers.close()

