#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __Author__ = 'gaogao'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
# 方法会打开请求的URL
driver.get('http://www.python.org')
#
assert "Python" in driver.title
# 通过 find_element_by_name 方法寻找网页元素,譬如 find_element_by_* 的方法
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
# 获取网页渲染后的源代码
print(driver.page_source)
