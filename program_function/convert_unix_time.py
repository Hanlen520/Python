#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 将普通时间转换为普通的时间戳

import datetime
import time

# now_time = str(datetime.datetime.now())
# print("now_time: ", now_time)
start_time = '2018-05-22 22:59:42'
end_time = '2018-05-23 22:59:42'


def format_time(value):

    # 将时间转换为时间组
    timeArray = time.strptime(value, "%Y-%m-%d %H:%M:%S")
    print(timeArray)

    # 转换为时间戳
    timestamp = time.mktime(timeArray)

    # 返回时间戳
    return timestamp


format_time(start_time)

# timeArray = time.strptime("2018-05-22 22:53:18", "%Y-%m-%d %H:%M:%S")
# print(timeArray)
# timestamp = time.mktime(timeArray)
# print(timestamp)