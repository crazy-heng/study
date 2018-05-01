#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1、封装数据属性：明确区分内外，控制外部对隐藏属性的操作行为


class Teacher:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print('姓名:%s,年龄:%s' % (self.__name, self.__age))

    def set_info(self, name, age):
        if not isinstance(name, str):
            raise TypeError('姓名必须是字符串类型')
        if not isinstance(age, int):
            raise TypeError('年龄必须是整型')
        self.__name = name
        self.__age = age


t = Teacher('egon', 18)
t.tell_info()

t.set_info('egon', 19)
t.tell_info()

# 2、封装方法：隔离复杂度


class ATM:

    def __card(self):
        print('插卡')

    def __auth(self):
        print('用户认证')

    def __input(self):
        print('输入取款金额')

    def __print_bill(self):
        print('打印账单')

    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


a = ATM()
a.withdraw()
