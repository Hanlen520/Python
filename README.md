# python
python学习笔记

#!/usr/bin/evn Python
#! -*- coding: UTF-8 -*-
# 函数篇

#**调用函数
print("绝对值：",abs(-123));
print("取整：",int(123.123));
print("小数：",float('123'));
#print("unicode: ", unicode(123));
print("boolean: ", bool(""));


#**定义函数
def my_abs(num):
    if num>=0:
        return num;
    else:
        return -num;
print('-5的绝对值为:',my_abs(-5));
#空函数，什么也不做
def non():
    pass;

import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle);
    ny = y - step * math.sin(angle);
    return ("横向移动了：",nx), ("纵向移动了：",ny);
print(move(100,100,60,math.pi/6));

#**函数的参数
def power(x):
    return x * x;
print("平方函数计算：",power(9));

def senior_power(num, args):
    s = 1;
    while args > 0:
        args = args -1;
        s = s * num;
    return s;
print("高次函数计算：", senior_power(5,3));
#参数可变
def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw);
kw={'gender':'male', 'job':'Engineer'};
person('JiangHeng',23,gender=kw['gender'],job=kw['job']);
person('JiangHeng',23,**kw);

