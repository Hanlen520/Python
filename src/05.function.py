#!/usr/bin/evn python
# 五.函数
# 调用函数
import math
print("绝对值：", abs(-123))
print("取整：", int(123.123))
print("小数：", float('123'))
# print("unicode: ", unicode(123));
print("boolean: ", bool(""))


# 定义函数
def my_abs(num):
    if num >= 0:
        return num
    else:
        return -num


print('-5的绝对值为:', my_abs(-5))


# 空函数占位
def non():
    pass


# 函数参数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return ("横向移动了：", nx), ("纵向移动了：", ny)


print(move(100, 100, 60, math.pi/6))


# 函数的参数
def power(x):
    return x * x


print("平方函数计算：", power(9))


def senior_power(num, args):
    s = 1
    while args > 0:
        args = args - 1
        s = s * num
    return s


print("高次函数计算：", senior_power(5, 3))
# 参数可变


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


kw = {'gender': 'male', 'job': 'Engineer'}
person('HuaWei', 23, gender=kw['gender'], job=kw['job'])


# ----------------------5.1.递归函数--------------------
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print('fact(5)的结果为：', fact(5))


# 尾递归优化：解决递归调用栈溢出
def senior_fact(n):
    return fact_iter(n, 1)


def fact_iter(num, result):
    if num == 1:
        return result
    return fact_iter(num - 1, num * result)


print('senior_fact(5)的结果为：', senior_fact(5))




