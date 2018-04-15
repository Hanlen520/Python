#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 小于 20 的所有数据

import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.31.178", "root", "159357", "")

# 操作cursor()方法创造cursor对象
cursor = db.cursor()

# 删除SQL语句
sql = """DELETE FROM my_database.EMPLOYEE 
         WHERE AGE < '%d'""" % (20)

try:
    # 执行删除SQL
    cursor.execute()

    # 提交修改
    db.commit()
except:
    # 发生错误时发生数据库回滚
    db.rollback()

# 关闭数据库连接
db.close()