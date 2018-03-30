#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os

# 脚本替换文件内容，参数1:要查找内容，参数2:要替换的内容，参数3:文件名
print("脚本名：", sys.argv)
f = open(sys.argv[3], 'r')
f_new = open("new.txt", 'w')
for line in f:
    if sys.argv[1] in line:
        newline = line.replace(sys.argv[1], sys.argv[2])
    else:
        newline = line
    f_new.write(newline)
f.close()
f_new.close()
os.replace("new.txt", sys.argv[3])