#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import re

#识别是不是邮件地址格式
def is_valid_email(addr):
    ver_addr = re.compile(r'^\w+.\w+@\w+.\w+$')
    if re.match(ver_addr):
        return True
    else:
        return False

#提取邮件名字
def name_of_email(addr):
    get_name = re.match(r"^<?([\w\s])>?[\s\w]@(\w+.\w+)$",addr).group(1)
    return get_name

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
