#!/usr/bin/evn
# -*- coding: utf-8 -*-
# by author: crisimple
# 七.函数式编程
import builtins
from functools import reduce
import functools

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


# 7.1.1.map()/reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def map_f(map_item):
    return map_item * map_item


r_map = map(map_f, [1, 2, 3, 4])
print(list(r_map))
print(list(map(str, [1, 2, 3, 4, 5])))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def sum_reduce(xb, yb):
    return xb + yb


print(reduce(sum_reduce, [1, 2, 3, 4, 5]))


# ----------------------------------------------------------------------------------------------------------------------
# 7.1.2.filter---filter()函数用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 在一个list中，删掉偶数，只保留奇数
def is_odd(filter_num):
    return filter_num % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 把一个序列中的空字符串删掉
def not_empty(empty_item):
    return empty_item and empty_item.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 用filter求素数


# ----------------------------------------------------------------------------------------------------------------------
# 7.1.3.sorted--排序算法
print(sorted([36, 5, -12, 9, -21]))


# 按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))


# 字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))


# 忽略大小写字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# ======================================================================================================================
# 7.2.返回函数


# ======================================================================================================================
# 7.3.匿名函数
print(list(map(lambda x_item: x_item * x_item, [1, 2, 3, 4])))


# ======================================================================================================================
# 7.4.装饰器--在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)


# ======================================================================================================================
# 7.5.偏函数
print(int('12345'))
print(int('12345', base=8))
print(int('12345', base=16))


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
def int_two(int_item, base=2):
    return int(int_item, base)


print("二进制转换函数：", int_two('1000000'))


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int_two_next = functools.partial(int, base=2)


print("二进制转换函数：", int_two_next("1000000"))
