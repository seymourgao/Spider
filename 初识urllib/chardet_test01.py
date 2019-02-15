#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("https://github.com/xiaoxiaogaogao")
    html = response.read()
    chardet = chardet.detect(html)
    print(chardet)