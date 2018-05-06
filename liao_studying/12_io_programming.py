#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: IO编程
from io import StringIO
from io import BytesIO
import os

# ======================================================================================================================
# 12.1 文件读写

# 12.1.1 读文件
# 》》》》》》1.要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
# 》》》》》》2.如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存
# 》》》》》》3.最后一步是调用close()方法关闭文件


def read_file():
    try:
        f = open("./__init__.py", 'r')
        print(f.read())
    finally:
        if f:
            f.close()
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：


with open("./__init__.py", 'r') as f:
    # print(f.read())
    for line in f.readlines():
        print(line.strip())


# 12.1.2 file-like Object
# open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。


# 12.1.3 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可


# 12.1.4 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')


# 12.1.5 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件


# ======================================================================================================================
# 12.2 StringIO和BytesIO
# 12.2.1 StringIO---是在内存中读写str

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readlines()
    if s == ' ':
        break
    print(s.strip())


# 12.2.2 如果要操作二进制数据，就需要使用BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())


# ======================================================================================================================
# 12.3. 操作文件和目录
# 12.3.1 获取操作系统信息：
if os.name == 'nt':
    print("this is windows.")

print(os.uname())


# 12.3.2 环境变量
print(os.environ)
print(os.environ.get('PATH'))


# 12.3.3 操作文件和目录
print(os.path.abspath('.'))     # 查看当前目录的绝对路径
os.path.join('/Users/michael', 'testDir')   # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('/Users/michael/testDire')     # 创建一个目录
os.rmdir('/Users/michael/testDire')     # 删除一个目录
os.path.split('/Users/michael/testDire/file.txt')      # os.path.split()函数，把一个路径拆分为两部分，后一部分是最后级别的目录或文件名
os.path.splitext('/path/to/file.txt')       # os.path.splitext()可以直接让你得到文件扩展名
os.rename('test.txt', 'test.py')        # 文件重命名
os.remove('test.py')        # 删除文件


# ======================================================================================================================
# 12.4 序列化 --- 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

# 12.4.1 JSON