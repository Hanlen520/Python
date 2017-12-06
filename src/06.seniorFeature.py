#!/usr/bin/evn python
# 六.高级特性


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


