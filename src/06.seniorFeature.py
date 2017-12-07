#!/usr/bin/evn python
# 六.高级特性
import os  #
from collections import Iterable


def odd_list():
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n = n + 2
    return L


print("1~99之间的奇数为：", odd_list())


# 6.1.切片
# 取section_list部分元素
section_list = ['A', 'B', 'C', 'D', 'E']
print("第一种截取list片段的方法：", [section_list[0], section_list[1], section_list[2]])
r = []
n = 3
for i in range(n):
    r.append(section_list[i])
print("第二种截取list片段的方法：", r)
print("第三种截取list片段的方法：", section_list[0:3])

L = list(range(100))
print("L这个list为：", L)
print("截取前10位：", L[0:10])
print("截取后十位：", L[-10:])
print("前十位数每两个取一个：", L[:10:2])
print("所有数，每5个取一个：", L[::5])
print("原样复制这个list：", L[:])

print("ABCDEFG"[:3])
print('ABCDEFG'[::2])


# 利用切片操作，实现一个trim()函数，去掉字符串首尾的空格
# def section_trim(string):
#     if len(string) == 0:
#         return string
#     elif string[0] == ' ':
#         return (section_list(string[1:]))
#     elif string[-1] == ' ':
#         return (section_list(string[:-1]))
#     return string
# section_list(" Hello ")


# ===================================================================================================================
# 6.2.迭代
iteration_list = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
for key in iteration_list:
    print("iteration_list的key为：", key)


# 判断对象是否可迭代，通过collections模块的Iterable类型判断
# from collections import Iterable
print("判断'abc'是否可迭代：", isinstance('abc', Iterable))
print("判断[1, 2, 3]是否可迭代：", isinstance([1, 2, 3], Iterable))
print("判断123是否可迭代：", isinstance(123, Iterable))


# 实现list的下标循环
for i, value in enumerate(iteration_list):
    print(i, value)


# ===================================================================================================================
# 6.3.列表生成式




# ===================================================================================================================
# 6.3.列表生成式
L = []
for x in range(1, 11):
    L.append(x)


print("生成1-10的数：", L)
print("生成平方数：", [x * x for x in range(1, 11)])
print("取偶数次的平方：", [x * x for x in range(1, 11) if x % 2 == 0])
print("两层循环生成全排列：", [m + n for m in 'ABC' for n in 'XYZ'])


# 利用列表生成式列出当前目录下的所有文件和文件名
print("目录下的所有文件和目录名：", [d for d in os.listdir('.')])


#列表式生成list
# d = {'X': 'A', 'Y': 'B', 'Z': 'C'}
# for k, v in d.iteritems():
#     print (k, '=', v)
# print([k + '=' + v for k, v in d.iteritems()])


# L = ['HELLO', 'World', 19, 'APPLE', None]
# print([s.lower() for s in L])


# ===================================================================================================================
# 6.4.生成器--把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
for ng in g:
    print("生成器获取元素：", ng)
# print("生成器获取元素：", g.next())


# 斐波拉切数列
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1

print(fab(6))
