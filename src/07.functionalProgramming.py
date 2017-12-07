#!/usr/bin/evn
# -*- coding: utf-8 -*-
# by author: crisimple
# 七.函数式编程
import builtins

# 7.1.高阶函数
# 变量可以指向函数
x = abs(-10)
print(x)

# 函数名也是变量
# abs = 10
# print(abs(-10))


# 传入函数--既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(xa, ya, f):
    return f(xa) + f(ya)


print(add(-5, -6, abs))



# 7.1.1.map/reduce