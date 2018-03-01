# -*- coding: utf-8 -*-
# by author: Crisimple
# description:格式化输出

name = input("Please input your name: ")
sex = input("Please inout your sex: ")
job = input("PLease input your job: ")
address = input("Please input your address: ")

message = '''
-------------The information of %s-----------------
   name:       %s
   sex :       %s
   job :       %s
address:       %s
-------------This is the end line------------------
''' %(name, name, sex, job, address)

print(message)




