#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

from collections import namedtuple

# 用namedtuple可以很方便地定义一种数据类型
Ponit = namedtuple('Point',['x','y'])
p = Ponit(1,2)
print(isinstance(p,tuple))


# 双向队列 deque
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


# defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
print(dd['key2'])

# OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# ChainMap可以把一组dict串起来并组成一个逻辑上的dict，下面的代码演示了如何查找user和color这两个参数
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


# counter计数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
