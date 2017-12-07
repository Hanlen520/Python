# python
python学习笔记


import os #


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
