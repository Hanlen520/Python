#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 常用的内建模块
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
import base64
import struct


# ===========================================  datetime  ===========================================================
# 15.1.1 获取当前日期和时间
now = datetime.now()
print(type(now))
print(now)


# 15.1.2 获取指定日期和时间
in_now = datetime(2016, 10, 1, 7, 30)
print(in_now)


# 15.1.3 datetime转换为timestamp
print(in_now.timestamp())


# 15.1.4 str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)


# 15.1.5 datetime转换为str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


# 15.1.6 datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now + timedelta(days=2, hours=12))


# 15.1.7 本地时间转换为UTC时间


# 15.1.8 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)


print('*****------*******--------******-------***********-------********')
# ===========================================  collections  ======================================================
# 15.2.1 namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)


# 15.2.2 deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。


# 15.2.3 defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


# 15.2.4 OrderedDict
# 如果要保持Key的顺序，可以用OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


# 15.2.5 Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)


# ======================================  base64   =========================================================
# Base64是一种用64个字符来表示任意二进制数据的方法
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
base64.b64encode(b'binary\x00string')


# ======================================  struct  ======================================================


# ======================================  hashlib  ======================================================


# ======================================  hmac  ======================================================


# ======================================  itertools  ======================================================


# ======================================  contextlib  ======================================================


# ======================================  urllib  ======================================================


# ======================================  XML  ======================================================


# ======================================  HTMLParser  ======================================================

