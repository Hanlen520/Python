#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 使用执行 SQL INSERT 语句向表 EMPLOYEE 插入记录

import pymysql

# 打开数据库
db = pymysql.connect("192.168.31.178", "root", "159357", "my_database")

# 使用cursor()方法创造一个游标对象cursor
cursor = db.cursor()

# SQL插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
         VALUES('Mi', 'Xi', 20, 'M', 2000000)"""

try:
    # 执行SQL语句
    cursor.execute(sql)

    # 提交到数据库执行
    db.commit()
except:
    # 发生错误回滚
    db.rollback()

# 关闭数据库连接
db.close()

