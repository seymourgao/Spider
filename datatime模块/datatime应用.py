#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

from datetime import datetime

# 当前时间
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# datetime转换为timestamp
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
print(dt.timestamp())

#timestamp转换为datetime
dt2 = 1429417200.0
print(datetime.fromtimestamp(dt2))
print(datetime.utcfromtimestamp(dt2))

# str转换为datetime
cdday = datetime.strptime('2019-1-23 19:45:23','%Y-%m-%d %H:%M:%S')
print(cdday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))