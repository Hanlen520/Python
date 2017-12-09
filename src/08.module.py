#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# by author: crisimple
import sys

# 八.模块
# 在Python中，一个.py文件就称之为一个模块（Module）。
# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。


# ======================================================================================================================
# 8.1.使用模块
__author__ = 'Michael Liao'


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello Python')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()

# 作用域
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用


# ======================================================================================================================
# 8.2.安装第三方模块

