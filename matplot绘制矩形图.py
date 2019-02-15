#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

from matplotlib import pyplot as plt

# 演示如何绘制散点图和柱状图
from matplotlib import pyplot as plt

# 主要x 和y的个数要相同，不然会报错
x = [2, 4, 6, 8]
y = [7, 3, 8, 3]

x1 = [1, 3, 5, 7]
y1 = [6, 7, 2, 6]

# 绘制柱状图用bar函数
plt.bar(x, y, color='g', label='Line One')
plt.bar(x1, y1, color='r', label='Line Two')

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()

# 显示网格线
# plt.grid(True,color='k')


plt.show()