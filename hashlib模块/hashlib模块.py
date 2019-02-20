#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。摘要算法又称哈希算法、散列算法，它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha256 = hashlib.sha256()
sha256.update('how to use sha256 in '.encode('utf-8'))
sha256.update('python hashlib?'.encode('utf-8'))
print(sha256.hexdigest())

sha512 = hashlib.sha512()
sha512.update('how to use sha512 in '.encode('utf-8'))
sha512.update('python hashlib?'.encode('utf-8'))
print(sha512.hexdigest())

# 摘要算法应用
# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以
# 在不存储明文口令的情况下验证用户口令。




