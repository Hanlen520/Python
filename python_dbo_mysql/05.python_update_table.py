#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 更新操作用于更新数据表的的数据，以下实例将 my_database表中的 SEX字段全部修改为 'M'，AGE 字段递增1：

import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.31.178", "root", "159357", "my_database")

# 使用cursor()方法创造cursor对象
cursor = db.cursor()

# SQL 更新语句
sql = """ UPDATE my_database.EMPLOYEE SET AGE = AGE +1 
          WHERE SEX = '%c'""" % ('M')


try:
    # 执行SQL语句
    cursor.execute(sql)

    # 提交到数据库执行
    db.commit()
except:
    # 发生数据库回滚
    db.rollback()

# 关闭数据库连接
db.close()