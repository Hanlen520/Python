#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 3.4 鼠标事件

from selenium import webdriver
from time import sleep


# 记载Chrome浏览器驱动
mouse_browser = webdriver.Chrome('./tools/chromedriver.exe')


# 配置要测试验证的URL地址
loading_url = 'https://pan.baidu.com/'
mouse_browser.get(loading_url)

# 打印加载的URL值
print("Current page's url is: %s" % loading_url)


# 最大化浏览现实
mouse_browser.maximize_window()


# 浏览器休眠3s
sleep(3)


# 点击 "百度网盘页面" 的账号密码登陆元素
mouse_browser.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn').click()
# 输入手机/邮箱/用户名
mouse_browser.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('')
mouse_browser.find_element_by_id('TANGRAM__PSP_4__password').send_keys('')
# 输入完信息等待1s，缓冲
sleep(1)
# 点击登陆按钮
mouse_browser.find_element_by_id('TANGRAM__PSP_4__submit').submit()
# 登陆成功，页面加载等待2s
sleep(2)

# 由于百度网盘新登陆会弹窗 "新增我的卡包，证件存储更加安全" 的提示，这时候的页面即为新的页面，需要重新定向页面
search_windows = mouse_browser.current_window_handle

mouse_browser.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/p[2]').submit()


