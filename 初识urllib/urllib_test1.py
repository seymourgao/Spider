#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

from urllib import request

if __name__ == "__main__":
    response = request.urlopen("https://github.com/xiaoxiaogaogao")
    html = response.read()
    print(html)



