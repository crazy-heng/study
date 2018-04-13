#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

li = ["1380000000", "14900000000", "15200000000", "abc123", "96810000"]
for i in li:
    phone = re.match("1([3|5|8])\d{9}", i)
    print("%s 是手机号" % i) if phone else print("%s 不是手机号" % i)

li1 = ["a@b.com", "1@e.com.cn", "22kkk.qq", "a_b@eq-r.net"]
for i in li1:
    mail = re.match("\w+@\w+.[com|net|cc|cn|org]", i)
    print("%s 是邮箱" % i) if mail else print("%s 不是邮箱" % i)