#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

# 演示如何绘制散点图和柱状图
from matplotlib import pyplot as plt

# 主要x 和y的个数要相同，不然会报错
x = [7, 6, 7, 8]
y = [7, 3, 8, 3]

x1 = [2, 5, 1, 9]
y1 = [5, 3, 2, 7]

# 绘制散点图用scatter函数
plt.scatter(x, y, color='b', label='Line One')
plt.scatter(x1, y1, color='r', label='Line Two')

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()

# 显示网格线
# plt.grid(True,color='k')


plt.show()

