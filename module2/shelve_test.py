#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve

f = shelve.open("shelve_test")  # 打开一个文件存多个pickle序列化

names = ["alex", "rain", "test"]
info = {'name': 'alex', 'age': 22}


f["names"] = names  # 持久化列表
f['info_dic'] = info

print(f["names"])

f.close()
