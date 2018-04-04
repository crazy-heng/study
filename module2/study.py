#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

# 函数1
# def sum_nu(*args):
#     a = 0
#     for i in args:
#         a += i
#     print(a)
#
#
# sum_nu(1, 2, 3, 4, 5)


# 函数2
# def replace_file(name, old_content, new_content):
#     f = open(name, 'r')
#     f1 = f.read()
#     f.close()
#     f1 = re.sub(old_content, new_content, f1)
#     f = open(name, 'w')
#     f.write(f1)
#     f.close()
#
#
# replace_file("test.txt", "HEHE", "new")


# 函数3
# def check(a):
#     print("wrong") if len(a) == 0 else print(a)
#
#
# check("")

# 函数4
def check_dic(d, long):
    for i in d.keys():
        if len(d[i]) > long:
            d[i] = d[i][:long]
    print(d)


dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
check_dic(dic, 1)


