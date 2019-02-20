#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

import hashlib

db = {}

def register(username,password):
    hashlib.md5((password + username + 'the-Salt').encode('utf-8')).hexdigest()
    return db[username]
