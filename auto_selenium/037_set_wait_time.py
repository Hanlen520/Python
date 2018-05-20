#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 设置等待时间

# sleep()：设置固定休眠时间。python的time包提供了休眠方法sleep() ，
# 导入time包后就可以使用sleep() 进行脚本的执行过程进行休眠。

# implicitly_wait()：是 webdirver 提供的一个超时等待。
# 隐的等待一个元素被发现，或一个命令完成。 如果超出了设置时间的则抛出异常。

# WebDriverWait()：同样也是 webdirver 提供的方法。
# 在设置时间内，默认每隔一段时间检测一次当前 页面元素是否存在，如果超过设置时间检测不到则抛出异常。

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

# 驱动 Chrome 浏览器
drivers = webdriver.Chrome('./tools/chromedriver.exe')
drivers.get('http://www.baidu.com/')

# WebDriverWait()使用
element = WebDriverWait(drivers, 10).until(lambda driver:drivers.find_element_by_id('kw'))
element.send_keys('selenium')

# 添加智能等待
drivers.implicitly_wait(30)
drivers.find_element_by_id('su').click()

# implicitly_wait()方法比 sleep() 更加智能，后者只能选择一个固定的时间的等待，前者可以在一个时间 范围内智能的等待。
# 添加固定休眠时间
time.sleep(5)

# 补充时间等待操作：
# WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
# timeout - 最长超时时间，默认以秒为单位
# poll_frequency- 休眠时间的间隔（步长）时间，默认为 0.5 秒
# ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。
# until(method,message=’’) - 调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。
# until_not(method,message=’’) - 调用该方法提供的驱动程序作为一个参数，直到返回值为 False。