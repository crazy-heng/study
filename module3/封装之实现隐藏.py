#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 隐藏属性


class A:
    __x = 1  # _A__x = 1

    def __init__(self, name):
        self.__name = name

    def __foo(self):  # def _A__foo(self):
        print('run foo')

    def bar(self):
        self.__foo()  # _A__foo()
        print('from bar')


class B(A):
    def __foo(self):
        print("run B foo")


a = A('egon')
print(a._A__name)
a.bar()

'''
变形的特点
    1、在类外部无法直接obj.__AttrName
    2、在类内部是可以直接使用：obj.__AttrName
    3、子类无法覆盖父类__开头的属性
注意
    1、并非正真隐藏可以a._A__N
    2、变形只在类定义阶段产生
    3、
'''

# 正常情况


class A:
    def fa(self):
        print('from A')

    def test(self):
        self.fa()


class B(A):

    def fa(self):
        print('from B')


b = B()
b.test()
# from B


# 把fa定义成私有的，即__fa
class C:
    def __fa(self):  # 在定义时就变形为_A__fa
        print('from A')

    def test(self):
        self.__fa()  # 只会与自己所在的类为准,即调用_A__fa


class D(C):
    def __fa(self):
        print('from B')


d = D()
d.test()
# from A
