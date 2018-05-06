#!/usr/bin/evn python
# -*- coding:utf-8 -*-

__author__ = 'Crisimple'


import logging
# 十一.错误/调试和测试
# ======================================================================================================================
# 11.1.错误处理
# 由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。

# 记录错误（紧接着下面的为记录错误的示例）


def fooo(s):
    return 10 / int(s)


def bar(s):
    return fooo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print("END")


# 抛出错误【因为错误是class，捕获一个错误就是捕获到该class的一个实例；python内置的函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误】
print("---------------------华丽的分割线-------------------------------")


class MyError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise MyError("invalid value: %s" % s)
    return 10 / n


foo('0')


# ======================================================================================================================
# 11.2.调试
# 11.2.1.断言（调试程序时写太多的print，后面还要删除，因此出来了断言）
# 启动Python解释器时可以用-O参数来关闭assert[python -O err.py]
print("---------------------华丽的分割线-------------------------------")


def asserted(s):
    n = int(s)
    # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    # 如果断言失败，assert语句本身就会抛出AssertionError
    assert n != 0, 'n is zero'
    return 10 / n


def main():
    asserted('0')


print("---------------------华丽的分割线-------------------------------")
# 11.2.2. logging


logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


print("---------------------华丽的分割线-------------------------------")
# 11.2.3. pdb（启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。）


# ======================================================================================================================
# 11.3 单元测试（单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。）
# setUp与tearDown


# ======================================================================================================================
# 11.4 文档测试


