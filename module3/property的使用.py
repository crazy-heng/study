#!/usr/bin/env python
# -*- coding: utf-8 -*-


class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height

    @property
    def bmi(self):
        return self.weight / (self.height**2)


p1 = People('egon', 75, 1.85)
print(p1.bmi)  # 加了property就不用p1.bmi()了
# 修改属性必须添加装饰器


class Foo:
    def __init__(self, val):
        self.__NAME = val  # 将所有的数据属性都隐藏起来

    @property
    def name(self):
        return self.__NAME  # obj.name访问的是self.__NAME(这也是真实值的存放位置)

    @name.setter
    def name(self, value):
        if not isinstance(value, str):  # 在设定值之前进行类型检查
            raise TypeError('%s must be str' % value)
        self.__NAME = value  # 通过类型检查后,将值value存放到真实的位置self.__NAME

    @name.deleter
    def name(self):
        raise TypeError('Can not delete')


f = Foo('egon')
f.name = 'EGON'
print(f.name)
