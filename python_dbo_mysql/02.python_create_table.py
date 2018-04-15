#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 如果数据库连接存在我们可以使用execute()方法来为数据库创建表，如下所示创建表EMPLOYEE：

import pymysql

# 打开数据库
db = pymysql.connect("192.168.31.178", "root", "159357", "my_database")

# 使用cursor()方法创造一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """ CREATE TABLE EMPLOYEE(
          FIRST_NAME CHAR(20) NOT NULL ,
          LAST_NAME CHAR(20) , 
          AGE INT ,
          SEX CHAR(1) ,
          INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()