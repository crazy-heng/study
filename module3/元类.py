#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 类名
class_name = 'Chinese'
# 类的父类
class_bases = (object,)
# 类体
class_body = """
country='China'
def __init__(self,name,age):
    self.name=name
    self.age=age
def talk(self):
    print('%s is talking' %self.name)
"""
class_dic = {}
exec(class_body, globals(), class_dic)
Foo = type(class_name, class_bases, class_dic)  # 实例化type得到对象Foo，即我们用class定义的类Foo
