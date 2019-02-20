#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import hmac

# Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
message = b'hello, world!'
key = b'secret'
h = hmac.new(key,message,digestmod='md5')
print(h.hexdigest())