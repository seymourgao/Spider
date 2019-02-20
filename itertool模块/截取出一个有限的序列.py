#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import itertools

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <=10, natuals)
print(list(ns))