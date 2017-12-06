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
