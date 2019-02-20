#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
print(re.split(r'[\s\,\;]+','a,b,;;;;   c       d'))

# 分组
g = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|'
             r'3[0-9]|4[0-9]|5[0-9]|[0-9])$', g)
print(m.groups())

# 贪婪/非贪婪匹配
print(re.match(r'^(\d+)(0*)$','1023000').groups(0))
print(re.match(r'^(\d+?)(0*)$','1023000').groups(0))

# 编译模板，直接调用
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-8086').groups())
