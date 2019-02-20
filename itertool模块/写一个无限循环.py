#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'


# 第一种
import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)

# 第二种
import itertools

cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
    print(c)

# 第三种 循环3次结束

import itertools

ns = itertools.repeat('A',3)
for n in ns:
    print(n)

