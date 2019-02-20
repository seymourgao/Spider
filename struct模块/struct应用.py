#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import struct
# https://docs.python.org/3/library/struct.html#format-characters

st = struct.pack('>I',10240099)
print(st)

st2 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(st2)

# bmp文件
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
st3 = struct.unpack('<ccIIIIIIHH', s)
print(st3)


