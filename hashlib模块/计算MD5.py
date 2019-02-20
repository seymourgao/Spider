#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import hashlib

def calc_md5(password):
    if not isinstance(password,str):
        raise TypeError('Please make sure your input is a string.')
    else:
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        print(md5.hexdigest())

