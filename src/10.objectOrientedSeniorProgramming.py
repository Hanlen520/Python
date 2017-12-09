#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# by author: crisimple


# ======================================================================================================================
# 10.1.使用__slots__
class Student(object):
    pass


# 给实例绑定一个属性
s = Student()
s.name = 'Crisimple'
print(s.name)