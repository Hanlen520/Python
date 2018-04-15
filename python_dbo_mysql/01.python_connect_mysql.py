#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description:

import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.31.178", "root", "159357", "my_database")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("DATABASE VERSION: %s " % data)

# 关闭数据库
db.close()
