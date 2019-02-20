#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import xlwt
import xlrd
from os import listdir
from os.path import isfile,join

# 用户输入目录
mypath = raw_input("Please enter the directory path for the input files: ")
# 获得所有的TXT文件
textfiles = [join(mypath,f) for f.inlistdir(mypath) if isfile(join(mypath,f)) and '.txt' in  f]

# 判断是否为数字
def is_number(s):
    try:
