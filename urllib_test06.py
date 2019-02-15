#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

from urllib import error
from urllib import request

if __name__ == "__main__":
    # 一个不存在的链接
    url = "http://www.gaogao.com/"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode("utf-8")
        print(html)
    except error.URLError as e:
        print(e.reason)


